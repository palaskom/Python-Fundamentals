from unittest.mock import Mock
from random import randint


def generate_number():
    return randint(1, 10)


# side_effect wins over the return_value
# every time we invoke our mock, the
# generate_number will be called
call_me_maybe = Mock(return_value=10, side_effect=generate_number)
print(call_me_maybe())

three_item_list = Mock()
three_item_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]
print(three_item_list.pop())  # 3
print(three_item_list.pop())  # 2
print(three_item_list.pop())  # 1
# print(three_item_list.pop())  # IndexError: pop from empty list

mock = Mock(side_effect=NameError("Some error message"))
mock()  # NameError: Some error message
