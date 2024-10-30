def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() # при вызове внутри функции test_function() печати не проиходит

test_function() # выполняется вывод текста на консоль

inner_function() # выскакивает ошибка, что эта функция не определена, т.е программа её не видит.

