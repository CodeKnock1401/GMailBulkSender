from send_bulk_message import send_mail

send_mail(
    subject="تاییدیه‌ی ثبت‌نام",
    template_path="message_templates/registration_confirmation.html")
