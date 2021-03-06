# Hostel Entry System - Backend
A backend server implementation to serve the data and processing needs of an entry system for recording who enters and exits the hostels of IIT Bombay

Language used: Python

## Current Features
- Record an *entry*
- Record an *exit*
- Get a list of students inside a hostel

## Packages used
### Django
Install using `pip install django`
### Django REST framework
Install using `pip install djangorestframework`
### Others
Native python libraries

## API end-points

### Record Entry
#### URL
Endpoint: POST `/logentry`
#### POST data parameters
<table>
    <tbody>
        <tr>
            <td><b>Name</b></td>
            <td><b>Required</b></td>
            <td><b>Description</b></td>
            <td><b>Example</b></td>
        </tr>
        <tr>
            <td>id</td>
            <td>required</td>
            <td>The roll number of student whose entry is being recorded</td>
            <td>210070028</td>
        </tr>
        <tr>
            <td>hostel_id</td>
            <td>required</td>
            <td>The ID of the hostel into which the entry is being recorded</td>
            <td>17</td>
        </tr>
    </tbody>
</table>

### Record Exit
#### URL
Endpoint: POST `/logexit`
#### POST data parameters
<table>
    <tbody>
        <tr>
            <td><b>Name</b></td>
            <td><b>Required</b></td>
            <td><b>Description</b></td>
            <td><b>Example</b></td>
        </tr>
        <tr>
            <td>id</td>
            <td>required</td>
            <td>The roll number of student whose exit is being recorded</td>
            <td>210070028</td>
        </tr>
        <tr>
            <td>hostel_id</td>
            <td>required</td>
            <td>The ID of the hostel out of which the exit is being recorded</td>
            <td>17</td>
        </tr>
    </tbody>
</table>

### Get students inside hotel
#### URL
Endpoint: GET `/whosinside/<int:hostel_id>`
#### URL Parameters
<table>
    <tbody>
        <tr>
            <td><b>Name</b></td>
            <td><b>Required</b></td>
            <td><b>Description</b></td>
            <td><b>Example</b></td>
        </tr>
        <tr>
            <td>hostel_id</td>
            <td>required</td>
            <td>The ID of the hostel whose information is required</td>
            <td>17</td>
        </tr>
    </tbody>
</table>