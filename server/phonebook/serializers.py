from rest_framework import serializers

from .models import Address, PhoneBookRecord


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "country",
            "state",
            "city",
            "line_1",
            "line_2",
        ]


class PhoneBookRecordSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = PhoneBookRecord
        fields = [
            "id",
            "name",
            "number",
            "email",
            "profile_picture",
            "address",
        ]

    def create(self, validated_data):
        address_data = validated_data.pop("address")

        address = Address.objects.create(**address_data)

        record = PhoneBookRecord.objects.create(
            address=address,
            user=self.context["request"].user,
            **validated_data,
        )

        return record

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)

        if address_data:
            for key, value in address_data.items():
                setattr(instance.address, key, value)

            instance.address.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
