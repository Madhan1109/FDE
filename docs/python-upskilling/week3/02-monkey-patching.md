# Week3.2) Monkey patching

## Plain English
Changing code behavior at runtime by replacing functions/attributes.

```python
import math
math.sqrt = lambda x: "nope"  # dangerous demo
```

## Useful in testing
```python
from unittest.mock import patch

with patch("payments.charge", return_value="OK"):
    ...
```

## Risks
- Hard to debug
- Breaks assumptions
Prefer dependency injection over random patching in production.

## Real scenario
In tests, patch external SMS API so CI does not send real messages.

## Mini practice
Explain one safe use and one unsafe use of monkey patching.
