from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    pages=models.IntegerField()
    language=models.CharField(max_length=20)
    cover=models.ImageField(upload_to='covers')
    pdf=models.FileField(upload_to='pdfs')

    def __str__(self):
        return self.title