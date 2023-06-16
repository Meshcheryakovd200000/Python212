from django.contrib import admin
# Register your models here.
from .models import Todo


# чтобы в админке появилось время создания "Сreated" в Todos
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)  # покажем что это кортеж ставим запятую


admin.site.register(Todo, TodoAdmin)
