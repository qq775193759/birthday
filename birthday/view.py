import json

from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse

from birthday.decorator import *

@method_required('GET')
def show_home(request):
    try:
        return render(request, 'home.html', {
            })
    except Exception as e:
        return show_message(request, 'Show home Error: ' + e.__str__())
        
@method_required('GET')
def show_surprise(request):
    try:
        surprise={'href':'#','name':'surprise'}
        prepare={'href':'#','name':'prepare'}
        exist={'href':'#','name':'exist'}
        lg_active=[surprise];
        lg=[prepare,exist];
        return render(request, 'surprise.html', {
        'left_group_active':lg_active,
        'left_group':lg,
            })
    except Exception as e:
        return show_message(request, 'Show home Error: ' + e.__str__())
        
@method_required('GET')
def show_enjoy(request):
    try:
        return render(request, 'enjoy.html', {
            })
    except Exception as e:
        return show_message(request, 'Show home Error: ' + e.__str__())