""" Cli interface """

from Pizza import Pizza, Margherita, Pepperoni, Hawaiian
import click
import random
from functools import wraps


def log(log_message=None, log_time=None) -> callable:
    """
    Parametrized decorator which prints log_message and log_time
    after function execution

    :param: log_message: if None prints function name
    :param: log_time: if None print randint from [0,100)
    :return: decorator object
    """

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            click.echo(log_message if log_message else
                       func.__name__, nl=False)
            click.echo(log_time if log_time else
                       random.randint(0, 100), nl=False)
            click.echo(' ', nl=False)
            click.echo('seconds')

        return wrapper

    return my_decorator


@log(log_time=10)
def bake(pizza: Pizza) -> None:
    """
    Bake pizza

    :param pizza: Pizza object
    :return: None
    """
    pass


@log(log_time=10)
def deliver(pizza: Pizza) -> None:
    """
    Deliver pizza

    :param: pizza: Pizza object
    :return: None
    """
    pass


@click.group()
def cli() -> None:
    """
    Interface to order pizza
    """
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_name', nargs=1)
def order(pizza_name: str, delivery: bool) -> None:
    """
    Create pizza and delivery it if delivery flag passed

    :param: pizza_name: string from {'margherita', 'pepperoni', 'hawaiian'}
    :param: delivery: include delivery in order

    :return: None
    """
    pizzas_dict = {
        'margherita': Margherita(), 'pepperoni': Pepperoni(),
        'hawaiian': Hawaiian()
    }

    if pizza_name not in pizzas_dict:
        click.echo('Sorry, only')
        click.echo(', '.join(pizzas_dict.keys()))
        click.echo('pizza available')
        return

    pizza = pizzas_dict[pizza_name]
    bake(pizza)
    if delivery:
        deliver(pizza)
    click.echo('Order is done')


@cli.command()
def menu() -> None:
    """
    Prints all pizzas

    :return: None
    """
    available_pizza = [Margherita(), Pepperoni(), Hawaiian()]
    click.echo('Available pizzas:')
    for pizza in available_pizza:
        click.echo(pizza)


if __name__ == '__main__':
    cli()
