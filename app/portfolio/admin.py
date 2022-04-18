from django.contrib import admin
from .models import Image, Project, Category, Project, Email, Socials, Profile
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.forms.widgets import DynamicArrayTextareaWidget
from django_better_admin_arrayfield.forms.fields import DynamicArrayField


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'filter', 'created_at', 'updated_at')
    search_fields = ('name', 'filter')


@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'icon_name',
                    'url', 'created_at', 'updated_at')


admin.site.register(Profile)
admin.site.register(Email)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_small', 'url', 'created_at', 'updated_at')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        DynamicArrayField: {'widget': DynamicArrayTextareaWidget},
    }

    list_display = ('name', 'tags', 'technologies',
                    'client', 'ongoing', 'description')
    search_fields = ('name', 'tags', 'technologies',
                     'client', 'ongoing', 'description')
    list_filter = ('technologies', 'ongoing', 'categories')
