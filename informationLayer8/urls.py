from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from django.conf import settings
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url('', include('social_django.urls', namespace='social')),
	url(r'^$', TemplateView.as_view(template_name="home.html"),
        name="home"),
	url(r'^users/logout/$',	logout, {'next_page': 'home'},
        name="logout"),
    url(r'^', include('members.urls', namespace='members')),
    url(r'^', include('events.urls', namespace='events')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
