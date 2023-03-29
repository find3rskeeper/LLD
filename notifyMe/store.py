from iphoneObservable import IphoneObservable
from emailNotification import EmailNotification
from smsNotification import SMSNotification

iphoneOb = IphoneObservable()
emailNotifObj = EmailNotification(iphoneOb)
SMSNotifiObj = SMSNotification(iphoneOb)
iphoneOb.add(emailNotifObj)
iphoneOb.add(SMSNotifiObj)
iphoneOb.notify()