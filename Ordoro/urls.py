from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from orderapi import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^api/orders/$', views.orderList, name='orders'),
    url(r'^api/orders/(?P<pk>.+)/$', views.orderDetailed, name='orderDetailed'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
