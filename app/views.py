# -*- coding: utf-8 -*-

# Django Imports
from django.shortcuts import render, redirect

# Project Imports
from .tasks import celery_mail_generation, simple_mail_generation
from .forms import MessageForm


def home(request):
    """
    Home Page View.
    """
    return render(request, 'home.html')


def mail_using_celery(request):
    """
    Method to Send Email Using Celery.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['receiver']
            celery_mail_generation.delay(subject, message, receiver)
            return redirect('home')
    else:
        form = MessageForm()
        return render(request, 'message.html', {'form': form})


def mail_without_celery(request):
    """
    Method to send email without Celery.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['receiver']
            simple_mail_generation(subject, message, receiver)
            return redirect('home')
    else:
        form = MessageForm()
        return render(request, 'message.html', {'form': form})

