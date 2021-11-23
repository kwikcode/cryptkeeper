from rest_framework import routers, serializers, viewsets, status, permissions, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from .models import *
from io import StringIO
from .transaction_parsers import tools
import json
from .core.crypto_price_finder import crypto_price_finder

### Transactions ###

# Serializers define the API representation.
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ['user']

    def create(self,validated_data):
        request = self.context['request']
        transaction = Transaction.objects.create(**validated_data, user = request.user)
        transaction.save()
        return transaction

# ViewSets define the view behavior.
class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

### File Importer ###
class TransactionImporterSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file')

class TransactionImporterViewSet(viewsets.ViewSet):
    serializer_class = TransactionImporterSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def create(self, request, *args, **kwargs):
        file        = request.FILES.get('file')
        file_name   = file.name

        results = tools.process_transactions_from_file(
            file_name       = file_name, 
            in_memory_file  = file, 
            user            = self.request.user
        )

        return Response(json.dumps(results))

### Spot Price ###
class SpotPriceSerializer(serializers.Serializer):
    asset_symbol = serializers.CharField()
    datetime     = serializers.DateTimeField(format="%Y-%m-%d-%H:%M:%S")

class SpotPriceViewSet(viewsets.ViewSet):
    serializer_class = SpotPriceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response([])

    #ex: http://localhost:8000/api/spot-price/btc/2020-04-30-15-15-30/
    @action(methods=['get'], detail=True, url_path='(?P<datetime>[^/.]+)', serializer_class= SpotPriceSerializer())
    def get_spot_price(self, request, datetime, pk=None):
        serializer = SpotPriceSerializer(data={'asset_symbol': pk, 'datetime': datetime})
        serializer.is_valid(raise_exception=True)

        success, price = crypto_price_finder.get_usd_price(
            datetime        = serializer.validated_data["datetime"],
            asset_symbol    = serializer.validated_data["asset_symbol"]
        )

        if not success:
            return Response("Request could not be completed.", status=400)
        
        return Response(price)