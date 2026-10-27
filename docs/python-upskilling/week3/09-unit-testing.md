# Week3.9) Unit testing

```python
import unittest
from unittest.mock import patch

def add(a, b):
    return a + b

class AddTests(unittest.TestCase):
    def setUp(self):
        self.a = 2

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(add(self.a, 3), 5)

    def test_error(self):
        with self.assertRaises(TypeError):
            add("2", 3)

if __name__ == "__main__":
    unittest.main()
```

## Mocking / patching
Replace external calls in tests so tests stay fast and offline.

## Real scenario
Test leave eligibility rules without a real database.

## Mini practice
Write a unittest for a function `is_even(n)`.
