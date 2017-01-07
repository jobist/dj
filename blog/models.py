from django.db import models

# Create your models here.


class Category(models.Model):
    name models.CharField(max_length=250, db_index=True, unique=True, blank=True, default="", verbose_name='Название')
    title = models.CharField(max_length=250, blank=True, verbose_name='Заголовок в браузере')
    metakey = models.CharField(max_length=250, blank=True, verbose_name='Ключевые слова')
    metadesc = models.CharField(max_length=250, blank=True, verbose_name='Мета описание')
    slug = models.CharField(max_length=250, unique=True, blank=True, verbose_name='Урл')
    parent = models.ForeignField('self', blank=True, null=True, verbose_name='Родительская категория')
    published = models.BooleanField(verbose_name='Опубликован', default=0)
    ordering = models.IntegerField(verbose_name='Порядок сортировки', default=0, blank=True, null=True)
    count_posts = models.IntegerField(verbose_name='Количество постов', default=0, blank=True, null=True)

    @property
    def name2(self):
        return self.name + self.title

    def save(self):
        super(Category, self).save()

    def ger_url(self):
        return "/blog/%s" % self.slug

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Категории"
        verbose_name="Категории"
        ordering = ['ordering']