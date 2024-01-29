from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from backoffice.forms import ContactForm
from backoffice.models import Contact


def create(request):
    form_action = reverse('backoffice:create')
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('backoffice:index')

        return render(
            request,
            'backoffice/create.html',
            context
        )
    
    context = {
            'form': ContactForm(),
            'form_action': form_action,
        }
    
    return render(
            request,
            'backoffice/create.html',
            context
        )


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, status=True)
    form_action = reverse('backoffice:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            return redirect('backoffice:index')

        return render(
            request,
            'backoffice/create.html',
            context
        )
    
    context = {
            'form': ContactForm(instance=contact),
            'form_action': form_action,
        }
    
    return render(
            request,
            'backoffice/create.html',
            context
        )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('backoffice:index')

    return render(
        request,
        'backoffice/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
