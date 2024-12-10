from unittest.mock import MagicMock


class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1


# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)
class_mock = MagicMock(spec=BurritoBowl)
print(class_mock.restaurant_name)
print(class_mock.steak_special())
# print(class_mock.chicken_special())  # AttributeError: Mock object has no attribute 'chicken_special'

instance_mock = MagicMock(spec=BurritoBowl.steak_special())
print(instance_mock.protein)
print(instance_mock.rice)
print(instance_mock.guacamole_portions)
instance_mock.add_guac()
print(instance_mock.guacamole_portions)
# print(instance_mock.add_cheese())  # AttributeError: Mock object has no attribute 'add_cheese'
# print(instance_mock.beans)  # AttributeError: Mock object has no attribute 'add_cheese'
instance_mock.beans = True
print(instance_mock.beans)

instance_strict_mock = MagicMock(spec_set=BurritoBowl.steak_special())
print(instance_strict_mock.protein)
instance_strict_mock.add_guac()
print(instance_strict_mock.guacamole_portions)
# instance_strict_mock.beans = True  # AttributeError: Mock object has no attribute 'beans'
