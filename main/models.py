from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
class Profil(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField(validators=[MinValueValidator(7), MaxValueValidator(60)], default=25)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'

class Kurs(models.Model):
    nom = models.CharField(max_length=255)
    daraja = models.CharField(max_length = 50,choices=(('Junior','Junior'),('Senior','Senior'),('Staff','Staff')))
    Ustoz = models.CharField(max_length = 50,choices=(('Otabek','Otabek'),('Abbos','Abbos')))
    narx = models.CharField(max_length=50)
    chegirma_narx = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    matn = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    baho = models.IntegerField()

    def __str__(self):
        return f"Izoh: {self.baho} - {self.profil} uchun {self.kurs}"


    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class Tanlangan(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profil} tomonidan tanlangan {self.kurs}"

    class Meta:
        verbose_name = 'Tanlangan'
        verbose_name_plural = 'Tanlanganlar'


class Xarid(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    holat = models.CharField(max_length=50)
    summasi=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.profil} tomonidan xarid qilingan {self.kurs} ({self.holat})"

    class Meta:
        verbose_name = 'Xarid'
        verbose_name_plural = 'Xaridlar'













