from django.shortcuts import render, redirect
from landingpage.forms import EbookForm
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        form = EbookForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
            )
            return redirect('landingpage:sent')
    else:
        form = EbookForm()
    return render(request, 'landingpage/home.html', {'form': form})

def sent_ebook(request):
    return render(
        request,
        'landingpage/sent.html',
    )

def terms(request):
    return render(
        request,
        'landingpage/terms.html',
    )