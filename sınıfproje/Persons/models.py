from django.db import models
from django.utils.text import slugify

class Person(models.Model): #Kişileri veritabanına kaydetmek için oluşturulan model
    name = models.CharField(blank=False,null=False,max_length=200) #Kişinin adı
    description = models.TextField() #Kişinin küçük biyografisi
    image = models.ImageField(upload_to="C:/Users/kayra/sınıfproje/static/img") #Kişinin fotoğrafı
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True) #Kişinin site içerisindeki sanal kimliği diyebiliriz.
    category = models.CharField(blank=True,null=True,max_length=200) #Kişinin bulunduğu kategori

    def str(self): #Admin panelinde kişinin ismine göre gösterilmesi
        return f"{self.name}"
    
    def save(self, *args, **kwargs): #Slug alanını otomatik olarak kişinin ismine göre kaydetmesi
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Report(models.Model): #Hakkımızda sayfasındaki geri bildirim formunu veritabanına kaydetmek için oluşturulan model
    name = models.CharField(blank=False,null=False,max_length=30) #Bildirimi yapan kullanıcının adı
    email = models.EmailField(blank=False,null=False) #Bildirimi yapan kullanıcının emaili
    report = models.TextField() #Bildirimi yapan kullanıcının belirtmek istediği şeyler
