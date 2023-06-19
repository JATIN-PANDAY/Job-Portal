from django.contrib import admin

from  app.models import *

# Register your models here.
admin.site.register(UserMaster)
admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(jobpost)
admin.site.register(Applylist)
admin.site.register(contact)