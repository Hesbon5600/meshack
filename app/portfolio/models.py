from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models
from django.utils.text import slugify
from django.db.models import Q

# Create a manager to exclude deleted items


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False).order_by('-created_at')


class BaseModel(models.Model):
    """
    The common field in all the models are defined here
    """
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # add deleted option for every entry
    deleted = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True  # Set this model as Abstract


class Category(BaseModel):
    """
    Category model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    filter = models.CharField(max_length=50, blank=True, null=True)
    skill_level = models.PositiveSmallIntegerField(default=50)
    projects_done = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of this `Category`.

        This string is used when a `Category` is printed in the console.
        """
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-created_at']


class Service(BaseModel):
    """
    Service model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of this `Service`.

        This string is used when a `Service` is printed in the console.
        """
        return self.name


class Image(BaseModel):
    """
    Image model
    """
    url = models.URLField(max_length=500, db_index=True,
                          blank=False, null=False)
    is_small = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of this `Image`.

        This string is used when a `Image` is printed in the console.
        """
        return f"{self.url}"


class ExtraImage(BaseModel):
    """
    ExtraImage model
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(max_length=500, db_index=True,
                          blank=False, null=False)

    def __str__(self):
        """
        Returns a string representation of this `ExtraImage`.

        This string is used when a `ExtraImage` is printed in the console.
        """
        return f"{self.name}"


class Project(BaseModel):
    """
    Project model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    slug = models.CharField(max_length=50, db_index=True,
                            blank=True, null=True)
    client = models.CharField(max_length=50, db_index=True,
                              blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    completion_date = models.DateField(max_length=50, db_index=True,
                                       blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=100, null=True, blank=True),
                      null=True, blank=True, default=list)
    technologies = ArrayField(models.TextField(null=True, blank=True),
                              null=True, blank=True, default=list)
    ongoing = models.BooleanField(default=False)
    url = models.URLField(max_length=500, blank=True, null=True)
    thumbnail_image_url = models.URLField(max_length=250,
                                          db_index=True, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)

    def __str__(self):
        """
        Returns a string representation of this `Project`.

        This string is used when a `Project` is printed in the console.
        """
        return self.name

    @property
    def proj_filters(self):
        """
        Returns a list of filters for this project
        """
        return list(self.categories.all().values_list('filter', flat=True))

    @property
    def small_images(self):
        """
        Returns a list of small images for this project
        """
        return list(self.images.filter(~Q(url=self.thumbnail_image_url), is_small=True).values_list('url', flat=True))

    @property
    def large_images(self):
        """
        Returns a list of small images for this project
        """
        return list(self.images.filter(~Q(url=self.thumbnail_image_url), is_small=False).values_list('url', flat=True))

    @property
    def filters(self):
        """
        Returns a list of filters for this project
        """
        return " ".join(self.proj_filters)

    @property
    def filters_formatted(self):
        """
        Returns a list of filters for this project
        """
        return ", ".join(self.proj_filters)

    @property
    def project_index(self):
        projects = Project.objects.all()
        return [projects.count(), list(projects.values_list('name', flat=True)).index(self.name)+1]

    def create_name_slug(self):
        """This method automatically slugs the name before saving"""
        slug = slugify(self.name)
        new_slug = slug
        n = 1
        while Project.objects.filter(slug=new_slug).exists():
            new_slug = '{}-{}'.format(slug, n)
            n += 1

        return new_slug

    def save(self, *args, **kwargs):
        """This method ensures that the project is saved with a slug"""
        if not self.slug:
            self.slug = self.create_name_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class Socials(BaseModel):
    """
    Socials model
    """
    full_name = models.CharField(max_length=50, db_index=True)
    short_name = models.CharField(max_length=50, db_index=True)
    url = models.URLField(max_length=500, db_index=True,
                          blank=False, null=False)
    icon_name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        """
        Returns a string representation of this `Socials`.

        This string is used when a `Socials` is printed in the console.
        """
        return self.full_name

    class Meta:
        verbose_name = "Socials"
        verbose_name_plural = "Socials"
        ordering = ['-created_at']


class Profile(BaseModel):
    """
    Skill model
    """
    name = models.CharField(max_length=50)
    header_image_url = models.URLField(max_length=500,
                                       db_index=True, blank=True, null=True)
    header_message = models.TextField(blank=True, null=True)
    about_message = models.TextField()

    def __str__(self):
        """
        Returns a string representation of this `Profile`.

        This string is used when a `Profile` is printed in the console.
        """
        return self.name


class Email(BaseModel):
    """
    Client model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    email = models.CharField(max_length=50, db_index=True,
                             blank=True, null=True)
    message = models.TextField(
        max_length=5000, blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of this `Email`.

        This string is used when a `Email` is printed in the console.
        """
        return f"<Email - {self.name}>"
