from django.contrib import admin

from .models import EduLevel, MaritalStatus, AngerExp, ProfileVariables

admin.site.register([EduLevel, MaritalStatus, AngerExp, ProfileVariables])
