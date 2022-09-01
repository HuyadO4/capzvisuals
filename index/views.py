from django.shortcuts import render, redirect
from django.http import Http404
from . import templates
from django.template import loader
from .forms import Komment, BeautyAdd, BirthdayAdd, EventAdd, FashionAdd, WeddingAdd
from .models import Comment
from .models import Beauty
from .models import Birthday
from .models import Event
from .models import Fashion
from .models import Wedding

def index(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'capzvisuals/index.html', context)

def services(request):
    birth = Birthday.objects.all()
    fash = Fashion.objects.all()
    vent = Event.objects.all()
    wed = Wedding.objects.all()
    pretty = Beauty.objects.all()
    context = {'pretty' : pretty, 'wed':wed, 'vent':vent, 'fash':fash, 'birth':birth}
    return render(request, 'capzvisuals/services.html', context)

def about(request):
    return render(request, 'capzvisuals/about.html')

def main(request):
    return render(request, 'main.html')

def contact(request):
    return render(request, 'capzvisuals/contact.html')

def birthday(request):
    birth = Birthday.objects.all()
    context = {'birth' : birth}
    return render(request, 'capzvisuals/birthday.html', context)

#def beauty(request):
#    beauty = Beauty.ob
#    context = {'beauty' : beauty}
#    return render(request, 'capzvisuals/birthday.html', context)

def wedding(request):
    wed = Wedding.objects.all()
    context = {'wed' : wed}
    return render(request, 'capzvisuals/wedding.html', context)

def event(request):
    vent = Event.objects.all()
    context = {'vent' : vent}
    return render(request, 'capzvisuals/event.html', context)

def fashion(request):
    fash = Fashion.objects.all()
    context = {'fash' : fash}
    return render(request, 'capzvisuals/fashion.html', context)

def beautiful(request):
    pretty = Beauty.objects.all()
    context = {'pretty' : pretty}
    return render(request, 'capzvisuals/beautiful.html', context)
    

def testimony(request):
    comments = Komment()
    if request.method == 'POST':
        comments = Komment(request.POST, request.FILES)
        if comments.is_valid():
            comments.save()
            return redirect('index')

    context = {'comments': comments}
    return render(request, 'capzvisuals/testimony.html', context)

def subadmin(request):
    birth = BirthdayAdd()
    if request.method == 'POST':
        birth = BIrthdayAdd(request.POST)
        if birth.is_valid():
            birth.save()
            return redirect('index')
    vent = EventAdd()
    if request.method == 'POST':
        vent = EventAdd(request.POST)
        if vent.is_valid():
            vent.save()
            return redirect('index')
    fash = FashionAdd()
    if request.method == 'POST':
        fash = FashionAdd(request.POST)
        if fash.is_valid():
            fash.save()
            return redirect('index')
    wed = WeddingAdd()
    if request.method == 'POST':
        wed = WeddingAdd(request.POST)
        if wed.is_valid():
            wed.save()
            return redirect('index')
    fine = BeautyAdd()
    if request.method == 'POST':
        fine = BeautyAdd(request.POST)
        if fine.is_valid():
            fine.save()
            return redirect('index')
    context = {'fine' : fine, 'wed' : wed, 'fash':fash, 'vent':vent, 'birth':birth}
    return render(request, 'capzvisuals/subadmin.html', context)
