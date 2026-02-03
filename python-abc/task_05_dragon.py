#!/usr/bin/python3
"""Dragon class using mixins"""

class SwimMixin:
    """Provides swimming ability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly"""

    def roar(self):
        print("The dragon roars!")
