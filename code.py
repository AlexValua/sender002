from flask import Flask, request, render_template
import smtplib
from email.message import EmailMessage
from datetime import datetime
appFlask = Flask(__name__)
@appFlask.route('/', methods=['GET', 'POST'])
def form_example():
# handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        time = request.form.get('time')
        status = request.form.get('status')
        maintext = request.form.get('maintext')
        msg = EmailMessage()
        msg['Subject'] = f'Daily report : {time}'
        msg['From'] = 'Auto Result <autoresultVIMC@yandex.com>'
        msg['To'] = "piliposyan.narine@gmail.com"

        msg.set_content(f"Կատարող՝  {name}\n\n Կարգավիճակ՝   {status}\n\n Գործողություն՝   {maintext}")

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.yandex.com:465')
        server.login('autoresultVIMC@yandex.com', 'smtuzyxyflhlfbun')
        while True:
            now = datetime.now().time().strftime("%H:%M:%S")
            if now == "16:57:10":
                server.send_message(msg)
                server.quit()
                return 'Sent'
# otherwise handle the GET request
    return render_template("index.html")


if name == '__main__':
    appFlask.run(debug = True)