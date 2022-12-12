from django.shortcuts import render, redirect
from .models import KontakModel
from .forms import KontakForm


def KontakView(request):
    contact_form = KontakForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid:
            simpan_data = KontakModel.objects.create(
                nama_lengkap=contact_form.cleaned_data.get('nama_lengkap'),
                tanggal_lahir=contact_form.cleaned_data.get('tanggal_lahir'),
                jenis_kelamin=contact_form.cleaned_data.get('jenis_kelamin'),
                alamat=contact_form.cleaned_data.get('alamat'),
                agree=contact_form.cleaned_data.get('agree')
            )
            return redirect('Contact:kontakList')
    context = {
        'form_saya': contact_form
    }
    return render(request, 'contact_form.html', context)
