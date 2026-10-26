"""Q3(d): same loop, fourth channel added. Run: python main_with_push.py"""
from channels import Sms, Email, WhatsApp, send_all
from push_notification import PushNotification

channels = [Sms(), Email(), WhatsApp(), PushNotification()]
send_all(channels, "Exam moved to Friday")
