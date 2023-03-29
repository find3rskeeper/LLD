from observer import Observer

class SMSNotification(Observer):
    def __init__(self, observable) -> None:
        super().__init__()
        self.observable = observable

    def update(self):
        print('SMS notification sent', self.observable.test)