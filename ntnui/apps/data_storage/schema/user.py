from graphene_django import DjangoObjectType
from ..models import UserModel

# Import resolvers
from .user_resolver import resolve_get_users

# Import graphene dependencies
from graphene import ObjectType, Mutation, Schema, List, Field, String, Boolean


class User(DjangoObjectType):
    ''' A NTNUI member'''

    class Meta:
        model = UserModel


# Mutations
class CreateUser(Mutation):
    class Arguments:
        first_name = String()
        last_name = String()

    success = Boolean()
    user = Field(lambda: User)

    def mutate(self, info, first_name, last_name):
        try:
            user = UserModel.objects.create(
                first_name=first_name, last_name=last_name)
            return CreateUser(user=user, success=True)
        except Exception as e:
            print("Could not creat user due to {}".format(e))
            return CreateUser(user=None, success=False)


class Queries(ObjectType):
    # Root query, exported at EOF
    users = List(User, description='A list of ntnui users',
                 resolver=resolve_get_users)


class Mutations(ObjectType):
    # Root mutation, exported at EOF
    create_user = CreateUser.Field()


user_schema = Schema(query=Queries, mutation=Mutations)
