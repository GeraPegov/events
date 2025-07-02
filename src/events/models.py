from django.db import models


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название площадки")


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название мероприятия")
    date = models.DateTimeField(
        verbose_name="Дата проведения мероприятия",
    )
    status = models.CharField(
        max_length=100, verbose_name="Текущий статус", default="open"
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)
