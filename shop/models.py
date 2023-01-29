from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class UserInf(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_id}"


class UserAdress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField("Full name",max_length=1024,)
    address1 = models.CharField("Address line 1",max_length=1024,)
    address2 = models.CharField("Address line 2",max_length=1024,)
    zip_code = models.CharField("ZIP / Postal code",max_length=12,)
    city = models.CharField( "City",max_length=1024,)
    country = models.CharField("Country",max_length=30,)
    def __str__(self):
        return f"{self.title}"


class UserPayment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    card_no = models.CharField(max_length=50)
    expiration = models.CharField(max_length=50)
    cvv = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    #expiry = models.DateField(blank=True)

    def __str__(self):
        return f"{self.user_id}"


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    image = models.ImageField(upload_to='productImg/', null=True)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)


class subCategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_category = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(blank=True)
    stock = models.IntegerField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='productImg/', null=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    sold_count = models.IntegerField(blank=True, default=0)
    top_featured = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.product_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    @property
    def count(self):
        return self.category_id.slug


class ShoppingSession(models.Model):
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    total = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f"{self.user_id}"


class Cart(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    session_id = models.ForeignKey(
        ShoppingSession, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    ordered = models.BooleanField(default=False, null=True)

    @property
    def productName(self):
        return self.product_id.product_name

    @property
    def productImage(self):
        return self.product_id.image

    @property
    def productPrice(self):
        return self.product_id.price

    @property
    def productSlug(self):
        return self.product_id.slug

    @property
    def productId(self):
        return self.product_id


class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.user_id}"


class OrderItems(models.Model):
    order_id = models.ForeignKey(
        Orders, null=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f"{self.product_id}"
  


class Discount(models.Model):
    discount = models.PositiveIntegerField(blank=True)
    product_id = models.OneToOneField(
        Product, null=True, on_delete=models.CASCADE)
    # def __str__(self):
    # return f"{self.product_id}


class Media(models.Model):
    image = models.ImageField(upload_to='movie/images/')
    product_id = models.ForeignKey


class Newsteller(models.Model):
    email = models.EmailField(unique=True, max_length=100)

    def __str__(self):
        return f"{self.email}"


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Wishlist(models.Model):
    product_id = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
