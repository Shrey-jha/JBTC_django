from django.shortcuts import render, redirect
from .models import LoadInfo
from .forms import LoadInfoForm, FeedbackForm

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, GetQuoteForm


def home(request):
    return render(request, 'transport/home.html')

def about(request):
    return render(request, 'transport/about.html')

def contact(request):
    return render(request, 'transport/contact.html')

def load_form(request):
    if request.method == "POST":
        form = LoadInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'transport/thank_you.html')
    else:
        form = LoadInfoForm()
    return render(request, 'transport/load_form.html', {'form': form})




def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def feedback_thanks_view(request):
    return render(request, 'feedback/feedback_thanks.html')





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email (optional)
            send_mail(
                f"New Contact Form Submission from {name}",
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )

            # Redirect to a 'thank you' page or show a success message
            return redirect('contact_thanks')
    else:
        form = ContactForm()

    return render(request, 'transport/contact.html', {'form': form})



def home(request):
    if request.method == 'POST':
        form = GetQuoteForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            details = form.cleaned_data['details']

            # Send an email (optional)
            send_mail(
                f"New Quote Request from {name}",
                f"Details: {details}\nPhone: {phone}\nEmail: {email}",
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )

            # Redirect to a 'thank you' page or show a success message
            return redirect('quote_thanks')
    else:
        form = GetQuoteForm()

    return render(request, 'transport/home.html', {'form': form})

def quote_thanks(request):
    return render(request, 'transport/quote_thanks.html')