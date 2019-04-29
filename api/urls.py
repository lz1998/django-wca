from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'queryId',views.queryId),
    url(r'^ranksAverage', views.ranksAverage),
    url(r'^ranksSingle', views.ranksSingle),
    # url...
]