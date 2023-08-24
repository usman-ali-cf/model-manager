
def sum_decorator(func):
    """
    a python decorator

    :param func: a function passed to decorator
    :return: a wrapped function
    """

    def warraper():
        a = func()
        return a + a

    return warraper


def product_decorator(func):
    """
    a python decorator

    :param func: a function passed to decorator
    :return: a wrapped function
    """

    def warraper():
        a = func()
        return a * a

    return warraper


@sum_decorator
@product_decorator
def get_value1():
    return 10


@product_decorator
@sum_decorator
def get_value2():
    return 10


def main():
    print("get_value1: ", get_value1())
    print("get_value2: ", get_value2())


def wellcome_decorator(func):
    """"
    a python decorator to print wellcome
    """

    def wellcome_warraper(request):
        print("Wellcome User")
        return func(request)

    return wellcome_warraper
