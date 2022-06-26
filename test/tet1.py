


class BenzCar:
    brand = '奔驰'
    country = '德国'

    def pressHorn(p):
        print('嘟嘟~~~~~~')


class test1(BenzCar):
    super.__prepare__()


p = test1()
p.pressHorn()
print(p.brand)