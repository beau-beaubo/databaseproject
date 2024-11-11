from django.urls import path

from . import views
from .views import UpdateVolunteerDetail, InsertVolunteer

app_name = 'nonprofit'
urlpatterns = [
    path("", views.index, name="index"),
    path("volunteer/", views.volunteer_home, name="volunteer_home"),
    path("event/", views.event_home, name="event_home"),
    path('<int:pk>/update/', UpdateVolunteerDetail.as_view(), name='update'),
    path('insert/', InsertVolunteer.as_view(), name='insert'),
    path('<int:pk>/delete/', views.delete_volunteer, name='delete'),
]