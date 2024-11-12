from django.urls import path

from . import views
from .views import (InsertVolunteer, InsertSkill, InsertCategory,
                    InsertOrganization, UpdateEventDetail, InsertEvent)

app_name = 'nonprofit'
urlpatterns = [
    path("", views.index, name="index"),
    path("volunteer/", views.volunteer_home, name="volunteer_home"),
    path("event/", views.event_home, name="event_home"),
    path('<int:pk>/update/volunteer/', views.update_volunteer_details, name='update_volunteer'),
    path('insert/volunteer/', InsertVolunteer.as_view(), name='insert_volunteer'),
    path('<int:pk>/delete/', views.delete_volunteer, name='delete'),
    path('insert/skill/', InsertSkill.as_view(), name='insert_skill'),
    path('insert/category/', InsertCategory.as_view(), name='insert_category'),
    path('insert/organization/', InsertOrganization.as_view(), name='insert_organization'),
    path('<int:pk>/update/event/', UpdateEventDetail.as_view(), name='update_event'),
    path('insert/event/', InsertEvent.as_view(), name='insert_event'),
]