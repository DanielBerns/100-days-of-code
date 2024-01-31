# https://www.freecodecamp.org/news/the-python-decorator-handbook/

def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Log the return value
        print(f"{original_function.__name__} returned: {result}")

        # Return the result
        return result
    return wrapper


import time

def measure_execution_time(func):
    def timed_execution(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print(f"Function {func.__name__} took {execution_duration:.2f} seconds to execute")
        return result
    return timed_execution


def cached_result_decorator(func):
    result_cache = {}

    def wrapper(*args, **kwargs):
        cache_key = (*args, *kwargs.items())

        if cache_key in result_cache:
            return f"[FROM CACHE] {result_cache[cache_key]}"

        result = func(*args, **kwargs)
        result_cache[cache_key] = result

        return result

    return wrapper


def check_condition_positive(value):
    def argument_validator(func):
        def validate_and_calculate(*args, **kwargs):
            if value(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Invalid arguments passed to the function")
        return validate_and_calculate
    return argument_validator

# @check_condition_positive(lambda x: x > 0)
# def compute_cubed_result(number):
#     return number ** 3



def handle_exceptions(default_response_msg):
    def exception_handler_decorator(func):
        def decorated_function(*args, **kwargs):
            try:
                # Call the original function
                return func(*args, **kwargs)
            except Exception as error:
                # Handle the exception and provide the default response
                print(f"Exception occurred: {error}")
                return default_response_msg
        return decorated_function
    return exception_handler_decorator

# Example usage
@handle_exceptions(default_response_msg="An error occurred!")
def divide_numbers_safely(dividend, divisor):
    return dividend / divisor

# Call the decorated function
result = divide_numbers_safely(7, 0)  # This will raise a ZeroDivisionError
print("Result:", result)
