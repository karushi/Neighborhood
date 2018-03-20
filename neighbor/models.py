from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

# User=get_user_model()

class Neighbourhood(models.Model):
    name=models.CharField(max_length=80)
    location=models.CharField(max_length=70)
    occoupants_count=models.IntegerField()
    user_admin=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def create_neigborhood(self):
            self.save()

    def delete_neigborhood(self):
            self.delete()

    @classmethod
    def find_neigborhood(cls,neigborhood_id):
            pass

    @classmethod
    def update_neighborhood(cls):
            pass

    @classmethod
    def update_occupants(cls):
            pass    

class Business(models.Model):
    name=models.CharField(max_length=60)
    user=models.ForeignKey(User)
    Neighbour=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email=models.CharField(max_length=60)


    def __str__(self):
        return self.name

    def create_business(self):
            self.save()

    def delete_business(self):
            self.delete()

    @classmethod
    def find_business(cls,business_id):
            pass

    @classmethod
    def update_business(cls):
            pass    


        
class User(models.Model):
    name=models.CharField(max_length=60)
    profile_phots=models.ImageField(upload_to='images/',blank=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Neighbour=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user_email=models.CharField(max_length=60)


    def __str__(self):
        return self.name

        


class Post(models.Model):
    title=models.CharField(max_length=60 )
    post=models.TextField()
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    post_image=models.ImageField(upload_to='images/',blank=True,null=True)


    def __str__(self):
        return self.title

    @classmethod
    def get_post(cls):
        posts=Post.objects.all()


    @classmethod
    def search_by_business(cls,search_term):    
        profile=cls.objects.filter(user__username__icontains=search_term)
        return profile  

# def create_user(sender, **kwargs):
#      if kwargs['created']:
#            profile = Profile.objects.create(user_id=kwargs['instance'])

# post_save.connect(create_user, sender=User)