"""Q3(b): send through all three channels. Run: python main.py"""
from channels import Sms, Email, WhatsApp, send_all

channels = [Sms(), Email(), WhatsApp()]
send_all(channels, "Exam moved to Friday")
