import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from faker import Faker
import random
from products.models import Products , Brand , Catgory 

def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg']
    for _ in range(n):
        name = fake.name()
        image = f"Brand/{images[random.randint(0,7)]}"
        Brand.objects.create(
            name = name,
            image = image
        )
         
def seed_catgory(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg']
    for _ in range(n):
        name = fake.name()
        image = f"Cagtory/{images[random.randint(0,5)]}"
        Catgory.objects.create(
            name = name,
            image = image
        )

def seed_products(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpeg','10.jpeg','11.jpeg','12.jpeg']
    flag_type = ['new' , 'sale' , 'fature']
    for _ in range(n):
        name = fake.name()
        image = f"proudcts/{images[random.randint(0,11)]}"
        sku = random.randint(1,15154)
        subtitle = fake.text(max_nb_chars = 150)
        desc = fake.text(max_nb_chars = 300)
        price = round(random.uniform(20.99,99.99),2)
        rate = random.uniform(0,5)
        flag = flag_type[random.randint(0,2)]
        catgory = Catgory.objects.get(id=random.randint(36,65))
        brand = Brand.objects.get(id=random.randint(49,78))
        Products.objects.create(
            name = name,
            image = image,
            sku = sku,
            rate = rate,
            subtitle = subtitle,
            dec = desc,
            price = price,
            brand = brand,
            catgory = catgory,
            flags = flag,
        )

seed_brand(250)
seed_catgory(250)
seed_products(850)