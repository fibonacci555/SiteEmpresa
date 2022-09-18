from django.shortcuts import render
from django.views import View
from .forms import * 






# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)

            new_contact.save()

            

        context = {
            'form' : contact_form,
            
        }
        return render(request, 'index.html', context)
