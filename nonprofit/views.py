from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (Volunteer, VolunteerForm, EventForm, Event,
                     Skill, SkillForm, CategoryForm, Category, OrganizationForm,
                     Organization, Participation)


def index(request):
    return render(request, 'nonprofit/index.html')


def volunteer_home(request):
    volunteer_list = Volunteer.objects.all()
    skill_list = Skill.objects.all()
    return render(request, 'nonprofit/volunteer.html', {'volunteer_list': volunteer_list,
                                                        'skill_list': skill_list})


def event_home(request):
    event_list = Event.objects.all()
    category_list = Category.objects.all()
    organization_list = Organization.objects.all()
    return render(request, 'nonprofit/event.html', {'event_list': event_list,
                                                    'category_list': category_list,
                                                    'organization_list': organization_list})


def update_volunteer_details(request, pk):
    try:
        volunteer = Volunteer.objects.get(pk=pk)
        if request.method == 'POST':
            volunteer_form = VolunteerForm(request.POST, instance=volunteer)
            if volunteer_form.is_valid():
                volunteer_form.save()
                messages.success(request, "Successfully updated volunteer details!")
                return redirect('nonprofit:volunteer_home')
        else:
            volunteer_form = VolunteerForm(instance=volunteer)
        return render(request, 'nonprofit/volunteer.html', {'volunteer_form': volunteer_form})
    except Volunteer.DoesNotExist:
        messages.error(request, "Can't find this volunteer")


def insert_volunteer(request):
    if request.method == 'POST':
        volunteer_form = VolunteerForm(request.POST)
        if volunteer_form.is_valid():
            volunteer_form.save()
            messages.success(request, "Successfully insert volunteer!")
            return redirect('nonprofit:volunteer_home')
    else:
        volunteer_form = VolunteerForm()
    return render(request, 'nonprofit/volunteer.html', {'volunteer_form': volunteer_form})


def delete_volunteer(request, pk):
    volunteer = Volunteer.objects.get(pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('nonprofit:volunteer_home')


def insert_skill(request):
    if request.method == 'POST':
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_form.save()
            messages.success(request, "Successfully insert skill!")
            return redirect('nonprofit:volunteer_home')
    else:
        skill_form = SkillForm()
    return render(request, 'nonprofit/volunteer.html', {'skill_form': skill_form})


def insert_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Successfully insert category!")
            return redirect('nonprofit:event_home')
    else:
        category_form = SkillForm()
    return render(request, 'nonprofit/event.html', {'category_form': category_form})


def insert_organization(request):
    if request.method == 'POST':
        organization_form = OrganizationForm(request.POST)
        if organization_form.is_valid():
            organization_form.save()
            messages.success(request, "Successfully insert organization!")
            return redirect('nonprofit:event_home')
    else:
        organization_form = OrganizationForm()
    return render(request, 'nonprofit/event.html', {'organization_form': organization_form})


def update_event_details(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        if request.method == 'POST':
            event_form = EventForm(request.POST, instance=event)
            if event_form.is_valid():
                event_form.save()
                messages.success(request, "Successfully updated event details!")
                return redirect('nonprofit:event_home')
        else:
            event_form = EventForm(instance=event)
        return render(request, 'nonprofit/volunteer.html', {'event_form': event_form})
    except Event.DoesNotExist:
        messages.error(request, "Can't find this event")


def insert_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Successfully insert event!")
            return redirect('nonprofit:event_home')
    else:
        event_form = EventForm()
    return render(request, 'nonprofit/event.html', {'event_form': event_form})


def delete_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        if request.method == 'POST':
            event.delete()
            return redirect('nonprofit:event_home')
        return render(request, 'nonprofit/event.html')
    except Event.DoesNotExist:
        messages.error(request, "Can't find this event")


def filter_event_by_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        event_list = Event.objects.filter(category=category)
        return render(request, 'nonprofit:event.html', {'event_list': event_list})
    except Category.DoesNotExist:
        messages.error(request, "Can't find this category")


def filter_event_by_organization(request, pk):
    try:
        organization = Organization.objects.get(pk=pk)
        event_list = Event.objects.filter(organization=organization)
        return render(request, 'nonprofit:event.html', {'event_list': event_list})
    except Organization.DoesNotExist:
        messages.error(request, "Can't find this organization")


def filter_volunteer_by_skill(request, pk):
    try:
        skill = Skill.objects.get(pk=pk)
        volunteer_list = Volunteer.objects.filter(skills=skill)
        return render(request, 'nonprofit:volunteer.html', {'volunteer_list': volunteer_list})
    except Volunteer.DoesNotExist:
        messages.error(request, "Can't find this skill")
