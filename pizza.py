""" Pizza class definitions """

from typing import List


class Pizza:
    """
    Base class for pizza classes
    """

    def dict(self) -> List[str]:
        """
        Return the list of pizza ingredients

        :return: List of strs
        """
        return self.ingredients

    def __repr__(self):
        return f'{self.__class__.__name__}: ' + ', '.join(
            ingredient for ingredient in self.dict())


class Margherita(Pizza):
    ingredients = {'tomato sauce': 2, 'mozzarella': 3, 'tomatoes': 5}


class Pepperoni(Pizza):
    ingredients = {'tomato sauce': 5, 'mozzarella': 3, 'pepperoni': 10}


class Hawaiian(Pizza):
    ingredients = {'tomato sauce': 1, 'mozzarella': 2, 'chicken': 5, 'pineapples': 5}
