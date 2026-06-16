from django.urls import path

from .views import (
    ad_list,
    ad_detail,
    ad_create,
    ad_edit,
    ad_delete,
    my_ads,
    toggle_ad,
)

urlpatterns = [

    path(
        '',
        ad_list,
        name='ad_list'
    ),

    path(
        'ad/<int:pk>/',
        ad_detail,
        name='ad_detail'
    ),

    path(
        'create/',
        ad_create,
        name='ad_create'
    ),

    path(
        'ad/<int:pk>/edit/',
        ad_edit,
        name='ad_edit'
    ),

    path(
        'ad/<int:pk>/delete/',
        ad_delete,
        name='ad_delete'
    ),

    path(
        'ad/<int:pk>/toggle/', 
        toggle_ad, 
        name='toggle_ad'
    ),
]