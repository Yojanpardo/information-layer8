from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^member/$', views.MemberList.as_view(), name='member'),
	url(r'^member/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view(),
		name='detail'),
	# url(r'^member/new$', views.MemberCreate.as_view(), name='new'),
	# url(r'^member/edit/(?P<pk>[0-9]+)/$',
	# 	views.MemberUpdate.as_view(), name='edit'),
    # url(r'^member/delete/(?P<pk>[0-9]+)/$',
    # 	views.MemberDelete.as_view(), name='delete'),
]
