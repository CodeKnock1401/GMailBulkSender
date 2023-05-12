import csv
import logging

from googleapiclient.errors import HttpError

from send_message import format_and_send_message

USERS_CSV_PATH = "/Users/parsa/Documents/Uni/Fall 1401/CodeKnock/Registrations/SecondRound/Registrations_Final.csv"
# USERS_CSV_PATH = "/Users/parsa/Library/Application Support/JetBrains/PyCharmCE2023.1/scratches/s.json"


def send_mail(*, subject, template_path):
    message_template = open(template_path, "r").read()
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)

    logging.info(f"users file: {USERS_CSV_PATH}")
    print(f"users file: {USERS_CSV_PATH}")

    with open(USERS_CSV_PATH, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header, *rows = [line for line in csv_reader]

    print(message_template.format(**dict(zip(header, rows[0]))))
    confirmation = input("is the sample formatted correctly? (y/N) ")
    if confirmation.lower() != "y":
        exit(1)

    for row in rows:
        info = dict(zip(header, row))
        to = info["email"]
        subject = subject
        body = message_template.format(**info)
        logging.info(f"sending to {to}")
        try:
            format_and_send_message(to, subject, body)
        except HttpError:
            logging.error(f"failed sending to {to}")

    print(f"sent {len(rows)} messages.")
    exit(0)
