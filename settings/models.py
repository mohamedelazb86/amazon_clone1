from django.db import models

class Settings(models.Model):
    name=models.CharField(max_length=120)
    logo=models.ImageField(upload_to='logo')
    subtitle=models.TextField(max_length=500)
    call_us=models.TextField(max_length=120)
    email_us=models.TextField(max_length=120)
    phones=models.TextField(max_length=120)
    address=models.TextField(max_length=200)
    facebook=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)
    android_apps=models.URLField(null=True,blank=True)
    ios_apps=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
