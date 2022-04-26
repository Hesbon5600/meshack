from django.contrib import admin
from .models import ExtraImage, Image, Project, Category, Project, Email, Service, Socials, Profile
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


admin.site.register(Email)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'header_message', 'about_message', 'header_image_url', 'resume_link', 'created_at', 'updated_at')
@admin.register(Service)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon',)




@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_small', 'url', 'created_at', 'updated_at', 'deleted')
@admin.register(ExtraImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'created_at', 'updated_at', 'deleted')


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
