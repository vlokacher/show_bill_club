from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Ad, Category, Response
from .forms import AdForm, ResponseForm


def ad_list(request):

    ads = Ad.objects.filter(
        is_active=True
    ).order_by('-created_at')

    query = request.GET.get('q')

    category_id = request.GET.get('category')

    if query:

        ads = ads.filter(

            Q(title__icontains=query) |
            Q(description__icontains=query)

        )
        
    if category_id:

        ads = ads.filter(
            category_id=category_id
        )

    categories = Category.objects.all()

    return render(
        request,
        'ads/ad_list.html',
        {
            'ads': ads,
            'categories': categories,
        }
    )

def ad_detail(request, pk):

    ad = get_object_or_404(
        Ad,
        pk=pk
    )

    responses = None

    if request.user == ad.author:

        responses = ad.responses.all().order_by(
            '-created_at'
        )

    if request.method == 'POST':

        if not request.user.is_authenticated:

            return redirect('login')

        if request.user == ad.author:

            messages.error(
                request,
                'Нельзя откликаться на своё объявление'
            )

            return redirect(
                'ad_detail',
                pk=ad.pk
            )

        form = ResponseForm(request.POST)

        if form.is_valid():

            response = form.save(commit=False)

            response.ad = ad

            response.author = request.user

            response.save()

            messages.success(
                request,
                'Отклик отправлен'
            )

            return redirect(
                'ad_detail',
                pk=ad.pk
            )

    else:

        form = ResponseForm()

    return render(
        request,
        'ads/ad_detail.html',
        {
            'ad': ad,
            'form': form,
            'responses': responses,
        }
    )

@login_required
def ad_create(request):

    if request.method == 'POST':

        form = AdForm(request.POST, request.FILES)

        if form.is_valid():

            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()

            messages.success(request, 'Объявление создано')

            return redirect('ad_detail', pk=ad.pk)

    else:
        form = AdForm()

    return render(
        request,
        'ads/ad_form.html',
        {'form': form}
    )

@login_required
def ad_edit(request, pk):

    ad = get_object_or_404(Ad, pk=pk)

    if ad.author != request.user:
        return redirect('ad_list')

    if request.method == 'POST':

        form = AdForm(request.POST, request.FILES, instance=ad)

        if form.is_valid():
            form.save()
            messages.success(request, 'Объявление обновлено')
            return redirect('ad_detail', pk=ad.pk)

    else:
        form = AdForm(instance=ad)

    return render(
        request,
        'ads/ad_form.html',
        {'form': form}
    )

@login_required
def ad_delete(request, pk):

    ad = get_object_or_404(Ad, pk=pk)

    if ad.author != request.user:
        return redirect('ad_list')

    if request.method == 'POST':
        ad.delete()
        messages.success(request, 'Объявление удалено')
        return redirect('ad_list')

    return render(
        request,
        'ads/ad_delete.html',
        {'ad': ad}
    )

@login_required
def my_ads(request):

    ads = Ad.objects.filter(
        author=request.user
    ).order_by('-created_at')

    return render(
        request,
        'ads/my_ads.html',
        {'ads': ads}
    )

@login_required
def toggle_ad(request, pk):

    ad = get_object_or_404(
        Ad,
        pk=pk,
        author=request.user
    )

    ad.is_active = not ad.is_active

    ad.save()

    return redirect('profile')