from django.shortcuts import render
from.models import *
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from .forms import ContactForm

# Create your views here.
def mai1(request):
    return render(request,"index.html")
def mai2(request):
    return render(request,"contact.html")
def mai3(request):
    bd=YourModelName.objects.all()
    return render(request,"news.html",context={"info":bd })
# views.py


from mainapp.forms import MessageForm
from mainapp.forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получение данных из формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка письма
            send_mail(
                subject=f'Сообщение от {name}',
                message=message,
                from_email=email,
                recipient_list=['kaktes4343@gmail.com'],  # Ваша Gmail-почта
            )
            return render(request, 'contact/success.html')  # Страница успеха
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
