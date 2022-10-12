from django.db import models
from django.contrib import admin
from django.db import models
from django.utils import timezone
from user.models import NewUser 



# Create your models here.

class tourist(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200,null=True,unique =True)
    description = models.TextField(null=True,blank=True)
    createdAt =models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(null=True, default=0)
    numReviews=models.PositiveIntegerField(null=True,blank=True,default=0)
    location = models.CharField(max_length=100, null =True )
    image=models.ImageField(upload_to ='uploads', blank=True,null=True)  
  

    def __str__(self):
        return self.user

class Review(models.Model):
    # title=models.CharField(max_length=100)
    user = models.ForeignKey(NewUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200,null=True,unique=True)
    post=models.ForeignKey(tourist,on_delete=models.CASCADE,null=True)
    slug =models.SlugField(blank=True,null=True)
    likes=models.PositiveIntegerField(null=True)
    comment=models.TextField(null=True,blank=True) 

    def save(self,*args, **kwargs):
        # self.slug = slugify(self.comment[:30])
        super(Review,self) .save (*args, **kwargs)
    
    def __str__(self):
        return self.slug

    
    def __str__(self):
        return self.name


# Create your models here.
