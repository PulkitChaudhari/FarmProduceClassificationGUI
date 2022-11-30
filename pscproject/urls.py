
from django.contrib import admin
from .view import mainpage
from django.urls import path,include,re_path
from . import view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", mainpage),
    path("predictImage",view.predictImage,name='predictImage'),
    path("aboutAlgorithm",view.aboutAlgorithm)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)