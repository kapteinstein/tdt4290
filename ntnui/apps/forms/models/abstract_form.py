from django.db import models

# Create your models here.
class AbstractForm(models.Model):
    form_name = models.CharField(max_length=40)
    form_instantiatior = models.ForeignKey('database.UserModel', on_delete=models.CASCADE, related_name="form_instantiatior")
    form_owner_groups = models.ManyToManyField('database.GroupModel', related_name="form_owner_groups")
    form_signers = models.ManyToManyField('database.UserModel', related_name="form_signers")
    #signatures = models.ManyToManyField('database.SignModel')
    #actions = models.ManyToManyField('')
    #form_contents = models.ManyToManyField('')

    class Meta:
        abstract = True