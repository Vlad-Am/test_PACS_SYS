from django.contrib import admin

from test_datatable.models import Modalities, Studies


@admin.register(Modalities)
class ModalitiesAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'name')


@admin.register(Studies)
class StudiesAdmin(admin.ModelAdmin):
    list_display = ('patient_fio', 'patient_birthdate', 'study_uid', 'study_date', 'study_modality')
    ordering = ('patient_fio', 'patient_birthdate', 'study_uid', 'study_date', 'study_modality')
    search_fields = ('patient_fio', 'patient_birthdate', 'study_uid', 'study_date', 'study_modality')
