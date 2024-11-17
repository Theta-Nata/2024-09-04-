# Задача "Учёт товаров"
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        open('products.txt', 'w')
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()

    def add(self, *products):
        file = open(self.__file_name, 'r')
        existing_products = file.readlines()
        file.close()

        existing_product_names = set()
        for line in existing_products:
            if line:  # Проверяем, что строка не пустая
                comma_index = line.find(', ')
                if comma_index != -1:
                    product_name = line[:comma_index]
                    existing_product_names.add(product_name)

        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in existing_product_names:
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print('Первый запуск')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

print('Второй запуск')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())