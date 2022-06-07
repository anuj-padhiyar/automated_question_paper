from pyexpat import model
from re import T
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256,db_index=True,unique=True,default='')

    def __unicode__(self):
        return u'{}-{}'.format(self.email,self.get_user_name())

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email
        }

    def get_user_name(self):
        return self.first_name + ' ' + self.last_name
    