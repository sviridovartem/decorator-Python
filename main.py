def decorator_function_with_arguments(*list_params):
    def wrap(function):
        def wrapped_f():
            print(f"Your function name:{function.__name__}")
            print(f"Your string list:{[el for el in list_params if isinstance(el, str)]}")
            function()
            print(f"Your not str list:{[el for el in list_params if not isinstance(el, str)]}")

        return wrapped_f

    return wrap


@decorator_function_with_arguments(1.5, "asdasdasdasdasdasdasdasdas0", 13, "bla", True, {"first": 1})
def any_type_except_str():
    return print("working inside function")


any_type_except_str()
