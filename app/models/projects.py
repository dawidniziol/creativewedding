from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


def request_upload_path(instance, filename) -> str:

    return f"media/{instance.name}/{filename}"


class RequestStatus(models.TextChoices):
    """Text choices model for Schedule communication type"""

    INTERNET = "INTERNET", _("Z Internetu")
    OFFICE = "OFFICE", _("Z Pracowni")
    EXHIBITION = "EXHIBITION", _("Z Targów")


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
    description = models.TextField(
        blank=True,
        verbose_name="Opis",
        help_text="Szczegółowy opis zamówienia",
    )
    email = models.EmailField(
        verbose_name="adres email",
        help_text="Adres email",
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name="nr telefonu",
        help_text="Kontaktowy nr telefonu w formacie 123456789",
        validators=[RegexValidator(regex=r'^\d{9,15}$')],
        max_length=9,
        blank=True,
        null=True
    )
    source = models.CharField(
        max_length=100,
        verbose_name="Źródło",
        help_text="Źródło",
        choices=RequestStatus.choices,
        null=True,
        blank=True
    )
    stage = models.ForeignKey(
        Stage,
        on_delete=models.SET_NULL,
        verbose_name="Etap",
        help_text="Etap wykonania zlecenia",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Utworzony",
        help_text="Data dodania"
    )
    file = models.FileField(
        upload_to=request_upload_path,
        null=True,
        blank=True,
        verbose_name="Pliki",
        help_text="Pliki",
    )
    deadline_invitations = models.DateField(
        verbose_name="Deadline zaproszenia",
        help_text="Deadline zaproszenia",
        null=True,
        blank=True
    )
    completed_invitations = models.BooleanField(
        verbose_name="Ukończone zaproszenia",
        default=False,
        help_text="Ukończone zaproszenia",
    )
    angels_extras = models.BooleanField(
        verbose_name="Anioły",
        default=False,
        help_text="Anioły",
    )
    deadline_extras = models.DateField(
        verbose_name="Deadline dodatki",
        help_text="Deadline dodatki",
        null=True,
        blank=True
    )
    completed_extras = models.BooleanField(
        verbose_name="Ukończone dodatki",
        default=False,
        help_text="Ukończone dodatki",
    )

    def __str__(self):
        return self.name


class Offers(models.Model):

    class Meta:
        db_table = "offer"
        verbose_name = "zapytanie"
        verbose_name_plural = "zapytanie"

    name = models.CharField(
        max_length=250,
        verbose_name="Zapytanie",
        help_text="Nazwa zapytania",
        unique=True
    )
    description = models.TextField(
        blank=True,
        verbose_name="Opis",
        help_text="Szczegółowy opis zamówienia",
    )
    email = models.EmailField(
        verbose_name="adres email",
        help_text="Adres email",
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name="nr telefonu",
        help_text="Kontaktowy nr telefonu w formacie 123456789",
        validators=[RegexValidator(regex=r'^\d{9,15}$')],
        max_length=9,
        blank=True,
        null=True
    )
    samples = models.BooleanField(
        verbose_name="Próbki",
        default=False,
        help_text="Próbki",
    )
    forms = models.BooleanField(
        verbose_name="Zapytanie z formularza",
        default=False,
        help_text="Zapytanie z formularza",
    )
