### First setup
1. Create a new Google Cloud project [here](https://console.cloud.google.com/projectcreate).
2. [Enable](https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com) the Gmail API for the project.
3. Complete the steps for [configuring the OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent). Add the email address you want to send from as a test user.
4. Go to [here](https://console.cloud.google.com/apis/credentials), click Create Credentials -> OAuth client ID. Select "Desktop app" for Application type, choose a name and click Create.
5. Click OK, a file will be downloaded. Move the file next to the program and rename it to `credentials.json`.
6. Install dependencies using `python3 -m pip install -r requirements.txt`.
7. Edit config.py and set the `from_address` properly.

Edit `message_templates/header.html` and `message_templates/header.html` to match your preferences.

### Usage
Prepare a CSV file with a header row. It has to have a column named `email`.

Create a html template in `message_templates` for each batch of messages you want to send. In the template, you can use field names from the CSV inside curly braces(`{}`). See the existing files for examples.

Then, invoke `send_bulk_message.send_mail(subject, template_path, users_file, verify=True)` to send the mail. If `verify` is `True`, the program shows a preview and waits for confirmation before sending the bulk emails.