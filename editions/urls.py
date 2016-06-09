
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'list/$', views.EditionListView.as_view(), name='edition_list'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.EditionDetailView.as_view(), name='edition_detail'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit_edition, name='edition_edit'),
    url(r'^sync$', views.sync, name='sync'),
    url(r'^sync-status$', views.sync_status, name='sync_status'),
]
