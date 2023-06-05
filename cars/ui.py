from cars.logic import create_brand, create_car, \
    read_brand, read_car, update_brand, update_car, delete_car, \
    delete_brand


def create_brand_ui():
    name = input('enter brand name -> ')
    brand_name = create_brand(name)
    print(f'brand with name {brand_name} was created')


def create_car_ui():
    data = {}
    data['model'] = input('enter model -> ')
    data['release_year'] = int(input('enter release year -> '))
    data['id'] = input('enter brand"s id -> ')
    car_model_name = create_car(data)
    print(f'{car_model_name} was created')



def read_brand_ui():
    brands = read_brand()
    for brand in brands:
        print(f'id - {brand.id} name - {brand.name}')


def read_car_ui():
    cars = read_car()
    for car, brand in cars:
        print(f'id - {car.id} - {car.model}, {car.release_year}, {brand.name}')


def update_brand_ui():
    id = int(input('enter brand id for update -> '))
    new_name = input("enter new brand's name -> ")
    update_brand(id, new_name)


def update_car_ui():
    id = int(input('enter car id for update -> '))
    data = {}
    data['model'] = input('enter model -> ')
    data['release_year'] = int(input('enter release year -> '))
    data['id'] = input('enter brand"s id -> ')
    update_car(id, data)


def delete_car_ui():
    id = int(input('enter car"s id for delete car -> '))
    delete_car(id)


def delete_brand_ui():
    id = int(input("enter brand's id for delete brand -> "))
    delete_brand(id)


def main():
    choices = {"1": create_brand_ui,
               "2": create_car_ui,
               "3": read_brand_ui,
               "4": read_car_ui,
               "5": update_brand_ui,
               "6": update_car_ui,
               "7": delete_car_ui,
               "8": delete_brand_ui}
    while True:
        choice = input("""
                enter
                "1": create_brand,
                "2": create_car,
                "3": read_brand,
                "4": read_car,
                "5": update_brand,
                "6": update_car,
                "7": delete_car,
                "8": delete_brand
                for exit enter something else
                let's do it ------------------>
                """)

        if choice not in choices:
            print('see you next time')
            break
        else:
            choices[choice]()


if __name__ == '__main__':
    main()
