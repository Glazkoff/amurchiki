import graphene
from .models import CustomUser
from .types import CustomUserType


class UpdateUserTestStatusMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        test_status = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, test_status):
        user = CustomUser.objects.get(pk=user_id)
        # TODO: проверять есть ли ответы уже и стирать их при смене на start
        user.test_status = test_status
        user.save()

        return UpdateUserTestStatusMutation(user=user)