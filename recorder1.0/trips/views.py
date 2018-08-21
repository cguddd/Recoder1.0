# trips/views.py

from datetime import datetime
#from flask import request
from django.shortcuts import render, redirect
from trips.forms import DocumentForm
from django.db import models
from trips.models import Document
from django.http import HttpResponse
from django.utils.html import escape
import datetime

def recorder(request):
    return render(request, 'recorder.html', {
    })
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/upload')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def upload(request):
    customHeader = request.META['HTTP_MYCUSTOMHEADER']


    time = "documents/" + datetime.datetime.now().strftime("%Y.%m.%d_%H:%M:%S.%f") + ".wav"
    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    uploadedFile = open(time, "wb")
    # the actual file is in request.body
    uploadedFile.write(request.body)
    uploadedFile.close()
    # put additional logic like creating a model instance or something like this here
    return HttpResponse(escape(repr(request)))