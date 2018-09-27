from django.db import models
""" from database.models.user import UserModel
from database.models.group import GroupModel
 """
# Create your models here.
class AbstractForm(models.Model): 
    form_name = models.CharField(max_length=40)
"""
    form_instantiatior = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    form_owner_groups = models.ManyToManyField('GroupModel')
    form_signers = models.ManyToManyField('UserModel')
    signatures = models.ManyToManyField('UserModel')
    # actions = models.ManyToManyField()
    # form_contents = models.ManyToManyField()

 """