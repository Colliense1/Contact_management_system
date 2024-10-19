
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm, ContactSearchForm
import random
from collections import OrderedDict
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages


def contact_list(request):

    query = request.GET.get('query', '')  # Get the search query from the request
    contacts = Contact.objects.all()

    # Filter contacts based on the search query
    if query:
        contacts = contacts.filter(first_name__istartswith=query)  # Filter by first letter (case insensitive)

    contacts = contacts.order_by('first_name')  # Order contacts by first name

    grouped_contacts = {}  # Initialize an empty dictionary to store grouped contacts

    for contact in contacts:
        first_letter = contact.first_name[0].upper()  # Get the first letter of the contact's name
        if first_letter not in grouped_contacts:
            grouped_contacts[first_letter] = []  # Initialize a new list for the first letter
        grouped_contacts[first_letter].append(contact)  # Add the contact to the list

    grouped_contacts = {letter: contacts for letter, contacts in grouped_contacts.items() if contacts}  # Filter out empty lists

    grouped_contacts = OrderedDict(sorted(grouped_contacts.items()))  # Sort the dictionary by letter keys

    return render(request, 'contact_list.html', {
        'contacts': contacts,
        'grouped_contacts': grouped_contacts,
        'query': query,  # Pass the query back to the template
    })


def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contact_detail.html', {'contact': contact})


def contact_add(request):

    header_title = "CMS | Create Contact"
    title = "Create contact"          # Set the title for the create contact form
    button = "Save"
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.color = contact.initial_color()
            contact.save()

            # Get the first letter of the contact's name
            first_letter = contact.first_name[0].upper()  
            # Redirect to contact list filtered by the first letter
            return redirect(f"{reverse('contact_list')}?q={first_letter}") 
        
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form, 'title': title, 'button': button, 'header_title': header_title})


def contact_edit(request, id):
    if id:
        contact = get_object_or_404(Contact, id=id)
        header_title = "CMS | Update Contact"
        title = "Update Contact"
        button = "Update"
    else:
        contact = None
        header_title = "CMS | Create Contact"
        title = "Create Contact"
        button = "Save"
        

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.has_changed():
            if form.is_valid():
                form.save()
                return redirect('contact_list')
        else:
            # Form is invalid, display error message
            messages.error(request, 'You didn\'t updated any data.')
            messages.error(request, 'If you don\'t want to update any data, you can click on the cross sign')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form, 'title': title, 'button': button, 'header_title': header_title})


def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})

