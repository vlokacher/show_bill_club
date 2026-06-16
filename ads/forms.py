from django import forms

from .models import Ad, Response


class AdForm(forms.ModelForm):

    class Meta:

        model = Ad

        fields = (
            'title',
            'description',
            'price',
            'category',
            'image',
            'is_active',
        )

        labels = {

            'title': 'Название',

            'description': 'Описание',

            'price': 'Цена',

            'category': 'Категория',

            'image': 'Изображение',

            'is_active': 'Активно',
        }

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
                'rows': 6,
                'style': 'resize:none;'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'checkbox-input'
            }),
        }

class ResponseForm(forms.ModelForm):

    class Meta:

        model = Response

        fields = ('text',)

        labels = {
            'text': ''
        }

        widgets = {

            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите сообщение...',
                'rows': 4,
                'style': 'resize:none;'
            })

        }