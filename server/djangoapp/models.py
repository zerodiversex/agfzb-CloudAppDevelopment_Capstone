from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='SampleMake')
    description = models.TextField(null=False, max_length=300, default='Sample description')
    
    def __str__(self):
        return self.name
        
class CarModel(models.Model):
    make = models.ForeignKey('CarMake',on_delete=models.RESTRICT)
    name = models.CharField(null=False, max_length=30, default='SampleModel')
    dealerid = models.IntegerField()
    year = models.IntegerField()
    type_list = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
        ('Coupe', 'Coupe'),
    )

    modeltype = models.CharField(
        choices=type_list,
        blank=True,
        max_length=30
    )
    
    car_manager = models.Manager()
    
    def __str__(self):
        return f'{self.name},{self.make},{self.year}'


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        # review dealership
        self.dealership = dealership
        # review name
        self.name = name
        # review purchase
        self.purchase = purchase
        # review review
        self.review = review
        # purchase_date
        self.purchase_date = purchase_date
        # car_make
        self.car_make = car_make
        # car_model
        self.car_model = car_model
        # car_year
        self.car_year = car_year
        # sentiment
        self.sentiment = sentiment
        #id
        self.id = id

    def __str__(self):
        return "Review name: " + self.name