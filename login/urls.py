from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from login import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^howto/$', core_views.howto, name='howto'),
    url(r'^naturalteas/$', core_views.naturalteas, name='naturalteas'),
    url(r'^washngo/$', core_views.washngo, name='washngo'),
    url(r'^twistoutbraidout/$', core_views.twistoutbraidout, name='twistoutbraidout'),
    url(r'^boxbraidsandaddins/$', core_views.boxbraidsandaddins, name='boxbraidsandaddins'),
    url(r'^profilepage/$', core_views.profilepage, name='profilepage'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
