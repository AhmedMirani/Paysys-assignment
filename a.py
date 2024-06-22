def process_numbers(a, b):
    if a==0:
        return 0 # deliberate change to show pipeline in action
    if a <= 0 or b <= 0:
        return "Error"
    elif a + b > 100:
        return a + b
    elif a + b == 100:
        return a * b
    else:
        return abs(a - b)
