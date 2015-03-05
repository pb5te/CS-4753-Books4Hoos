from django.shortcuts import render


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
 
def start(request):
    return render(request, 'home/default.html')


