from django.urls import path, include

path('', include('core.urls', namespace='core')),
path('categorias/', include('categories.urls', namespace='categories')),
path('produtos/', include('products.urls', namespace='products')),