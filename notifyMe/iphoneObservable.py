from observable import Observable

class IphoneObservable(Observable):
    def __init__(self):
        super().__init__()
        self.observers = []
        self.test = 1
    
    def add(self, observable):
        self.observers.append(observable)
    
    # def remove(self, observable):
    #     if observable not in self.observables:
    #         self.observables.remove(observable)

    def notify(self):
        for observer in self.observers:
            observer.update()