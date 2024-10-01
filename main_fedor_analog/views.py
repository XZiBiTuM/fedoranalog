import json
from .forms import *
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
import urllib.parse
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(emails):
    print('started')
    sender = 'ivanbalanar323@gmail.com'
    sender_pass = 'kmps tlnz qnru bfbf'
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)

    server.starttls()

    server.login(sender, sender_pass)

    to_email = 'ffedorchuk@seznam.cz'
    #to_email = 'balayi323161@mail.ru'
    
    user_name = emails.name
    user_email = emails.email
    user_message_text = emails.text
    
    subject = "A request from the user"
    message = "***FedorAnalog***<br>"
    message += f"Username: {user_name}<br>"
    message += f"Email: {user_email}<br>"
    message += f"Text: {user_message_text}<br><br><br><br>"
    message += "Powered by XZiBiTuM<br>"
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    server.sendmail(sender, to_email, msg.as_string())

    server.quit()
    

def set_language(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_language = data.get('language', 'en')
        request.session['selected_language'] = selected_language
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


def main(request):
    selected_language = request.session.get('selected_language', 'en')
    articles = Article.objects.all()

    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            user_message_text = form.cleaned_data['text']

            emails = type('EmailData', (object,), {
                'name': user_name,
                'email': user_email,
                'text': user_message_text
            })()

            send_mail(emails)  # Передаем объект в функцию отправки письма

            form.save()
            return redirect('success')
    else:
        form = QuestForm()

    context = {
        'articles': articles,
        'selected_language': selected_language,
        'form': form,
    }
    return render(request, 'main.html', context)


def what_do_i_do(request):
    selected_language = request.session.get('selected_language', 'en')
    context = {
        'selected_language': selected_language,
    }
    return render(request, 'what_do_i_do.html', context)


def success_view(request):
    selected_language = request.session.get('selected_language', 'en')
    context = {
        'selected_language': selected_language,
    }
    return render(request, 'success.html', context)


def page_not_found(request):
    selected_language = request.session.get('selected_language', 'en')
    context = {
        'selected_language': selected_language,
    }
    return render(request, '404.html', context)
