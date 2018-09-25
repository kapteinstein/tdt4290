from ..models import UserModel
from ..scalars import Gender, Language

# Import graphene dependencies
from graphene import relay, Schema, Node, Field, ObjectType, Boolean, String, Int, Mutation
from graphene_django import DjangoConnectionField, DjangoObjectType
from graphene.types import DateTime


class User(DjangoObjectType):
    ''' A NTNUI member'''
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


# Mutations
class CreateUser(Mutation):
    class Arguments:
        first_name = String(required=True)
        last_name = String(required=True)
        date_of_birth = DateTime()
        gender = Gender(required=True)
        customer_no = String()
        register_date = DateTime()
        card_no = String()
        contract_no = Int()
        contract_expiry_date = DateTime()
        language = Language(required=True)
        calling_code = Int()
        phone_no = Int(required=True)
        email = String(required=True)

    success = Boolean()
    error = String()
    user = Field(User)

    def mutate(self, info, first_name=None,
               last_name=None,
               date_of_birth=None,
               gender=None,
               customer_no=None,
               email=None,
               phone_no=None,
               register_date=None,
               card_no=None,
               contract_no=None,
               contract_expiry_date=None,
               language=None,
               calling_code=None):
        try:
            user = UserModel(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                customer_no=customer_no,
                email=email,
                phone_no=phone_no,
                register_date=register_date,
                card_no=card_no,
                contract_no=contract_no,
                contract_expiry_date=contract_expiry_date,
                language=language,
                calling_code=calling_code)
            user.save()

            return CreateUser(user=user, success=True)
        except Exception as e:
            print("Could not creat user due to {}".format(e))
            return CreateUser(user=None, success=False, error=str(e))


class Queries(ObjectType):
    user = Field(User, description='A single ntnui user', id=Int())
    all_users = DjangoConnectionField(
        User, description='All ntnui users')

    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=_id)


class Mutations(ObjectType):
    # Root mutation, exported at EOF
    create_user = CreateUser.Field()


user_schema = Schema(query=Queries, mutation=Mutations)
