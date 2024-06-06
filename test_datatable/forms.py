import datetime

from django import forms
from django.contrib.admin import widgets

from test_datatable.models import Studies


class StudiesForm(forms.ModelForm):
    patient_birthdate = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date',
                   'class': 'form-control',
                   'placeholder': 'дд.мм.гггг'},
        ),
    )

    study_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local',
                   'class': 'form-control',
                   'placeholder': 'дд.мм.гггг чч:мм:сс'},
        ),
    )

    class Meta:
        model = Studies
        fields = ("patient_fio", "patient_birthdate", "study_uid", "study_date", "study_modality")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# def patient_birthdate_view(self):
#      """Делает поле даты рождения удобным для выбора"""
#      self.fields['patient_birthdate'].widget = forms.DateInput(attrs={'type': 'date',
#                                                                       'class': 'form-control',
#                                                                       'placeholder': 'дд.мм.гггг'
#                                                                       })
