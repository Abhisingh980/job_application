from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request == 'POST':
        forms = ApplicationForm()
        if forms.is_valid():
            first_name = forms.cleaned_data["first_name"]
            last_name = forms.cleaned_data["last_name"]
            email = forms.cleaned_data["email"]
            date = forms.cleaned_data["data"]
            occupation = forms.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            messages_body = f"Thanks for submitting  {first_name}."
            email_message = EmailMessage("From submission confirmation", messages_body,
                                         to=[email])
            email_message.send()
            messages.success(request, "Forms submitted successfully!")
    return render(request, "index.html")
