from rest_framework import serializers

from core.models.table import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('pk', 'position')
