from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def press(self):
        pass
