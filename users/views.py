from django.shortcuts import (
    render,
    redirect
)

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm

@login_required
def profile(request):

    ads = request.user.ads.all()

    return render(
        request,
        'users/profile.html',
        {
            'ads': ads
        }
    )

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Регистрация прошла успешно'
            )

            return redirect('/')

    else:

        form = RegisterForm()

    return render(
        request,
        'users/register.html',
        {'form': form}
    )