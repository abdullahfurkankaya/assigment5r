from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', show_blog),
    url(r'^(?P<todo_id>[0-9]+)', get_blog),
    url(r'^all/$', show_entry),
    url(r'^all/user/(?P<userId>[0-9]+)$', show_all_entry),
]
