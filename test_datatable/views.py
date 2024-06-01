import datetime

from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Modalities, Studies
import random
from datetime import timedelta
import uuid


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def init_db(request):
    """
    База предоставляется уже предзаполненной, но в случае желания перехода
    на другую СУБД, можно раскомментировать код ниже и сгенерировать тестовые данные.
    """

    # Modalities.objects.all().delete()
    # modalities = [['CT', 'Computed Tomography'],
    #               ['MR', 'Magnetic Resonance'],
    #               ['PT', 'Positron emission tomography'],
    #               ['US', 'Ultrasound'],
    #               ['XA', 'X-Ray Angiography'],
    #               ['MG', 'Mammography'],
    #               ['CR', 'Computed Radiography'],
    #               ['AS', 'Angioscopy'],
    #               ['DX', 'Digital Radiography'],
    #               ['EC', 'Echocardiography']]
    # for modality in modalities:
    #     modality_obj = Modalities()
    #     modality_obj.short_code = modality[0]
    #     modality_obj.name = modality[1]
    #     modality_obj.save()
    # for i in range(100000):
    #     study_obj = Studies()
    #     study_obj.patient_fio = names.get_full_name()
    #     study_obj.patient_birthdate = random_date(datetime.datetime(2000, 1, 1, 0, 0, 0),
    #                                               datetime.datetime(2023, 1, 1, 0, 0, 0))
    #     study_obj.study_date = random_date(datetime.datetime(2023, 1, 1, 0, 0, 0),
    #                                        datetime.datetime(2023, 9, 1, 0, 0, 0))
    #     study_obj.study_uid = uuid.uuid4()
    #     random_modality_id = random.randint(1, 10)
    #     study_obj.study_modality = Modalities.objects.get(id=int(random_modality_id))
    #     study_obj.save()
    return render(request, 'test_datatable/init_db.html')


class StudiesCreateView(CreateView):
    model = Studies
    # form_class = StudiesForm
    success_url = reverse_lazy('test_datatable:table_create')


class StudiesListView(ListView):
    model = Studies

    # form_class = StudiesForm

    @transaction.atomic
    def get_queryset(self):
        return Studies.objects.all()
