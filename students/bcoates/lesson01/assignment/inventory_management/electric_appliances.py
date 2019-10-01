""" This module defines the Electric Appliances class """

# pylint: disable=too-many-arguments, too-few-public-methods

from inventory import Inventory

class ElectricAppliances(Inventory):
    """ Defines the ElectricAppliances class """

    def __init__(self, product_code, description, market_price, rental_price, brand, voltage):
        """ Creates common instance variables from the parent class """
        Inventory.__init__(self, product_code, description, market_price, rental_price)

        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """ Returns a dictionary object """

        output_dict = Inventory.return_as_dictionary(self)
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
