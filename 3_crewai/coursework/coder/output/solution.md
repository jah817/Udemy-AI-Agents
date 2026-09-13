I wrote a Python program in the sandbox to compute the first 1,000,000 terms of the series

1 - 1/3 + 1/5 - 1/7 + ...

and multiply the sum by 4.

The file created was:

```python
def calculate_pi_series(terms: int = 1_000_000) -> float:
    total = 0.0
    sign = 1.0

    for i in range(terms):
        denominator = 2 * i + 1
        total += sign / denominator
        sign = -sign

    return 4 * total


if __name__ == "__main__":
    result = calculate_pi_series()
    print(result)
```

I ran it, and the output was:

```text
3.1415916535897743
```