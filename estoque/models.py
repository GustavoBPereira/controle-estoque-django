from django.db import models
from django.core.validators import MinValueValidator

class Estoque(models.Model):
    # id already declared
    produto = models.CharField(max_length=120)
    quantidade_em_estoque = models.IntegerField(default=0 ,validators=[MinValueValidator(0)])
    estoque_minimo = models.IntegerField(default=0 ,validators=[MinValueValidator(0)])

    def __str__(self,):
        return self.produto
# Create your models here.
