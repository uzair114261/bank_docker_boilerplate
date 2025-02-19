from rest_framework import serializers

from bank_management_system.authentication.api.serializers import UserSerializer
from bank_management_system.authentication.models import User
from bank_management_system.banks.api.serializers import Bank, BankSerializer

from ..models import Account


class AccountDetailSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ["id", "bank", "balance", "user"]


class AccountSerializer(serializers.ModelSerializer):
    # bank = BankSerializer()
    # user = UserSerializer()
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Account
        fields = ["id", "bank", "balance", "user"]

    def create(self, validated_data):
        user = self.context["request"].user
        bank = validated_data.pop("bank")

        account = Account.objects.create(user=user, bank=bank, balance=validated_data["balance"])
        return account
