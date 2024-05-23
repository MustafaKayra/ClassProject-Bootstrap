from django.shortcuts import render,get_object_or_404,redirect
from .models import Person,Report
from .forms import ReportForm
from django.contrib import messages

def index(request): #Kişilerin bulunduğu sayfa
    persons = Person.objects.all() #Kayıtlı bütün kullanıcıları çekmek için
    context = { #Çekilen kullanıcıları anasayfaya göndermek için kullanılan sözlük
        "persons":persons
    }
    return render(request,"index.html",context) #Sayfayı render etmek için

def WhoPerson(request,slug): #Her kişinin slug'ına göre filtrelenerek gösterildiği sayfa(detay sayfası)
    person = get_object_or_404(Person,slug=slug) #Kişiyi slug'ına göre filtreleyerek çekmek için
    context = { #Çekilen kişiyi detay sayfasına göndermek için kullanılan sözlük
        "person":person
    }
    return render(request,"person.html",context)

def about(request): #Hakkımızda sayfasında bulunan açıklamayı ve geri dönüşleri alabilmemiz için gereken işlemlerin olduğu sayfa
    form = ReportForm(request.POST or None) #Bildirim formunu almak için
    context = { #Bildirim formunu hakkımızda sayfasına yollamak için
        "form":form
    }
    if form.is_valid(): #Eğer formumuz istenen şekilde doldurulduysa işlemlere devam etmesi için yapılan kontrol
        form.save() #Form kaydı
        messages.success(request,'Bildiriminiz Başarıyla İletildi') #Kullanıcıya formu kaydettiğini bildiren mesaj
        return redirect('about') #Kullanıcının geri hakkımızda sayfasına dönmesi için yönlendirme
    else:
        messages.warning(request,form.errors) #Eğer form istemediğimiz şekilde doldurulmuşsa kullanıcının nerede hata yaptığını bildiren mesaj
        
    return render(request,"about.html",context)