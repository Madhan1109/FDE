# Week2.8) Descriptors

## Plain English
Descriptors let you customize get/set/delete of attributes. `property` is the friendly form.

```python
class Celsius:
    def __init__(self, value=0):
        self._value = value

    def __get__(self, obj, objtype=None):
        return self._value

    def __set__(self, obj, value):
        if value < -273:
            raise ValueError("too cold")
        self._value = value

class Temperature:
    celsius = Celsius()
```

## property shorthand
```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("invalid")
        self._salary = value
```

## Real scenario
Validate leave days whenever someone sets `request.days = -1`.

## Mini practice
Create a property `age` that rejects negative values.
