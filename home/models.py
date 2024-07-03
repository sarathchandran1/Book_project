from django.db import models

# Create your models here.


class Auther(models.Model):

    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return '{}'.format(self.name)
    

class Book(models.Model):

    title = models.CharField(max_length=200,null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='book_media')
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE)
    quantity = models.IntegerField()



    def __str__(self):
        return '{}'.format(self.title)