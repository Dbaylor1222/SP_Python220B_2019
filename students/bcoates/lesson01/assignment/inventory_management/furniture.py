""" This Module defines the Furniture class """

# pylint: disable=too-many-arguments, too-few-public-methods

from inventory import Inventory

class Furniture(Inventory):
    """ Defines Furniture """

    def __init__(self, product_code, description, market_price, rental_price, material, size):
        """ Creates common instance variables from the parent class """

        Inventory.__init__(self, product_code, description, market_price, rental_price)

        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """ Returns a dictionary object with furniture details """

        output_dict = Inventory.return_as_dictionary(self)
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
