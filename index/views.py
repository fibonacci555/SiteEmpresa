from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        schedule_form = ScheduleForm(request.POST)
        services_list = Service.objects.all()
        
        if schedule_form.is_valid():
            new_schedule = schedule_form.save(commit=False)
            print('estev aqui 4')
            new_schedule.save()

        context = {
            'form' : schedule_form,
            'services' : services_list
        }
        return render(request, 'appointment.html', context)
