from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.DecimalField(decimal_places=2, max_digits=30)
    # cost of goods sold (cogs) is the manufacturing cost associated with the item.
    cogs =  forms.DecimalField(decimal_places=2, max_digits=30)
    quantity = forms.IntegerField()
    origin_country = forms.CharField(max_length=50)
    weight = forms.DecimalField(decimal_places=2, max_digits=30) # kg by default