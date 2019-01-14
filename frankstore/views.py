# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def searchme(request):
    return render(request, 'searchme.html')