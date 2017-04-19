from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^visualize/',views.visualize, name='index'),
    url(r'^report/(?P<report_id>\d+)',views.report, name='report'),
    url(r'^fare_time_calculator',views.faretime, name='report'),
]
