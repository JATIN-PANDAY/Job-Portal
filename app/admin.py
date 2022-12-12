from django.contrib import admin
from  app.models import UserMaster
from  app.models import Candidate
from  app.models import Company

# Register your models here.
admin.site.register(UserMaster)
admin.site.register(Candidate)
admin.site.register(Company)