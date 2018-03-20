from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __repr__(self):
        return self.first_name.title() + " " + self.last_name.title()
