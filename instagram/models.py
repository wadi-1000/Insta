from django.db import models
from vote.models import VoteModel
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Image(VoteModel, models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = CloudinaryField('image', default='image')
    image_name = models.CharField(max_length=100)
    caption = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  '{}'.format(self.image_name)

    def save_post(self):
        self.save()
    @classmethod
    def delete_post(cls, id):
        image = cls.objects.filter(id).all()
        image.delete() 


    @classmethod
    def get_single_image_by_id(cls, id):
        image = cls.objects.filter(pk=id)
        return image

    @classmethod
    def search_by_author(cls, search_term):
        users = cls.objects.filter(author__username__icontains=search_term)
        return users
class Comments(models.Model):
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    models.ForeignKey(Image,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.content)

    def vaild(self):
        self.vaild = True
        self.save()



# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     post = models.ForeignKey(Image, on_delete=models.CASCADE)
#     value = models.CharField(choices=, default='Like', max_length=10)


