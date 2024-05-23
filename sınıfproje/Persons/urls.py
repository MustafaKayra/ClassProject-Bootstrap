from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('person/<slug:slug>',views.WhoPerson,name="WhoPerson") #WhoPerson fonksiyonu ile filtrelediğimiz kişinin sayfasına yönlendirilmesi
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Static dosyalarının urlpatterns içerisindeki sayfalara yönlendirilmesi