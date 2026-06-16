from django.urls import path

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from .views import (
    register_view,
    profile,
)

from .forms import LoginForm


urlpatterns = [

    path(
        'register/',
        register_view,
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
            authentication_form=LoginForm
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(
            next_page='/'
        ),
        name='logout'
    ),

    path(
        'profile/',
        profile,
        name='profile'
    ),
]