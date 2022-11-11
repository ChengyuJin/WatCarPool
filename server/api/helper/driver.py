import mysql.connector
from datetime import datetime
from sqlite3 import OperationalError
import json

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="WCP_DB",
)

cursor = db.cursor()

def execute_createTrip(driverID, vehicleID, origin, destination, departTime, price, description):
    command = "SELECT COUNT(*) FROM Trip WHERE driverID = %s AND vehicleID = %s"
    val = (driverID, vehicleID)
    cursor.execute(command, val)
    result = cursor.fetchone()
    tripID = result[0] + 1
    time = datetime.strptime(departTime, "%Y-%m-%d %H:%M:%S")
    if time <= datetime.now():
        return { "status": "Fail", "errorMessage": "ERROR: Trip time must be greater than the current time" }
    if origin == destination:
        return { "status": "Fail", "errorMessage": "ERROR: Origin and destination must be different" }
    try:
        command = "INSERT INTO Trip VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (driverID, vehicleID, tripID, origin, destination, departTime, price, description)
        cursor.execute(command, val)
        db.commit()
    except OperationalError as msg:
        print("Command skipped: ", msg)
    return { "status": "Success" }
