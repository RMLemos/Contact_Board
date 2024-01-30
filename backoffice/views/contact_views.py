from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.db.models import Q
from backoffice.models import Contact


@login_required(login_url=('backoffice:login'))
def index(request):
    contacts = Contact.objects.filter(status=True).order_by('first_name')

    paginator = Paginator(contacts, 15)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contact Board'
    }

    return render(
        request,
        'backoffice/index.html',
        context
    )


@login_required(login_url=('backoffice:login'))
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('backoffice:index')

    contacts = Contact.objects \
        .filter(status=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('first_name')
    
    paginator = Paginator(contacts, 15)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - '
    }

    return render(
        request,
        'backoffice/index.html',
        context
    )


@login_required(login_url=('backoffice:login'))
def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, status=True)

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'backoffice/contact.html',
        context
    )