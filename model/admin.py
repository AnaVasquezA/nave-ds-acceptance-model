from django.contrib import admin

from .models import EduLevel, MaritalStatus, AngerExp, ProfileVariables, LegalBack, Earnings, EcoDependents, HousingTime, DrivingTime, PlatRegistTime

admin.site.register([EduLevel, MaritalStatus, AngerExp, ProfileVariables, LegalBack, Earnings, EcoDependents, HousingTime, DrivingTime, PlatRegistTime])
