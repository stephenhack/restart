from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all-projects/', views.allProfiles, name='all-profiles'),
    url(r'^detail/(?P<profile_id>[0-9]+)/', views.detail, name='detail'),
    url(r'^checkout/(?P<profile_id>[0-9]+)/', views.checkout, name='checkout'),
    url(r'^charities/', views.charitiesIndex, name='charitiesIndex'),
    url(r'^charities-detail/(?P<charity_id>[0-9]+)/', views.charitiesDetail, name='charitiesDetail'),
    url(r'^charities-checkout/(?P<charity_id>[0-9]+)/', views.charitiesCheckout, name='charitiesCheckout'),
    url(r'^new/', views.new_project, name='new'),
    #url(r'^user/'
    #url(r'^charities/'
]