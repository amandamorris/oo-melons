"""This file should have our order classes in it."""


class MelonOrder(object):
    """Base class for melon order"""

    def __init__(self, species, qty, order_type, tax, country_code="USA"):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(MelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)
        # self.order_type = "domestic"
#        self.tax = 0.08


class InternationalMelonOrder(MelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species,
                                                      qty,
                                                      "international",
                                                      0.17,
                                                      country_code)
        # self.order_type = "international"
        # self.tax = 0.17

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(MelonOrder):
    """ Melon orders for the goverment"""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species,
                                                      qty,
                                                      "domestic",
                                                      0.0)
        self.passed_inspection = False

    def mark_inspection(self, is_passed):
        self.passed_inspection = is_passed
