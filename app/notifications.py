from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .schemas import AppointmentOut

conf = ConnectionConfig(
    MAIL_USERNAME="seu@mail.com",
    MAIL_PASSWORD="senha",
    MAIL_FROM="seu@mail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True, MAIL_SSL=False,
)

async def send_reminder_email(background_tasks: BackgroundTasks, appointment: AppointmentOut):
    html = f"<p>Olá, lembrete: você tem <b>{appointment.title}</b> em {appointment.start}.</p>"
    message = MessageSchema(subject="🔔 Lembrete de Agendamento",
                             recipients=[appointment.owner.email],
                             body=html, subtype="html")
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
