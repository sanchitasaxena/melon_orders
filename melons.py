"""This file should have our order classes in it."""

#establish parent class
class AbstractMelonOrder(object):
    shipped = False
    #parent method to be called initiating the program and accepting the arguements
    def __init__(self, species, qty, order_type, tax, country_code, base_price=5):
    #defining the parent attributes and methods to be accessible to the child class
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.base_price = base_price
        self.country_code = country_code
        self.get_total()
        self.marked_shipped()


    def get_total(self):
        # if self.species == "Christmas":
        #     base_price = base_price * 1.5
        #     print "I'm a xmas melon", base_price
        total = (1 + self.tax) * self.qty * self.base_price
        return total


    def marked_shipped(self):
        self.shipped = True
        print self.shipped, "I'm shipped"





class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08
    order_type = "Domestic"
    country_code = "US"


class InternationalMelonOrder(AbstractMelonOrder, country_code):
    """An international (non-US) melon order."""
    tax = 0.12
    order_type = "International"
    self.get_country_code()
    
    def get_country_code(self):
        """Return the country code."""
        return self.country_code
