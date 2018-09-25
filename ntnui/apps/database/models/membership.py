from django.db import models
from datetime import date, timedelta


def one_year_from_today():
    return date.today() + timedelta(days=365)


class MembershipModel(models.Model):
    ''' Membership details '''
    # Auto-generated membership number as primary key
    membership_no = models.AutoField(primary_key=True)

    # Default to object creation time, but allow this to be set manually
    date_joined = models.DateField(default=date.today)

    # Whether or not the membership fee has been payed (if applicable)
    # TODO: Figure out the necessary requirements for membership payment and exipry
    group_expiry = models.DateField(default=one_year_from_today)

    # Sports license details
    sports_license_expiry = models.DateField(
        default=None, null=True, blank=True)
    sports_license_no = models.CharField(max_length=40, null=True, blank=True)

    ''' Membership relationships '''
    member = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    group = models.ForeignKey('GroupModel', on_delete=models.CASCADE)

    # Comment should also be available from membership with its OneToOneField (if not add a foreignKey here)

    ''' Membership methods '''

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"

    def __str__(self):
        return "Membership for {} to {}".format(str(self.member), str(self.group))

    def save(self, *args, **kwargs):
        ''' On first save add the date_joined if not changed '''
        return super(MembershipModel, self).save(*args, **kwargs)
