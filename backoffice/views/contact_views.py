from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from backoffice.models import Contact

def index(request):
    contacts = Contact.objects.filter(status=True).order_by('first_name')

    context = {
        'contacts': contacts,
        'site_title': 'Contact Board'
    }

    return render(
        request,
        'backoffice/index.html',
        context
    )


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

    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request,
        'backoffice/index.html',
        context
    )



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