from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    uuid = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    price = serializers.DecimalField(decimal_places=2, max_digits=30)
    # cost of goods sold (cogs) is the manufacturing cost associated with the item.
    cogs =  serializers.DecimalField(decimal_places=2, max_digits=30)
    quantity = serializers.IntegerField()
    origin_country = serializers.CharField(max_length=50)
    weight = serializers.DecimalField(decimal_places=2, max_digits=30) # kg by default
    deletion_comment = serializers.CharField(max_length=50)
    deletion_time = serializers.DateTimeField()