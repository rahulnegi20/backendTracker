from django.contrib import admin
from .models import Module,Submodule,Resource
# Register your models here.

admin.site.register(Module)
admin.site.register(Submodule)
admin.site.register(Resource)
