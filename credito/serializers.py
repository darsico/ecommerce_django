from rest_framework import serializers
from . import models

class CreditoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Pagos
		fields = "__all__"