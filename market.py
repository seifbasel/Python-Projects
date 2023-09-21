def tvs():
    choice_tv = int(
        input(print(" for LG enter 1:  \n for samsung enter 2:  \n for sony enter 3: ")))
    tv_name = ["LG", "samsung", "sony"]
    tv_price = [6000, 10000, 15000]
    discount = .10
    if choice_tv == 1:
        x = 0
    elif choice_tv == 2:
        x = 1
    elif choice_tv == 3:
        x = 2

    tv_price_after_dis = tv_price[x]-(tv_price[x]*discount)

    print(f"{tv_name[x]} price before discont is {tv_price[x]}")
    print(f" price after discont {tv_price_after_dis}")


def colders():
    choice_colder = int(input(
        print(" for LG enter 1:  \n for samsung enter 2:  \n for toshiba enter 3: ")))
    colder_name = ["LG", "samsung", "toshiba"]
    colder_price = [3000, 7000, 9000]
    discount = .20
    if choice_colder == 1:
        z = 0
    elif choice_colder == 2:
        z = 1
    elif choice_colder == 3:
        z = 2
    colder_price_after_dis = colder_price[z]-(colder_price[z]*discount)
    print(f"{colder_name[z]} price before discont is {colder_price[z]}")
    print(f" price after discont {colder_price_after_dis}")


def iot():
    choice_iot = int(input(print(" for arduino uno enter 1:  \n for arduino nano enter 2:  \n for raspberry pi enter 3: ")))
    iot_name = ["arduino uno","arduino nano","raspberry pi"]
    iot_price =[300,500,2000]
    discount = .30
    if choice_iot == 1:
        s = 0
    elif choice_iot == 2:
        s = 1
    elif choice_iot == 3:
        s = 2
    iot_price_after_dis = iot_price[s]-(iot_price[s]*discount)
    print(f"{iot_name[s]} price before discont is {iot_price[s]}")
    print(f" price after discont {iot_price_after_dis}")

def robotics():
    choice_robot = int(input(print(
        " for robot 1 enter 1:  \n for robot 2 enter 2:  \n for robot 3 enter 3: ")))
    robot_name = ["robot 1", "robot 2", "robot 3"]
    robot_price = [200000, 500000, 300000]
    discount = .25
    if choice_robot == 1:
        s = 0
    elif choice_robot == 2:
        s = 1
    elif choice_robot == 3:
        s = 2
    iot_price_after_dis = robot_price[s]-(robot_price[s]*discount)
    print(f"{robot_name[s]} price before discont is {robot_price[s]}")
    print(f" price after discont {iot_price_after_dis}")


def laptops():
    choice_laptop = int(input(print(
        " for dell enter 1:  \n for HP enter 2:  \n for lenovo enter 3: ")))
    laptop_name = ["dell", "hp", "lenovo"]
    laptop_price = [20000, 15000, 22000]
    discount = .25
    if choice_laptop == 1:
        s = 0
    elif choice_laptop == 2:
        s = 1
    elif choice_laptop == 3:
        s = 2
    laptop_price_after_dis = laptop_price[s]-(laptop_price[s]*discount)
    print(f"{laptop_name[s]} price before discont is {laptop_price[s]}")
    print(f" price after discont {laptop_price_after_dis}")



name = str(input(print("what is your name?")))
print(" hi " , name ,"\n welcome to our store \n please choose a category ")
choice = int(input(print(
    " for tvs enter 1:  \n for colders enter 2:  \n for iot enter 3: \n for robotcs enter 4: \n for laptops enter 5: ")))

if choice == 1:
    tvs()

elif choice == 2:
    colders()

elif choice == 3:
    iot()

elif choice == 4:
    robotics()

elif choice == 5:
    laptops()
