from django.db import models
from .membership import MembershipModel


class CommentModel(models.Model):
    ''' Auto-generated primary key '''
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=500)

    ''' Comment relationships '''
    membership = models.OneToOneField(
        MembershipModel, on_delete=models.CASCADE)

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return "Comment for {}".format(str(self.membership))
