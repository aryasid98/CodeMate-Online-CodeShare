from django.conf.urls import url
from django.urls import path
from create import views

app_name='create'

urlpatterns=[
    url(r'^$', views.IndexView.as_view(), name="index"),

    url('paste/', views.CodeCreate.as_view(), name="detail"),

    path('result/<slug:slug>', views.result, name="result"),

    url('addObject/', views.addObject, name='addObject'),

    path('result/<slug:slug>/modify/', views.modify, name='modify'),

    path('result/<slug:slug>/delete/', views.DeleteObject.as_view(), name='delete'),
]