from django.urls import path
from . import views
from .views import StudiesListView, StudiesCreateView

urlpatterns = [
    path('init_db/', views.init_db, name='init_db'),
    path("table_list/", StudiesListView.as_view(), name="table_list"),
    path("table_create/", StudiesCreateView.as_view(), name="table_create"),
]
