from django.test import TestCase
from .models import Image

# Create your tests here.

class PostTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.alex=Image(caption="We are who we are.",image_name='self expression')

    #Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.alex,Image))

    #Testing Save method
    def test_save_method(self):
        self.alex.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_post(self):
        self.image = Image(capation="We are who we are" image_name='self expression')
        self.image.delete_post()
        after = Image.object.all()
        self.assertTrue(len(after)<1)




