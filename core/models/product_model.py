from django.contrib.auth import get_user_model
from django.db import models

from core.managers import CategoryManager, ProductManager, TagManager
from e_commerce.utils import BaseModel

User = get_user_model()


class Image(BaseModel):

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class MetaData(BaseModel):
    class META_TYPES(models.TextChoices):
        TAG = "TAG", "Tag"
        CATEGORY = "CATEGORY", "Category"

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=META_TYPES.choices)

    class Meta:
        verbose_name = "Meta data"
        verbose_name_plural = "Meta datas"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.type, self.name)


class Tag(MetaData):

    objects = TagManager()

    class Meta:
        proxy = True


class Category(MetaData):

    objects = CategoryManager()

    class Meta:
        proxy = True


class Product(BaseModel):

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category"
    )
    tags = models.ManyToManyField(Tag, default=[], related_name="tags")
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def images(self):
        return Image.objects.filter(product_id=self.id)
