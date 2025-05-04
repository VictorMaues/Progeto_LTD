import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Brand, Category, Product, Paciente, Exame  # Remova a segunda importação

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'leito', 'nivel_gravidade', 'liberado_para_alta')
    list_filter = ('nivel_gravidade', 'liberado_para_alta')
    search_fields = ('nome', 'leito')

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'paciente', 'realizado')
    list_filter = ('realizado', 'data')
    raw_id_fields = ('paciente',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price',
                    'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'brand__name', 'category__name')
    list_filter = ('is_active', 'brand', 'category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.category.name,
                             product.price, product.is_active, product.description,
                             product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]