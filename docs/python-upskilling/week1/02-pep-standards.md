# 2) PEP standards (PEP 8, naming, formatting, Pythonic code)

## Plain English
**PEP** = Python Enhancement Proposal (official suggestions).  
**PEP 8** = the style guide most teams follow.

## Why it matters
In Java, Checkstyle/Spotless keep code consistent. In Python, PEP 8 + formatters (Black/Ruff) do that job.

## Naming conventions
| Thing | Style | Example |
|-------|-------|---------|
| Variable / function | snake_case | `leave_balance` |
| Class | CapWords | `LeaveRequest` |
| Constant | UPPER_SNAKE | `MAX_DAYS` |
| Private-ish | leading `_` | `_internal_helper` |

## Formatting basics
- 4 spaces indentation (not tabs)
- Blank lines between functions/classes
- Imports usually at top
- Line length often ~88–100 chars (team choice)

## Pythonic means
Prefer clear code:
```python
# Good
if errors:
    return False

# Less Pythonic
if len(errors) > 0:
    return False
```

## Real scenario
Two FDEs edit the same agent code. If one uses `camelCase` and another `snake_case`, reviews become painful. PEP 8 keeps the team moving.

## Mini practice
Rename this to PEP 8 style: `def GetLeaveBalance(empId):`
