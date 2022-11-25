""" Pizza class definitions """

from typing import List
import abc
from abc import abstractmethod


class Pizza(abc.ABC):
    """
    Abstract base class for pizza classes
    """

    @staticmethod
    @abstractmethod
    def dict() -> List[str]:
        """
        Return the list of pizza ingredients

        :return: List of strs
        """
        pass

    def __repr__(self):
        return type(self).__name__ + ': ' + ', '.join(
            ingredient for ingredient in self.dict())


class Margherita(Pizza):
    @staticmethod
    def dict() -> List[str]:
        ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        return ingredients


class Pepperoni(Pizza):
    @staticmethod
    def dict() -> List[str]:
        ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        return ingredients


class Hawaiian(Pizza):
    @staticmethod
    def dict() -> List[str]:
        ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        return ingredients
