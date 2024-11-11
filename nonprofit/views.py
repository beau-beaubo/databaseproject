from django.shortcuts import render
from django.http import HttpResponse
from .models import Volunteer


def index(request):
    volunteers = Volunteer.objects.all()

    response_content = ""
    for volunteer in volunteers:
        skills_list = ", ".join([skill.name for skill in volunteer.skills.all()])
        response_content += f"{volunteer.name} - Skills: {skills_list}<br>"

    return HttpResponse(response_content)
