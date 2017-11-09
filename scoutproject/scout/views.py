# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('scout/index.html')
    context = {
        'hello': "hello scout",
    }
    return HttpResponse(template.render(context, request))
