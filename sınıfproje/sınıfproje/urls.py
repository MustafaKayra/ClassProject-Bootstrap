from django.contrib import admin
from django.urls import path,include
from Persons import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/',include("Persons.urls")),
    path('',views.index,name="index"),
    path('about/',views.about,name="about")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
