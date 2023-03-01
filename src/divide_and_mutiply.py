from divide import divide_by_three
from multiply import multiply_by_three

def divide_and_multiply(num):
    num_divided_by_three = divide_by_three.divide_by_three(num)
    print("after divided by 3 the input value is ")
    print(num)
    num = multiply_by_three.multiply_by_three(num_divided_by_three)
    print("after divided and multiply with the same value the input is ")
    print(num)