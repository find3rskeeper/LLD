from observer import Observer

class EmailNotification(Observer):
    def __init__(self, observable):
        super().__init__()
        self.observable = observable
    
    def update(self):
        print('Email Notification sent', self.observable.test)
