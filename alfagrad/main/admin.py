from django.contrib import admin

# Register your models here.
from .models import LastProjects, BaseLevel, Location, Contacts

admin.site.register(LastProjects)
admin.site.register(BaseLevel)
admin.site.register(Location)
admin.site.register(Contacts)



