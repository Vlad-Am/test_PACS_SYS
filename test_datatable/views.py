import datetime

from django.db import transaction
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin

from .forms import StudiesForm
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


class FormListView(FormMixin, ListView):
    """Подмешивание формы в ListView для возможности вывода
     на странице с листом формы по добавлению записей в БД"""

    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(u"Empty list and '%(class_name)s.allow_empty' is False."
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)


class StudiesListView(FormListView):
    model = Studies
    form_class = StudiesForm
    template_name = 'test_datatable/studies_list.html'
    success_url = reverse_lazy('test_datatable:studies_list')

    def post(self, request, *args, **kwargs):
        self.form = StudiesForm(request.POST)
        if self.form.is_valid():
            self.form.save()
        return super().get(request, *args, **kwargs)



