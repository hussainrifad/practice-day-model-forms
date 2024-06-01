from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms

def home(request):
    return redirect('formpage')

def form(request):
    form = forms.PersonalForm(request.POST)
    if(request.method == 'POST'):
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'form.html', {'form' : form})
    else:
        form = forms.PersonalForm()
        return render(request, 'form.html', {'form' : form})

def artist(request):
    form = forms.Artist(request.POST)
    if(request.method == 'POST'):
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('homepage')
            return render(request, 'artist.html', {'form' : form})
    else:
        form = forms.Artist()
        return render(request, 'artist.html', {'form' : form})