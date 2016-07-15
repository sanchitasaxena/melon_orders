"""This file should have our order classes in it."""

#establish parent class
class AbstractMelonOrder(object):
    #parent method to be called initiating the program and accepting the arguements
    def __init__(self, species, qty, shipped, order_type, tax):
    #defining the parent attributes and methods to be accessible to the child class
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.get_total()
        self.marked_shipped()


    def get_total(self, tax, qty, base_price = 5):
        print base_price
        if self.species == "Christmas":
            base_price = base_price * 1.5
            print "I'm a xmas melon", base_price
        total = (1 + self.tax) * self.qty * base_price
        return total

    def marked_shipped(self, shipped):
        self.shipped = True
        print self.shipped




class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, order_type, tax):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__("domestic", 0.08)

    def get_total(self):
        """Calculate price."""
        return super(DomesticMelonOrder, self).get_total(0.08)

    def mark_shipped(self):
        """Set shipped to true."""
        return super(DomesticMelonOrder, self).marked_shipped(True)




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    self.country_code = country_code
    self.get_country_code()

    def __init__(self, order_type, country_code, tax):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__("international", country_code, 0.12)

    def get_total(self):
        """Calculate price."""
        return super(InternationalMelonOrder, self).get_total(0.12)

    def mark_shipped(self):
        """Set shipped to true."""
        return super(InternationalMelonOrder, self).mark_shipped(True)

    def get_country_code(self, country_code):
        """Return the country code."""
        return self.country_code
