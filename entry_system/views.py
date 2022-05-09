from django.shortcuts import render
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PersonSerializer

from .models import Person, Log

# Create your views here.

@api_view(['GET'])
def getData(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def registerEntry(request):
    if request.method == "POST":
        return registerLog(request, 'EN')

@api_view(['POST'])
def registerExit(request):
    if request.method == "POST":
        return registerLog(request, 'EX')

def registerLog(request, activityType):
     if request.method == "POST":
        valid, data = getAndValidateData(request.data, ["roll_no", "hostel_id"])
        if not valid:
            return Response({'detail':'Invalid request format'}, status=400)

        studInHostel = personInHostel(data["roll_no"], data["hostel_id"])

        if studInHostel and activityType == 'EN':
            return Response({'detail':'Can not register entry as student is already in the hostel'}, status=403)
        if not studInHostel and activityType == 'EX':
            return Response({'detail':'Can not register exit as student is not in the hostel'}, status=403)

        person = Person.objects.get(roll = data["roll_no"])
        hostel_id = data["hostel_id"]
        time = timezone.now()


        new_log = Log(person = person, hostel_id = hostel_id, time=time, activity=activityType)
        new_log.save()

        return Response({'detail': 'Register Successful'}, status=200)

def personInHostel(roll_no, hostel_no):
    logs = Log.objects.filter(person__roll=roll_no, hostel_id=hostel_no)

    entries = logs.filter(activity = 'EN').count()
    exit = logs.filter(activity = 'EX').count()

    return (entries>exit)

def getAndValidateData(data, fields):
    data_valid = True
    v_data = dict()
    for field in fields:
        if field not in data.keys():
            data_valid = False
            v_data[field] = None
        else:
            v_data[field]=data[field]

    return (data_valid, v_data)

@api_view(['GET'])
def getPeopleInside(request, hostel_id):
    everyone = Log.objects.filter(hostel_id=hostel_id).values('person').distinct()
    dist_rolls = [per['person'] for per in everyone]

    inside = []

    for roll in dist_rolls:
        entries = Log.objects.filter(person=roll).filter(activity='EN').count()
        exits = Log.objects.filter(person=roll).filter(activity='EX').count()

        if entries > exits:
            inside.append(Person.objects.get(roll=roll))

    serializer = PersonSerializer(inside, many=True)

    return Response(serializer.data)