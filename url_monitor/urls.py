from django.conf.urls import url
from django.urls import include

from url_monitor import views

urlpatterns = [
    url(r'sync/url/(?P<url_obj_id>\d+)/$', views.SyncUrl.as_view(), name='sync_url'),
    url(r'sync/urls/$', views.SyncUrlSet.as_view(), name='sync_url_set'),
    url(r'active/(?P<url_obj_id>\d+)/$', views.SyncActive.as_view(), name='active'),
    url(r'$', views.Base.as_view(), name='base'),

]