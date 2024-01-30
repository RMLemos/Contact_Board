from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from backoffice.forms import RegisterForm, RegisterUpdateForm

@login_required(login_url=('backoffice:login'))
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('backoffice:login')


    return render(
        request,
        'backoffice/register.html',
        {
            'form': form
        }
    )

@login_required(login_url=('backoffice:login'))
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'backoffice/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'backoffice/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('backoffice:index')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('backoffice:index')

    return render(
        request,
        'backoffice/login.html',
        {
            'form': form
        }
    )


@login_required(login_url=('backoffice:login'))
def logout_view(request):
    auth.logout(request)
    return redirect('backoffice:login')