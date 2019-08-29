from django.db import models
from django.contrib.auth.models import User
import json, os
from PIL import Image

with open(os.path.dirname(__file__) + '/static/record/countries.json') as f:
    countries_json = json.loads(f.read())
    COUNTRIES_ISD_CODES = [(str(country["code"]), str(country["name"])) for country in countries_json]

TYPE_CHOICES = (
    ('1','Candidate'),
    ('2','Employer')
)
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    typeuser = models.CharField(choices=TYPE_CHOICES, verbose_name=u"Type User", null=True, blank=False, max_length=10)
    image = models.ImageField(default='default.png', upload_to='profile_pics', verbose_name=u"Avatar", )
    phone = models.CharField(max_length=300, verbose_name=u"Phone number", null=True, blank=True, help_text=u"Please enter your Phone")
    suscription = models.BooleanField(verbose_name=u"suscription newsletter",default=True)
    #country = models.CharField(choices=json_data[0].name, verbose_name=u"Country", null=True, blank=False, max_length=10)
    country = models.CharField(choices=COUNTRIES_ISD_CODES, help_text="Country ISD code loaded from JSON file",max_length=100,null=True)

    def __str__(self):

        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)