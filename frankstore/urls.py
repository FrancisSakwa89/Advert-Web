from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^searchme/', views.searchme,name = 'searchme'),
    url(r'^adverts/', views.adverts, name='adverts'),
    url(r'^new/advert$',views.newadvert, name='newadvert'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^adverts/(\d+)', views.adverts, name='adverts'),
    # url(r'^new/business/',views.newbusiness, name='newbusiness'), 
    url(r'^new/profile$',views.newprofile, name='newprofile'),
    # url(r'^new/comment/',views.newcomment, name='newcomment'), 
    # url(r'^new/post$',views.newpost, name='newpost'),
    # url(r'^mail$',views.mail,name='mail'),
    # url(r'^chat/', views.chat, name='chat'),
    # url(r'^subscribe/', views.subscribe, name='subscribe'),
    # url(r'^business$', views.business,name = 'business'),
    url(r'^search/', views.search,name = 'search'),
    url(r'^advert/(?P<pk>\d+)/remove/$', views.advert_remove, name='advert_remove'),
    url(r'^myadvert/', views.myadvert, name='myadvert'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
