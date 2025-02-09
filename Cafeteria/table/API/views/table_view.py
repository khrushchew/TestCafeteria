from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from core.models.table import Table

from table.API.serializers.table_serializer import TableSerializer

class TableView(ViewSet):
    def get_table(self):
        try:
            table = Table.objects.get(pk=self.kwargs.get('pk')) 
            return table
        except:
            raise NotFound(detail='Стол не найден!')

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = TableSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"detail": 'Стол успешно добавлен!'}, status=201)

    def list(self, request, *args, **kwargs):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        try:
            return Response(serializer.data, status=200)
        except:
            return Response(data={'detail': 'Ошибка сервера'}, status=500)
    
    def retrieve(self, request, *args, **kwargs):
        table = self.get_dish()
        serializer = TableSerializer(table)
        return Response(serializer.data, status=200)
    
    def partial_update(self, request, *args, **kwargs):
        data = request.data
        table = Table.objects.get(pk=kwargs.get('pk'))
        serializer = TableSerializer(table, data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Данные обновлены'}, status=200)

    def update(self, request, *args, **kwargs):
        data = request.data

        table = Table.objects.get(pk=kwargs.get('pk'))

        serializer = TableSerializer(table, data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Данные обновлены'}, status=200)
    
    def destroy(self, request, *args, **kwargs):
        table = self.get_table()
        table.delete()
        return Response({'detail': 'Данные удалены'}, status=200)
