from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^$', "recepies.views.recipe_list"),
    url(r'^create/$', "recepies.views.recipe_create"),
    url(r'^detail/(?P<id>[\w\-]+)/$', "recepies.views.recipe_detail"),
    url(r'^update/$', "recepies.views.recipe_update"),
    url(r'^delete/$', "recepies.views.recipe_delete"),
]
