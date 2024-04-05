"""Function for fibonacci calculation"""

def generate_fibonacci(loop_length):
    if loop_length <= 0:
        return 0
    if loop_length == 1:
        return 1

    prev_number, current_number = 0, 1

    for _ in range(loop_length - 1):
        prev_number, current_number = current_number, prev_number + current_number

    return current_number
