from django.db import models

# Create your models here.
DESCRIPTION=(
    ('book','book'),
    ('poster','poster'),
    ('flier','flier'),
    ('notebook','notebook'),
    ('booklet','booklet'),
    ('banner','banner'),
)
THEMATIC=(
    ('SRHR','SRHR'),
    ('H&G','H&G'),
    ('HIV/TB','HIV/TB'),
    ('WLPR','WLPR'),
    ('SILU','SILU')
)

class IecMaterial(models.Model):
    title=models.CharField('material Title',max_length=200)
    author=models.CharField('author',max_length=200,null=True,blank=True)
    description=models.CharField('Description',choices=DESCRIPTION, max_length=200)
    thematic=models.CharField('Thematic',choices=THEMATIC,max_length=200,null=True,blank=True)
    quantity=models.IntegerField('Quantity',null=True,blank=True)
    dates=models.DateField(auto_now_add=True)
    name=models.CharField('your name',max_length=200,null=True,blank=True)
    copies_requested=models.IntegerField('copies requested',null=True,blank=True)
    copies_returned=models.IntegerField('copies returned',null=True,blank=True)

    def __str__(self):
        return self.title

    
