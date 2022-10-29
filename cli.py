""" Cli interface """

from Pizza import Pizza, Margherita, Pepperoni, Hawaiian
import click
import random


def log(log_message=None, log_time=None) -> callable:
    """
    Parametrized decorator which prints log_message and log_time
    after function execution

    :param log_message: if None prints function name
    :param log_time: if None print randint from [0,100)
    :return: decorator object
    """

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(log_message if log_message else func.__name__, end=' ')
            print(log_time if log_time else random.randint(0, 100), 'seconds')

        return wrapper

    return my_decorator


@log()
def bake(pizza: Pizza) -> None:
    """
    Bake pizza

    :param pizza: Pizza object
    :return: None
    """
    pass


@log('Deliver time -', 50)
def deliver(pizza: Pizza) -> None:
    """
    Deliver pizza

    :param pizza: Pizza object
    :return: None
    """
    pass


@click.group()
def cli() -> None:
    """
    Define click group

    :return: None
    """
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool) -> None:
    """
    Create pizza and delivery it if delivery flag passed
    :param pizza_name: string from {'margherita', 'pepperoni', 'hawaiian'}
    :param delivery: include delivery in order

    :return: None
    """
    pizzas_dict = {
        'margherita': Margherita(), 'pepperoni': Pepperoni(), 'hawaiian': Hawaiian()
    }

    if pizza_name not in pizzas_dict:
        print('Sorry, only')
        print(*(pizza for pizza in pizzas_dict.keys()), sep=', ')
        print('pizza available')
        return

    pizza = pizzas_dict[pizza_name]
    bake(pizza)
    if delivery:
        deliver(pizza)
    print('Order is done')


@cli.command()
def menu() -> None:
    """
    Prints all pizzas

    :return: None
    """
    available_pizza = [Margherita(), Pepperoni(), Hawaiian()]
    print('Available pizzas:')
    for pizza in available_pizza:
        print(pizza)


if __name__ == '__main__':
    cli()
