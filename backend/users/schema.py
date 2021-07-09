import graphene
from .models import CustomUser
from .types import CustomUserType
from .mutations import UpdateUserTestStatusMutation

class Query(graphene.ObjectType):
    users = graphene.List(CustomUserType)
    user = graphene.Field(CustomUserType, user_id=graphene.ID())

    def resolve_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_user(self, info, user_id):
        return CustomUser.objects.get(pk=user_id)


class Mutation(graphene.ObjectType):
    updateUserTestStatus = UpdateUserTestStatusMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)