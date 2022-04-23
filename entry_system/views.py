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
        person = Person.objects.get(roll = request.data["roll_no"])
        hostel_id = request.data["hostel_id"]
        time = timezone.now()

        new_log = Log(person = person, hostel_id = hostel_id, time=time, activity=activityType)
        new_log.save()

        return Response("Register Successful")

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