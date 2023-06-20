import random
class crushlove:
    def love(self, yourname, crushname):
        i = 0
        your_list = []
        for i in yourname:
            your_list.append(i)
        j = 0
        crush_list = []
        for j in crushname:
            crush_list.append(j)

        x = random.choice(your_list)
        y = random.choice(crush_list)
        
        if x in crush_list:
            print(f"{yourname} loves {crushname}")
        else:
            print(f"{yourname} don't love {crushname}")
        if y in your_list:
            print(f"{crush_name} loves {your_name} back ")
        else:
            print(f"{crush_name} dosen't love {your_name} back ")


print("find out how much chimistry between you and your crush ???")
your_name = str(input("\n enter your name: "))
crush_name = str(input("\n enter your crush name: "))
love1 = crushlove()
love1.love(your_name, crush_name)
