from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import ContactForm

def index(request):
    if request.method == 'POST':
#        print 'post'
        form = ContactForm(request.POST)
        
        if form.is_valid():
#enter code here to process submitted forms
            print 'success!\n'
            return HttpResponse('Dear {}, Your message has been successfully submitted!\n, below is your message text:\n{}'.format(form.cleaned_data['guest_name'],form.cleaned_data['context']))
    else:
#            print 'not post\n'
        form = ContactForm()
    return render(request,'contacts.html',{'form':form})
