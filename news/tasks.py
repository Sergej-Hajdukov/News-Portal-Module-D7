from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_mail_for_sub_once(sub_username, sub_user_mail, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}. Новая статья в вашем разделе!',
        from_email='serha@yandex.ru',
        to=[sub_user_mail]
    )

    msg.attach_alternative(html_content, 'text/html')

    msg.send()


@shared_task
def send_mail_for_sub_every_week(sub_username, sub_user_mail, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}, новые статьи за прошлую неделю в вашем разделе!',
        from_email='serha@yandex.ru',
        to=[sub_user_mail]
    )

    msg.attach_alternative(html_content, 'text/html')

    msg.send()
