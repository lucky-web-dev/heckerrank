def hello_decorator(func):
    def inner1(*args, **kwargs):

        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a,d):
    print("Inside the function")
    return a + d

a= 2
b= 1

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
