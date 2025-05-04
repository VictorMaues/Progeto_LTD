from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='products', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='products', verbose_name='Categoria')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']
        verbose_name = 'Produto'

    def __str__(self):
        return self.title

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    leito = models.CharField(max_length=10)
    nivel_gravidade = models.CharField(
        max_length=10,
        choices=[
            ('critico', 'Crítico'),
            ('alto', 'Alto'),
            ('medio', 'Médio'),
            ('baixo', 'Baixo')
        ]
    )
    liberado_para_alta = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Exame(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='exames')  # Corrigido para singular
    nome = models.CharField(max_length=100)
    data = models.DateField()
    resultado = models.TextField(blank=True, null=True)  # Adicionei campo opcional
    realizado = models.BooleanField(default=False)  # Adicionei campo status

    def __str__(self):
        return f"{self.nome} ({self.data}) - {self.paciente.nome}"