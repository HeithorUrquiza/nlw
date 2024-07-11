import smtplib
from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs: List, body: str) -> None:
    from_addr = "gfo5kigimwraqj5a@ethereal.email"
    login = "gfo5kigimwraqj5a@ethereal.email"
    password = "Wnt4vbSH9XM1ue1DFf"
    
    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ', '.join(to_addrs)
    msg["Subject"] = "Confirmação de Viagem !!"
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    
    for email in to_addrs:
        server.sendmail(from_addr, email, text)
        
    server.quit()