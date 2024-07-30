from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "date_joined",
            "about",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    #  Sobrescribe el método 'create' para manejar la creación de una nueva instancia del modelo
    def create(self, validated_data):

        # elimina el campo password del diccionario validated_data y lo asigna a la variable password
        # si password no está en validated_data, se asigna None a password
        password = validated_data.pop("password", None)

        # crea una instancia del modelo CustomUser con el resto de los datos validados (que ya no incluyen la contraseña)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            # se establece la contraseña utilizando el método set_password. Esto asegura que se almacene de manera segura (hashed)
            instance.set_password(password)

        instance.save()  # Guarda la instancia del modelo en la base de datos

        return instance  # Devuelve la instancia creada
