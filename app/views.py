"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
#necessary imports
from .forms import UrlForm
from .models import Url
from django.shortcuts import get_object_or_404, redirect

def home(request):
    """Renders the home page."""
    if request.method == "POST":
        form = UrlForm(request.POST)
        #UrlForm returns a url object
        if form.is_valid():#form 
            form.save()
            return redirect('app.views.home')
    else:
        form = UrlForm()
        urls = Url.objects.filter(created_date__isnull=False).order_by('created_date').reverse()
    return render(
        request,
        'app/index.html',
        {
            'form':form,
            'urls':urls,
            'curr_host_red':request.get_host()+"/red/",
        }
    )
def red(request,pk):
    """Performs the redirect of shortened link"""
    assert isinstance(request, HttpRequest)
    full_link = Url.objects.get(id=pk).link
    if full_link[0:8] != r'http://':
        full_link = r'http://'+full_link
    return redirect(full_link)

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Contact me.',
            'email':'rallapalli.harish@gmail.com',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'A simple URL shortening service.',
            'year':datetime.now().year,
        })
    )
