# Week3.8) Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("hr")

log.debug("detail")
log.info("started")
log.warning("slow query")
log.error("failed")
log.critical("down")
```

## File logging
```python
logging.basicConfig(filename="app.log", level=logging.INFO)
```

## Why not only print?
Logs have levels, timestamps, and can go to files/aggregators in production.

## Real scenario
In an FDE deployment, logs prove whether leave submit failed due to validation or DB.

## Mini practice
Log an info message when a function starts and an error when input is invalid.
