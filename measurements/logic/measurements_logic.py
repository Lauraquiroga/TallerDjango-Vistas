from ..models import Measurement
from variables.logic import variables_logic as vl
from django.db import models
from datetime import datetime


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(ms_pk):
    measurement = Measurement.objects.get(pk=ms_pk)
    return measurement

def update_measurement(ms_pk, new_ms):
    measurement = get_measurement(ms_pk)
    measurement.variable = vl.get_variable(new_ms["variable"])
    measurement.value = new_ms["value"]
    measurement.unit = new_ms["unit"]
    measurement.place = new_ms["place"]
    measurement.dateTime = datetime.strptime(new_ms["dateTime"], "%Y-%m-%d %H:%M")
    measurement.save()
    return measurement

def create_measurement(ms):
    measurement = Measurement( variable= vl.get_variable(ms["variable"]),
                            value=ms["value"], 
                            unit=ms["unit"],
                            place=ms["place"],
                            dateTime=ms["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(ms_pk):
    measurement = get_measurement(ms_pk)
    measurement.delete()
    return measurement

