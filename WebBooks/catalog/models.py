from django.db import models


class MyModelName(models.Model):
    """
    Класс, определякхций модель, производный от класса Model
    """
    # Поле (множество полей)
    my_field_name = models.CharField(max_length=20, help_text='Не более 20 символов')

    # Метаданные
    class Meta:
        ordering = ["-my_field_name"]

    def get_absolute_url(self):
        # Возвращает url-aдpec для доступа к экземпляру MyModelName
            return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        # Строка для представления объекта MyModelName в Admin site
            return self.field_name
