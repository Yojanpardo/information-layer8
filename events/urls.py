from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^event/$', views.EventList.as_view(), name='home'),
	url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetail.as_view(),
		name='detail'),
	url(r'^event/new$', views.EventCreate.as_view(), name='new'),
	url(r'^event/edit/(?P<pk>[0-9]+)/$',
		views.EventUpdate.as_view(), name='edit'),
    url(r'^event/delete/(?P<pk>[0-9]+)/$',
    	views.EventDelete.as_view(), name='delete'),
]
