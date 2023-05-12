def format_subject(subject: str):
    return f"کدناک ۱۴۰۱ - {subject}"


def get_header():
    return open("message_templates/header.html", "r").read()


def get_footer():
    return open("message_templates/footer.html", "r").read()


def format_body(body: str):
    return get_header() + body + get_footer()
