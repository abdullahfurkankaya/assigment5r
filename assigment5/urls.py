from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^todos/',include("todo.urls")),
    url('^blog/entries/',include("blog.urls")),
    url('^users/', include("users.urls")),
    url('^tags/', include("tags.urls")),

]
