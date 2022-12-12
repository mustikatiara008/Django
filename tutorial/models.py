from django.db import models

# Create your models here.


class KontakModel(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    GENDER = [
        ('p', 'Pria'),
        ('w', 'Wanita'),
    ]
    jenis_kelamin = models.CharField(choices=GENDER, max_length=10)
    alamat = models.TextField()
    agree = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_lengkap
