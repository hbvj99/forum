from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from common.resize_image import resize_image

CATEGORY_TYPE = (
    ("Apparels & Accessories", "Apparels & Accessories"),
    ("Automobiles ", "Automobiles "),
    ("Beauty & Health", "Beauty & Health"),
    ("Books & Learning", "Books & Learning"),
    ("Business & Industrial", "Business & Industrial"),
    ("Computer & Peripherals", "Computer & Peripherals"),
    ("Electronics", "Electronics"),
    ("Events & Happenings", "Events & Happenings"),
    ("Home, Furnishing & Appliances ", "Home, Furnishing & Appliances "),
    ("Mobile & Accessories ", "Mobile & Accessories "),
    ("Music Instrument", "Music Instrument"),
    ("Pets & Pet Care", "Pets & Pet Care"),
    ("Real Estate ", "Real Estate "),
    ("Services", "Services"),
    ("Sports & Fitness", "Sports & Fitness"),
    ("Toys & Video Games", "Toys & Video Games"),
    ("Travel, Tour & Packages", "Travel, Tour & Packages"),
    ("Others", "Others"))


class Discussion(models.Model):
    title = models.CharField(max_length=130, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True, editable=False)
    content = RichTextField(blank=False, max_length=1500, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)  # Created
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)  # Updated
    img = models.ImageField(upload_to='images/discussion/%Y/%m/%d/', null=True, blank=True)
    category = models.CharField(max_length=70, blank=False, default='Others', choices=CATEGORY_TYPE)
    tags = models.CharField(max_length=70, blank=True)
    votes = models.ManyToManyField(User, related_name='votes', blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def votes_count(self):
        return self.votes.count()

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Discussion.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        if self.img:
            size = 960, 720
            quality = 75
            upload_to = 'images/discussion/%Y/%m/%d/'
            self.img = resize_image(self.img, size, quality, upload_to)
        super().save(*args, **kwargs)

    def get_tags(self):
        tag = self.tags.split(',')
        return tag

    def delete(self, *args, **kwargs):
        if self.img:
            self.img.delete()
        super().delete(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    content = RichTextField(max_length=300, blank=False)
    post = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def comment_count(self):
        return self.content.count()
