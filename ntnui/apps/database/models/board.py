from django.db import models
from django.core.exceptions import ValidationError
from .enums import ACCESS_CHOICES, ROLE_CHOICES
from ..models import GroupModel
from datetime import date
from copy import deepcopy

# Require every board to have one president and one cashier (no more no less)
BOARD_RESTRICTIONS = {
    "P": 1,
    "C": 1,
}


def validate_user_roles(obj):
    print(BoardModel.objects.all().prefetch_related('roles'))
    # Retrieve list of roles from the model object
    roles = obj.roles.all()

    # Create a new instance of the restricitons object
    board_requirement = deepcopy(BOARD_RESTRICTIONS)

    # Iterate over the current board roles
    for r in roles:
        print(r)

        if r.role in board_requirement:
            # Reduce the 'score' of the requirement for the given role
            board_requirement[r.role] -= 1

    # If the board requirements are not met, raise a validation error!
    for role, num in board_requirement.items():
        if num != 0:
            # Most of this is just pretty text output to the user
            raise ValidationError("There {} be {} {}{} in a group".format(
                "can only " if board_requirement[role] < 0 else "has to ",
                BOARD_RESTRICTIONS[role],
                dict(ROLE_CHOICES)[role], "s" if BOARD_RESTRICTIONS[role] > 1 else ""))


def validate_previous_board(obj):
    if obj.predecessor:
        # Ensure the board is not set as its own predecessor
        if obj.predecessor.board_id == obj.board_id:
            raise ValidationError(
                "The board cannot be set as it's own predecessor!")


class BoardModel(models.Model):
    ''' Board information '''
    # Autogenerated board id as primary key
    board_id = models.AutoField(primary_key=True)
    creation_date = models.DateField(
        default=date.today, null=False, blank=False, editable=True)

    ''' Board relationships '''
    # Reference to the previous board. If null then this is the first board
    predecessor = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True)

    group = models.OneToOneField(
        GroupModel, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        roles = self.rolemodel_set.all().filter()

        # Represent the board as first three members
        members = ", ".join(str(r) for r in roles[:3])

        return members + " - est. " + str(self.creation_date)

    def clean(self):
        ''' This method is "magically" called by django whenever a model instance is saved '''
        validate_user_roles(self)
        validate_previous_board(self)
