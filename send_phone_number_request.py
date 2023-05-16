from send_bulk_message import send_mail

send_mail(
    subject="شماره موبایل اعضای تیم",
    template_path="message_templates/phone_number_request.html")
