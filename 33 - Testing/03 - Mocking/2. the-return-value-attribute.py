from unittest.mock import Mock

mock = Mock(return_value=25)
print(mock)

print(mock())  # different mock object from mock
print(mock.return_value)  # the return of mock()

stuntman = Mock()
stuntman.jump_off_building.return_value = "Oh no, my leg"
stuntman.light_on_fire.return_value = "It burns!"

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())
