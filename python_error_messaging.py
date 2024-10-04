### Example Code Without Error Message

### Initial Code:
def divide_numbers(numerator, divisor):
    return numerator / divisor

def main():
    result = divide_numbers(10, 0)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

# Can you use Copilot to explain the error message that you should add before you run this code?
# In this code, the `divide_numbers` function performs a division operation. However, it does
# not handle the case where the `divisor` is zero, which will cause a `ZeroDivisionError` at runtime.

# Use Copilot to generate the error message that you should add to the code to handle this case.
def divide_numbers(numerator, divisor):
    if divisor == 0:
        raise ValueError("Error: Divisor cannot be zero.")
    return numerator / divisor

def main():
    try:
        result = divide_numbers(10, 0)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()