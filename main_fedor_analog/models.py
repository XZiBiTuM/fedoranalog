from django.db import models


class Article(models.Model):
    title_en = models.CharField(max_length=100, verbose_name='Название на английском', default='en')  # delete default
    title_cz = models.CharField(max_length=100, verbose_name='Название на чешском', default='cz')  # delete default
    content_cz = models.TextField(max_length=200, verbose_name='Краткий текст на чешском')
    content_en = models.TextField(max_length=200, verbose_name='Краткий текст на английском')
    img = models.ImageField(upload_to='articles/', null=True, blank=True, verbose_name='Изображение')
    pdf_cz = models.FileField(upload_to='pdf/', verbose_name='PDF Статья (чешский)', default='/')
    pdf_en = models.FileField(upload_to='pdf/', verbose_name='PDF Статья (английский)', default='/')
    reversed = models.BooleanField(default=False,
                                   verbose_name="Fasle-изображение слева, текст справа; True-изображение справа, "
                                                "текст слева")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title_en


class Emails(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Эл. почта')
    text = models.TextField(max_length=500, verbose_name='Текст обращения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата обращения')

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'{self.name} - {self.email}'
