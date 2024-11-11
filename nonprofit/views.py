from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from .models import Volunteer, VolunteerForm, EventForm, Event


def index(request):
    return render(request, 'nonprofit/index.html')


def volunteer_home(request):
    volunteer_list = Volunteer.objects.all()
    return render(request, 'nonprofit/volunteer.html', {'volunteer_list': volunteer_list})


def event_home(request):
    event_list = Event.objects.all()
    return render(request, 'nonprofit/event.html', {'event_list': event_list})


class UpdateVolunteerDetail(UpdateView):
    model = Volunteer
    template_name = "nonprofit/update.html"
    form_class = VolunteerForm
    success_url = reverse_lazy('nonprofit:volunteer_home')


class InsertVolunteer(CreateView):
    model = Volunteer
    template_name = "nonprofit/insert.html"
    form_class = VolunteerForm
    success_url = reverse_lazy('nonprofit:volunteer_home')


def delete_volunteer(request, pk):
    volunteer = Volunteer.objects.get(pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('nonprofit:volunteer_home')
