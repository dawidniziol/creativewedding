from django.db import models

# Create your models here.


class Stage(models.Model):

    class Meta:
        db_table = "stage"
        verbose_name = "etap"
        verbose_name_plural = "etap"

    name = models.CharField(
        max_length=250,
        verbose_name="Etap",
        help_text="Etap produkcji",
        unique=True
    )

    def __str__(self):
        return self.name


class Order(models.Model):

    class Meta:
        db_table = "order"
        verbose_name = "zlecenie"
        verbose_name_plural = "zlecenie"

    name = models.CharField(
        max_length=250,
        verbose_name="Zlecenie",
        help_text="Nazwa zlecenia",
        unique=True
    )
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        verbose_name="Etap",
        help_text="Etap wykonania zlecenia",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Utworzony",
        help_text="Data dodania"
    )
    deadline = models.DateField(
        verbose_name="Deadline",
        help_text="Termin wykonania"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Opis",
        help_text="Szczegółowy opis zamówienia",
    )
    completed = models.BooleanField(
        verbose_name="Ukończony",
        default=False,
        help_text="Czy zlecenie zakończone",
    )

    def __str__(self):
        return self.name
