from django.db import models
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default=None)
    location = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name


class Participation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    hours_contributed = models.IntegerField()

    def __str__(self):
        return f"{self.volunteer} participated in {self.event}"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "date", "location", "category"]


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }
