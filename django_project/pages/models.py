from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    cover_url = models.URLField(default='')
    pdf_url = models.URLField(default='')

    
    def __str__(self):
        return self.title + ' - ' + self.cover_url + ' - ' + self.pdf_url