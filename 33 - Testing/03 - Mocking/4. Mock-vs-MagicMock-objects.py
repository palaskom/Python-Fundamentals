from unittest.mock import Mock, MagicMock

plain_mock = Mock()  # does not support magic methods
magic_mock = MagicMock()  # returns default values for its magic methods

# Mock() does not have dunder methods (e.g., __len__())
# print(len(plain_mock))  # TypeError: object of type 'Mock' has no len()
print(len(magic_mock))  # 0

# print(plain_mock[3])  # TypeError: 'Mock' object is not subscriptable
print(magic_mock[3])  # new mock object mock.__getitem__()
print(magic_mock["hello"])

magic_mock.__len__.return_value = 50
print(len(magic_mock))  # 50

# by default is truthy
if magic_mock:
    print("hello")

magic_mock.__bool__.return_value = False
if magic_mock:
    print("goodbye")

magic_mock.__getitem__.return_value = 100
print(magic_mock[3])  # 100
print(magic_mock[100])  # 100
print(magic_mock["hello"])  # 100
