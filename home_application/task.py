from __future__ import absolute_import, unicode_literals

from celery import shared_task # it is adecoratoer
from time import sleep
from django.shortcuts import render,HttpResponse,redirect


@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task()
def cal():
    print('cal')
    return True