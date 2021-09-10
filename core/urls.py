
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from web import views
from web.views import *

app_name = "web"

# # from views import HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view()),
    path('graph/', graph, name="graph"),
    path('tempChart/', views.tempChart, name='tempChart'),
    path('presChart/', views.presChart, name='presChart'),
    path('humChart/', views.humChart, name='humChart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)