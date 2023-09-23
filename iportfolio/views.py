from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from .models import Contact

def home (request):
    if request.method == 'POST':
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name is not None and email is not None and subject is not None and message is not None:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            return HttpResponse('Message Successfully Sent', status=200)

    return render(request, 'index.html')