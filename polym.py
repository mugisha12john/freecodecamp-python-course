class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example1.__dict__)