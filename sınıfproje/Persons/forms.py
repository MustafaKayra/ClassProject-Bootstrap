from django import forms
from .models import Report

class ReportForm(forms.ModelForm): #Hakkımızda sayfasındaki geri bildirim formu
    class Meta:
        model = Report #Formun model ile bağlantısının yapılması
        fields = ["name","email","report"] #Geri bildirim formunun alanlarının belirtilmesi