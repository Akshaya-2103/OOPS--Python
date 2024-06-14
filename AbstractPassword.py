from abc import ABC, abstractmethod

class AbstractPassword(ABC):
    def __init__(self, original_password, attempts):
        self.original_password = "Akshaya123"
        self.attempts = 3

    @abstractmethod
    def authentication(self):
        pass