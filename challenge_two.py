""" DESCRIPTION
You as a developer are tasked to create an application for a restaurant.
The application should take care of the available meals, their price and taxes.
The restaurant can have different type of offers like daily menu, weekend menu or happy hour.
The manager of the restaurant should be able to see detailed information about the items sold, like item cost, tax, quantity, etc.

Using the objected oriented language of your choice; design an OBJECT MODEL for this application that:

- Allows managing orders: order meals, drinks, menus, mark orders as payed, generate bills, etc.
- Provides realtime control of the stock: when the restaurant runs out of a specific meal, refill stock, etc.
- Provides aggregated data (i.e. weekly) of the restaurant accountability: aggregated revenue, costs, Taxes, offers ratio, etc.
- Provides access to different devices to the system.

Try to be as detailed as possible with each requirement. Requirements are presented by priority. Make sure you've got a good design for one of the requirements before starting with the next one. We'd rather see 2 points well designed than the 4 but not complete. Please focus on the SW design rather than the high level architecture, but if you feel like (and have time), a small description of your architecture proposal will be welcome.

Have fun!
"""

# Design is based on DDD (Domain Driven Design)
# First requirement is modeled with Order, OrderItem, Item and the subclasses associated.
# The class OrderManagement coordinate the use cases (create order, pay order, search orders, etc...).
# Second requirement is based on quantity property of Item model. When the order is payed, the system checks
# if there is stock available (the stock is not below a threshold). The application could make a electronic
# request to the provider.
#
# NOTE: I use python 3.7 data clases new feature

import typing
from datetime import datetime
from decimal import Decimal
from enum import Enum


class OrderError(Exception):
    pass


class Unit(Enum):
    LITRES = 1
    KILOGRAMS = 2


class Period(Enum):
    DAILY = 1
    WEEKEND = 2
    HAPPY_HOUR = 3


class Status(Enum):
    CREATED = 1
    PAYED = 2
    BILL_GENERATED = 3


@dataclass
class Item:
    """Base class to handle common info to each item.
       This class and the subclasses are Value Objets in DDD terminology
    """
    name: str
    description: str
    quantity: int
    quantity_threshold: int
    unit_price: Decimal
    provider_price: Decimal
    unit_taxes: Decimal
    unit_of_measure: Unit

    def has_stock(self, quantity):
        """Each subclass muss define what is stock. By default, the quantity.
        """
        return self.quantity >= quantity

    def update_stock(self, quantity):
        """Update the stock. If the design is based on an event system (like kafka).
           We could publish a message to the system responsible of the stock when the stock
           is below a threshold.
        """


class Menu(Item):
    period: Period
    courses: []


class Meal(Item):
    pass


class Drink(Item):
    pass


@dataclass
class OrderItem:
    """This class is an Entity in DDD terminology.
    """
    item: Item
    quantity: int
    total_price: Decimal
    total_taxes: Decimal

    def calculate_total(self):
        # I want a snapshot for the numeric data because the unit price and taxes
        # could be change in time and the order was made with a specific price.
        self.total_price = quantity * item.unit_price
        self.total_taxes = quantity * item.unit_taxes


@dataclass
class Order:
    """This class acts as an Aggregate in DDD terminology.
    """
    id: long
    status: Status
    requested: datetime
    created: datetime
    payed: datetime
    items: List[OrderItem]


def authorized(func):
    """Basic authorization decorator
    """
    def decorator(*args, **kwargs):
        # get user profile. User is always in args[0]
        # check if user profile can performs the operation
        # raise AuthError if cann't
        return func(*args, **kwargs)
    return decorator


class OrderManager:
    """Implements command pattern. It's the api to the UI, report system, etc...
    """
    @authorized
    def create(self, user, order_items: List[OrderItem]) -> long:
        """Create a new order.

        :param order_items: a list with the info introduced by the client or the operator
        :returns: the id of the order
        :raises OrderError: Validation error
        """
        for item in order_items:
            pass
            # Make validations. Stock available, at least 1 order item, etc...
            # Raise errors when the items are invalid
            # In the same transaction save the info asociated to each OrderItem and
            # set status to CREATED

    @authorized
    def pay(self, user, order_id: long):
        """Makes the pay of the order.

        :param order_id: The id of the order to be payed
        :raises OrderError: Validation errors
        """
        # Make validations. Order exists, order status is CREATED, credit card is valid, etc...
        # set status to PAYED
        # Update items stock. Another process will lauch an alarm when stock is too low

    @authorized
    def generate_bill(self, user, order_id: long):
        """Generate the bill.

        :param order_id: The id of the order to be payed
        :raises OrderError: Validation errors
        """
        # Make validations. Order exists, order status is PAYED, etc...
        # set status to BILL_GENERATED

    @authorized
    def get(self, user, order_id: long) -> Order:
        """Get info about a specific order

        :param order_id: unique id of the order
        :returns: A order object
        :raises OrderError: When the order doesn't exist
        """

    @authorized
    def search(self, user, *args, **args) -> List[Order]:
        """Search all orders that match the passes criteria
        """
