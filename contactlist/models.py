from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Contact(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(default=0, validators=[MaxValueValidator(99), MinValueValidator(0)])
    email = models.EmailField()
    twitterAccount = models.CharField(max_length=45, null=True, blank=True)
    telegramAccount = models.CharField(max_length=45, null=True, blank=True)
    dataCadastro = models.DateField(auto_now_add=True)
    dataModificacao = models.DateField(auto_now=True)

    sexoOpcao = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não se aplica')
    )

    sexo = models.CharField(max_length=1, choices=sexoOpcao)


    def __str__(self):
        return self.nome