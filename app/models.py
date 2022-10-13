from django.db import models




class services(models.Model):
    head = models.CharField(max_length = 20)
    discription = models.CharField(max_length = 150)
    def __str__(self):
        return self.head


class work(models.Model):
    image1 = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    title = models.CharField(max_length = 100)
    dis = models.CharField(max_length = 200)
    def __str__(self):
        return self.title
    
class about(models.Model):
    img1 = models.ImageField(upload_to = 'media')
    title1 = models.CharField(max_length = 60)
    dis1 = models.TextField(max_length = 500)
    
    img2 = models.ImageField(upload_to = 'media')
    title2 = models.CharField(max_length = 60)
    dis2 = models.TextField(max_length = 500)
    
    def __str__(self):
        return self.title1
    
class massage(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    sub = models.CharField(max_length = 100)
    text = models.TextField(max_length = 500)
    def __str__(self):
        return self.name