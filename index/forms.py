from django import forms
from django.forms import ModelForm
from .models import Comment, Beauty, Wedding, Fashion, Birthday, Event


class Komment(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']

class BeautyAdd(ModelForm):
    class Meta:
        model = Beauty
        fields = '__all__'

class WeddingAdd(ModelForm):
    class Meta:
        model = Wedding
        fields = '__all__'

class FashionAdd(ModelForm):
    class Meta:
        model = Fashion
        fields = '__all__'

class BirthdayAdd(ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'

class EventAdd(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

