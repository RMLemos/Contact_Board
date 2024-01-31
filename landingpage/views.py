from django.shortcuts import render, redirect
from landingpage.forms import EbookForm

def home(request):
    if request.method == 'POST':
        form = EbookForm(request.POST)
        if form.is_valid():
            form.save()
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