from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from social_media.app.urls import urlpatterns as app_apis


urlpatterns = [

    url(r'^app/', include(app_apis)),
    url(r'^admin/', admin.site.urls),

]