class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        n_f = int(new_floor)
        if 1< n_f > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            i = 1
            while i <= n_f:
                print(i)
                i += 1

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
