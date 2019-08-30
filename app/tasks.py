# -*- coding: utf-8 -*-

# Django Imports
from celery import task
from django.core.mail import send_mail
from django.conf import settings


@task
def celery_mail_generation(subject, message, receiver):
    """
    Task to send an e-mail notification using celery.
    """
    sender = settings.EMAIL_HOST_USER
    mail_sent = send_mail(subject, message, sender, [receiver])
    return mail_sent


def simple_mail_generation(subject, message, receiver):
    """
    Task to send an e-mail notification without celery .
    """
    sender = settings.EMAIL_HOST_USER
    mail_sent = send_mail(subject, message, sender, [receiver])
    return mail_sent

