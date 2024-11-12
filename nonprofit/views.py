from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView, CreateView
from .models import (Volunteer, VolunteerForm, EventForm, Event,
                     Skill, SkillForm, CategoryForm, Category, OrganizationForm, Organization)


def index(request):
    return render(request, 'nonprofit/index.html')


def volunteer_home(request):
    print("mi")
    volunteer_list = Volunteer.objects.all()
    return render(request, 'nonprofit/volunteer.html', {'volunteer_list': volunteer_list})


def event_home(request):
    event_list = Event.objects.all()
    event_form = EventForm
    organization_form = OrganizationForm
    category_form = CategoryForm
    return render(request, 'nonprofit/event.html', {'event_list': event_list,
                                                    'organization_form': organization_form,
                                                    'category_form': category_form,
                                                    'event_form': event_form})


# class UpdateVolunteerDetail(UpdateView):
#     model = Volunteer
#     form_class = VolunteerForm(instance=model)
#     template_name = "nonprofit/volunteer.html"
#     success_url = reverse_lazy('nonprofit:volunteer_home')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         # Ensure the form is populated with the correct instance
#         kwargs['instance'] = self.get_object()  # This gets the specific volunteer instance for the update view
#         return kwargs


def update_volunteer_details(request, pk):
    print("mim")
    try:
        volunteer = Volunteer.objects.get(pk=pk)
        if request.method == 'POST':
            volunteer_form = VolunteerForm(request.POST, instance=volunteer)
            if volunteer_form.is_valid():
                volunteer_form.save()
                messages.success(request, "Successfully update volunteer details!")
                return redirect('nonprofit:volunteer_home')
        else:
            volunteer_form = VolunteerForm(instance=volunteer)
    except Volunteer.DoesNotExist:
        messages.error(request, "Volunteer not found.")
        return redirect('nonprofit:volunteer_home')
    return render(request, 'nonprofit/volunteer.html', {'volunteer_form': volunteer_form})


class InsertVolunteer(CreateView):
    print("ooo")
    model = Volunteer
    template_name = "nonprofit/volunteer.html"
    form_class = VolunteerForm
    success_url = reverse_lazy('nonprofit:volunteer_home')


def delete_volunteer(request, pk):
    volunteer = Volunteer.objects.get(pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('nonprofit:volunteer_home')


class InsertSkill(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = "nonprofit/volunteer.html"
    success_url = reverse_lazy('nonprofit:volunteer_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class InsertCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "nonprofit/event.html"
    success_url = reverse_lazy('nonprofit:event_home')


class InsertOrganization(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "nonprofit/event.html"
    success_url = reverse_lazy('nonprofit:event_home')


class UpdateEventDetail(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "nonprofit/event.html"
    success_url = reverse_lazy('nonprofit:event_home')


class InsertEvent(CreateView):
    model = Event
    form_class = EventForm
    template_name = "nonprofit/event.html"
    success_url = reverse_lazy('nonprofit:event_home')
