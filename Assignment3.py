
def math_operations(a, b):
    """
    The math operation function takes the two numbers as input and returns
    the sum and products using the lambda functions as illustrated in the code below.
    """
# Lambda functions for sum and product
    lambda_sum = lambda x, y: x + y
    lambda_product = lambda x, y: x * y

    # Return the sum and product
    return lambda_sum(a, b), lambda_product(a,b)

def main():
    # Users input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # call the math operations function
    sum_results, product_results = math_operations(num1,num2)

    # print the results
    print("sum: ", sum_results)
    print("product: ", product_results)

# Run the main function
if __name__ == "__main__":
    main()