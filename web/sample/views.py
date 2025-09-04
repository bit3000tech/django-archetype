"""
Sample app views
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from project.sample.models import Person
from .forms import PersonForm


def person_list(request):
    """List all people"""
    people = Person.objects.all()
    return render(request, 'sample/person_list.html', {'people': people})


def person_detail(request, pk):
    """Display a single person's details"""
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'sample/person_detail.html', {'person': person})


def person_create(request):
    """Create a new person"""
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            messages.success(request, f'Person "{person.full_name}" was created successfully.')
            return redirect('sample:person_detail', pk=person.pk)
    else:
        form = PersonForm()
    
    return render(request, 'sample/person_form.html', {'form': form})


def person_update(request, pk):
    """Update an existing person"""
    person = get_object_or_404(Person, pk=pk)
    
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save()
            messages.success(request, f'Person "{person.full_name}" was updated successfully.')
            return redirect('sample:person_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    
    return render(request, 'sample/person_form.html', {'form': form, 'person': person})


def person_delete(request, pk):
    """Delete a person"""
    person = get_object_or_404(Person, pk=pk)
    
    if request.method == 'POST':
        name = person.full_name
        person.delete()
        messages.success(request, f'Person "{name}" was deleted successfully.')
        return redirect('sample:person_list')
    
    return render(request, 'sample/person_confirm_delete.html', {'person': person})
