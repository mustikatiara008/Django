from django import forms


class KontakForm(forms.Form):
    nama_lengkap = forms.CharField()
    tanggal_lahir = forms.DateField()
    GENDER = [
        ('p', 'Pria'),
        ('w', 'Wanita'),
    ]
    jenis_kelamin = forms.ChoiceField(choices=GENDER)
    alamat = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()
