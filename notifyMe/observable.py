from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def add(self, Observable):
        pass

    def remove(self, Observable):
        pass

    @abstractmethod
    def notify(self):
        pass

    def setData(self):
        pass