import os
import math
import datetime
from pathlib import Path
from functools import reduce

# 1. Get "main:app" from a file path
get_app_string = lambda f: os.path.splitext(os.path.basename(f))[0] + ":app"

# 2. Get file extension
get_ext = lambda f: os.path.splitext(f)[1]

# 3. Get filename without extension
get_filename = lambda f: os.path.splitext(os.path.basename(f))[0]

# 4. Flatten a nested list
flatten = lambda l: [item for sublist in l for item in sublist]

# 5. Count items in a list using a dictionary
count_items = lambda l: {i: l.count(i) for i in set(l)}

# 6. Check if a number is prime (simple check)
is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

# 7. Compute factorial
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# 8. Calculate nth Fibonacci number
fibonacci = lambda n: n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# 9. Reverse a string
reverse_str = lambda s: s[::-1]

# 10. Check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]

# 11. Get current timestamp string
now_str = lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 12. Add days to today’s date
add_days = lambda d: (datetime.datetime.now() + datetime.timedelta(days=d)).date()

# 13. Safe divide
safe_div = lambda a, b: a / b if b else None

# 14. List intersection
intersect = lambda a, b: list(set(a) & set(b))

# 15. Flatten and deduplicate a list of lists
flat_unique = lambda l: list(set(flatten(l)))

# 16. Convert list of tuples to dict
tuples_to_dict = lambda t: dict(t)

# 17. Convert dict to list of tuples
dict_to_tuples = lambda d: list(d.items())

# 18. Compose two functions
compose = lambda f, g: lambda x: f(g(x))

# 19. Sum of squares
sum_squares = lambda l: sum(x ** 2 for x in l)

# 20. Deep get from nested dict (with default)
deep_get = lambda d, keys, default=None: reduce(lambda c, k: c.get(k) if isinstance(c, dict) else default, keys, d)

# 21. Get file size in KB
file_size_kb = lambda f: round(Path(f).stat().st_size / 1024, 2) if Path(f).exists() else None

# Sample usage for testing (comment or remove in actual use)
if __name__ == "__main__":
    print(get_app_string(__file__))
    print(flatten([[1, 2], [3, 4]]))
    print(is_prime(13))
    print(reverse_str("hello"))
    print(now_str())
    print(add_days(5))
    print(safe_div(10, 0))
    print(intersect([1, 2, 3], [2, 3, 4]))
    print(sum_squares([1, 2, 3]))
    nested = {"a": {"b": {"c": 42}}}
    print(deep_get(nested, ["a", "b", "c"]))
