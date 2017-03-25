from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
	url(r'^$', TemplateView.as_view(template_name="home.html"),
        name="home"),
	url(r'^users/logout/$',	logout, {'next_page': 'home'},
        name="logout"),

]
