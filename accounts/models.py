from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length= 200, null=True)
    Phone = models.CharField(max_length= 200, null=True)
    email = models.CharField(max_length= 200, null=True)
    date_created = models.DateField( auto_now_add=  True, null=True)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
      return self.name

    
class Product(models.Model):
    CATE = (('Indoor','Indoor'),
    ('Out Door','Out Door')
    ,)
    name = models.CharField(max_length=200,  null=True)
    price =models.CharField(max_length=200,  null=True)
    category = models.CharField(max_length=200, choices=CATE)
    Description = models.CharField(max_length=200, null=True, blank=True )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
  
        
    
class Order(models.Model):
    STATUS =(('pending','pending'),
    ('Out For Delivery','Out For Delivery'),
    ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL )
    product =models.ForeignKey(Product, null=True, on_delete= models.SET_NULL )
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)
    note = models.CharField(max_length=2000, null=True)
    
    def __str__(self):
        return self.product.name
    

