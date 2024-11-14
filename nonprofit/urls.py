from django.urls import path
from . import views


app_name = 'nonprofit'
urlpatterns = [
    path("", views.index, name="index"),
    path("volunteer/", views.volunteer_home, name="volunteer_home"),
    path("event/", views.event_home, name="event_home"),
    path('<int:pk>/update/volunteer/', views.update_volunteer_details, name='update_volunteer'),
    path('insert/volunteer/', views.insert_volunteer, name='insert_volunteer'),
    path('<int:pk>/delete/volunteer/', views.delete_volunteer, name='delete_volunteer'),
    path('insert/skill/', views.insert_skill, name='insert_skill'),
    path('insert/category/', views.insert_category, name='insert_category'),
    path('insert/organization/', views.insert_organization, name='insert_organization'),
    path('<int:pk>/update/event/', views.update_event_details, name='update_event'),
    path('insert/event/', views.insert_event, name='insert_event'),
    path('<int:pk>/delete/event/', views.delete_event, name='delete_event'),
    path('<int:pk>/filterby/category/', views.filter_event_by_category, name='filter_by_category'),
    path('<int:pk>/filterby/organization/', views.filter_event_by_organization, name='filter_by_organization'),
    path('<int:pk>/filterby/skill/', views.filter_volunteer_by_skill, name='filter_by_skill'),
]
