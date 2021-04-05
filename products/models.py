from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55, verbose_name='categoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=55, verbose_name='Nome')
    normal_price = models.CharField(max_length=10, verbose_name='Preço')
    promotion_price = models.CharField(max_length=10, verbose_name='Preço promocional')
    promotion = models.BooleanField(default=False, verbose_name='Em promoção')
    picture = models.ImageField(upload_to='products/%Y/%m/', verbose_name='Imagem')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
