def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(*args):
        print(f"Your function name:{function_to_decorate.__name__}")
        print(f"Your string list:{[el for el in args if isinstance(el, str)]}")
        print(function_to_decorate(*args))

    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def any_type_except_str(*args):
    return [el for el in args if not isinstance(el, str)]


any_type_except_str(1.5, "asdasdasdasdasdasdasdasdas0", 13, "bla", True, {"first": 1})
