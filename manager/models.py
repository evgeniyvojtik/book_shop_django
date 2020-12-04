from django.db import models

class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(
        max_length=50,
        verbose_name='название',
        help_text='Нуэто тип погоняло книги'
    )

    date = models.DateTimeField(null=True)
    text = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return f"{self.title} ~ {self.id}"

class Comment(models.Model):
    text = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
