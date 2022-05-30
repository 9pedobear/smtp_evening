from django.shortcuts import render, redirect
from .forms import SMTPForm
from django.core.mail import send_mail
from django.contrib import messages


def smtpshka(request):
    if request.method == 'POST':
        form = SMTPForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['context'],
                '9pedobear@gmail.com',
                ['kayratsagynbekov@gmail.com'],
                fail_silently=False,
            )
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('/')
            else:
                messages.error(request, 'Письмо не отправленно')
    else:
        form = SMTPForm()
    return render(request, 'index.html', {'form': form})
