from django.contrib import admin
from .models import Category, Event, Volunteer, Organization, Skill, Participation


admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Volunteer)
admin.site.register(Organization)
admin.site.register(Skill)
admin.site.register(Participation)
