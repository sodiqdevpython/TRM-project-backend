from django.db import models

class OrganizationsType(models.TextChoices):
    maktabgacha = "Maktabgacha ta'lim", "Maktabgacha ta'lim"
    maktab = "Umumiy o'rta ta'lim maktablari", "Umumiy o'rta ta'lim maktablari"
    musiqa_maktab = "Musiqa maktablari", "Musiqa maktablari"
    sport_maktab = "Sport maktablari","Sport maktablari"

class OrganizationsRatingType(models.TextChoices):
    red = "Qoniqarsiz", "Qoniqarsiz"
    yellow = "O'rtacha", "O'rtacha"
    green = "Yaxshi", "Yaxshi"

class MeasureType(models.TextChoices):
    piece = "dona", "dona"
    couple = "juftlik", "juftlik"
    collection = "to'plam", "to'plam"

class EquipmentType(models.TextChoices):
    tool = "Asbob uskunalar", "Asbob uskunalar"
    equipment = "Jihozlar", "Jihozlar"

class AvilableType(models.TextChoices):
    avilable = "Soz", "Soz"
    invalid = "Nosoz", "Nosoz"
    not_avilable = "Yaroqsiz", "Yaroqsiz"