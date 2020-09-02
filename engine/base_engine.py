from abc import ABC, abstractmethod

class BaseEngine(ABC):
    @abstractmethod
    def encrypt(self, data):
        """Encrypt data"""
        pass

    @abstractmethod
    def decrypt(self, data, key):
        """Decrypt data"""
        pass

    @abstractmethod
    def get_capabilities(self):
        """Get engine capabilities"""
        pass
    