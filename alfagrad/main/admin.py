from django.contrib import admin

# Register your models here.
from .models import LastProjects, BaseLevel, Location, Contacts, SubText, AskQuestions

admin.site.register(LastProjects)
admin.site.register(BaseLevel)
admin.site.register(Location)
admin.site.register(Contacts)
admin.site.register(SubText)
admin.site.register(AskQuestions)



