def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()

# inner_function() - работать не будет, тк эта функция существует только во время работы test_function и находится в ее локальном пространстве

