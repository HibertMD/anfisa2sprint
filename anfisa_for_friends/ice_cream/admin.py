from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput

from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'

class IceCreamInline(admin.TabularInline):
    fields = ('title',
              'is_published',
              'is_on_main',
              'description',
              'category',
              'wrapper',
              'toppings',),
    model = IceCream
    extra = 0

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '30'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 45})},
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)
    actions_selection_counter = False


admin.site.register(Topping)
admin.site.register(Wrapper)
