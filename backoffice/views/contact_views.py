from django.shortcuts import render
from backoffice.models import Contact

def index(request):
    contacts = Contact.objects.filter(status=True).order_by('first_name')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'backoffice/index.html',
        context
    )