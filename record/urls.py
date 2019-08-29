from django.urls import path
from .views import RecordListView, RecordDetailView, RecordCreateView
from . import views



urlpatterns = [

    path('', RecordListView.as_view(), name ='record-home'),

    path('record/<int:pk>/', RecordDetailView.as_view(), name='record-detail'),
    path('record/new/<int:pk>/', RecordCreateView.as_view(), name='record-create'),

    path('about/', views.about, name ='record-about'),
]
