from django.db import models

# Create your models here.
class Product(models.Model):
    Title =models.CharField(max_length=50)
    Description=models.TextField()
    Price =models.IntegerField()
    Unique_code=models.BooleanField(default=True)
    choice=('10','10'),('20','20'),('30','30')
    Size =models.CharField(choices=choice,max_length=50)
    
    def __str__(self) :
        return self.Title
    
    
class ColourModel(models.Model):
    
    Product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='color')
    choice=('red','red'),('blue','blue'),('green','green'),('black','black')
    Colour =models.CharField(choices=choice,max_length=50)
    
    def __str__(self) :
        return self.Product.Title
    
class productImage(models.Model):
              
        Product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='image')
        image=models.ImageField(upload_to='images')
        
        def __str__(self) :
         return self.Product.Title
        