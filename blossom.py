from typing import Callable, Any
import requests
import re
# import json


class ConfigurationError(Exception):
    """Исключение если значение параметра - не целое число или целое число но меньшее 1."""

    def __init__(self, errors_list: str)  -> None:
        """Вызов конструктора базового класса с параметрами которые ему нужны."""
        super().__init__(self)
        # Затем свой код исключения
        self.errors_list = errors_list

    def __str__(self)  -> str:
        return str(self.errors_list)


def blossom(repeat_times: int = 1) -> Callable:
    """Декоратор повторяет укананную функцию до max_retries раз пока не равершится без исключений."""
    string_verifier = re.compile("^[1-9]+$")  # отвергаем если не цифры 1-9, правильность на позже
    if not string_verifier.match(str(repeat_times)):
        raise ConfigurationError("Количество повторений не целое число или меньше единицы")

    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            exceptions = dict()
            exceptions[func.__name__] = {}
            exceptions[func.__name__]["run"] = list()
            for i in range(int(repeat_times)):
                try:
                    x = func(*args, **kwargs)
                    exceptions[func.__name__]["is_success"] = True
                    print(x)
                    exceptions[func.__name__]["run"].append({"exception" : None, "return": x})
                    return exceptions
                except Exception as ex:
                    exceptions[func.__name__]["is_success"] = False
                    y = ex.__doc__
                    exceptions[func.__name__]["run"].append({"exception" : y, "return": None})
            # json_str = json.dumps(exceptions, indent=4, sort_keys=True) #  вариант с выводом Json
            # return json_str
            return exceptions
        return wrapper
    return decoration


@blossom(2)
def get_page_content(url: str)  -> Any:
    """Основная функция, отправляет реквесты на подаваемый url."""
    resp = requests.get(url)
    return resp.content

# print(get_page_content("https://httpbin.org/get"))
