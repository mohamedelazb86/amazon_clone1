import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from products.models import Brand,Product,Review
from authuser.models import User
import random

def seed_brand(n):
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    fake=Faker()
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'image_brand/{images[random.randint(0,9)]}'
        )

def seed_product(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    flag=['New','Sale','Feature']
    brands=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            image=f'image_product/{images[random.randint(0,9)]}',
            flag=flag[random.randint(0,2)],
            brand=brands[random.randint(0,len(brands)-1)],
            price=round(random.uniform(5.55,99.99),2),
            subtitle=fake.text(max_nb_chars=500),
            descriptions=fake.text(max_nb_chars=5000),
            quantity=random.randint(10,1000),
            sku=random.randint(100,100000000)


        )



def seed_review(n):
    fake=Faker()
    users=User.objects.all()
    products=Product.objects.all()
    for _ in range(n):
        Review.objects.create(
            user=users[random.randint(0,len(users)-1)],
            product=products[random.randint(0,len(products)-1)],
            review=fake.text(max_nb_chars=400),
            rate=random.randint(1,6),

        )

# seed_brand(150)
# seed_product(700)
seed_review(500)
