import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Max, Min, Avg, Count
from django.db.models.functions import TruncMonth
from .models import (Volunteer, VolunteerForm, EventForm, Event,
                     Skill, SkillForm, CategoryForm, Category, OrganizationForm,
                     Organization, Participation, ParticipationForm)


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
        return render(request, 'nonprofit/event.html')


def participation_home(request):
    participation_list = Participation.objects.all()
    volunteer_list = Volunteer.objects.all()
    event_list = Event.objects.all()
    return render(request, 'nonprofit/participation.html',
                  {'participation_list': participation_list,
                   'volunteer_list': volunteer_list, 'event_list': event_list})


def insert_participation(request):
    if request.method == 'POST':
        participation_form = ParticipationForm(request.POST)
        if participation_form.is_valid():
            participation_form.save()
            messages.success(request, "Successfully insert participation!")
            return redirect('nonprofit:participation_home')
    else:
        participation_form = ParticipationForm()
    return render(request, 'nonprofit/participation.html', {'participation_form': participation_form})


def update_participation_details(request, pk):
    try:
        participation = Participation.objects.get(pk=pk)
        if request.method == 'POST':
            participation_form = ParticipationForm(request.POST, instance=participation)
            if participation_form.is_valid():
                participation_form.save()
                messages.success(request, "Successfully updated participation details!")
                return redirect('nonprofit:participation_home')
        else:
            participation_form = EventForm(instance=participation)
        return render(request, 'nonprofit/participation.html', {'participation_form': participation_form})
    except Participation.DoesNotExist:
        messages.error(request, "Can't find this participation")


def delete_participation(request, pk):
    try:
        participation = Participation.objects.get(pk=pk)
        if request.method == 'POST':
            participation.delete()
            return redirect('nonprofit:participation_home')
        return render(request, 'nonprofit/participation.html')
    except Participation.DoesNotExist:
        messages.error(request, "Can't find this participation")
        return render(request, 'nonprofit/participation.html')


def insight_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        max_hours = Participation.objects.filter(event=event
                                                 ).aggregate(Max('hours_contributed'))['hours_contributed__max']
        min_hours = Participation.objects.filter(event=event
                                                 ).aggregate(Min('hours_contributed'))['hours_contributed__min']
        avg_hours = Participation.objects.filter(event=event
                                                 ).aggregate(Avg('hours_contributed'))['hours_contributed__avg']
        max_hours_list = Participation.objects.filter(event=event, hours_contributed=max_hours)
        min_hours_list = Participation.objects.filter(event=event, hours_contributed=min_hours)
        return render(request, 'nonprofit/insight_event.html',
                      {'max_hours_list': max_hours_list, 'min_hours_list': min_hours_list,
                       'avg_hours': avg_hours})
    except Event.DoesNotExist:
        messages.error(request, "Can't find this event")
        return render(request, 'nonprofit/insight_event.html')


def statistic_dashboard(request):
    event_per_month = Event.objects.annotate(month=TruncMonth('date')
                                             ).values('month').annotate(event_count=Count('id')).order_by('month')

    event_per_month_list = [
        {'month': item['month'].strftime('%Y-%m'),
         'event_count': item['event_count']
         } for item in event_per_month
    ]
    event_per_month_json = json.dumps(event_per_month_list)

    skill_counts = Skill.objects.annotate(volunteer_count=Count('volunteer')).all()
    skill_counts_list = [
        {'skill': skill.name,
         'volunteer_count': skill.volunteer_count
         } for skill in skill_counts
    ]
    skill_counts_json = json.dumps(skill_counts_list)

    category_counts = Category.objects.annotate(event_count=Count('event')).all()
    category_counts_list = [
        {'category': category.name,
         'event_count': category.event_count
         } for category in category_counts
    ]
    category_counts_json = json.dumps(category_counts_list)
    return render(request, 'nonprofit/statistic.html', {'event_per_month': event_per_month_json,
                                                        'skill_counts': skill_counts_json,
                                                        'category_counts': category_counts_json})
