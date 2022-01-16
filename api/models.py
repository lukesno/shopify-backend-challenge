from django.db import models
from datetime import datetime

# Abstract model that handles deletion
# Extracted out the deletion logic for modularity
class Deletion(models.Model):
    
    # Making Deletion an abstract model; meaning Deletion can't be initialized on its own
    class Meta:
        abstract = True
    
    def delete(self, comment):
        ## use .strftime("%Y/%m/%d %H:%M:%S") on deletion_time when portraying to users
        # Standardized to GMT time
        self.deletion_time = datetime.utcnow()
        self.deletion_comment = comment
        print("hi")
        # saving changes back into database
        self.save()
    
    # Calling original delete() from models.Model
    def hard_delete(self):
        super(Deletion, self).delete()

class Item(Deletion):
    uuid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=30)
    # cost of goods sold (cogs) is the manufacturing cost associated with the item.
    cogs =  models.DecimalField(default=0, decimal_places=2, max_digits=30)
    quantity = models.IntegerField(default=0)
    origin_country = models.CharField(max_length=50)
    weight = models.DecimalField(default=0, decimal_places=2, max_digits=30) # kg by default
    deletion_comment = models.CharField(blank=True, null=True, max_length=50)
    deletion_time = models.DateTimeField(blank=True, null=True)

    ## i = Item(uuid=uuid.uuid4(), name="Nintendo Switch OLED", price=300, cogs=257, quantity=1000, origin_country="Japan", weight=0.30)
    # Returning the item's name whenever Item object is casted to a string
    def __str__(self):
        return self.name
