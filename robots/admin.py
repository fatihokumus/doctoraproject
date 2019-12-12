from django.contrib import admin
from .models import Robot, RobotModel, Tenant, SubNet, Map, Sticker, Mapping,  TransferredObject, WorkStation, WaitingStation, ChargingStation, TransferVehicle

admin.site.register([Robot, RobotModel, Tenant, SubNet, Map, Sticker, Mapping,  TransferredObject, WorkStation, WaitingStation, ChargingStation, TransferVehicle])

