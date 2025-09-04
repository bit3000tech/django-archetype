"""
Public app views
"""
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def home(request):
    """Home page view"""
    return render(request, 'public/home.html')


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real application, you would send an email or save to database
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            form = ContactForm()  # Clear the form
    else:
        form = ContactForm()
    
    return render(request, 'public/contact.html', {'form': form})
