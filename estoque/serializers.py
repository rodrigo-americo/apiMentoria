from rest_framework import serializers
from .models import Pc
import re

class PcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pc
        fields = "__all__"
    def validate_id(self, value):
        # Define o padrão que o ID deve seguir
        pattern = r'^PC[1-5][0][1-9]$|^PC[1-5][1][0]$'

        # Verifica se o ID segue o padrão especificado
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "ID inválido. O ID deve começar com 'PC', seguido por um número de 1 a 5, e terminar com um número de 01 a 10."
            )

        return value