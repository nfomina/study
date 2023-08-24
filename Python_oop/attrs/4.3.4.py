class Gun:
    def __init__(self):
        self.flag = 0
    def shoot(self):
        if self.flag == 0:
            print('pif')
            self.flag = 1
        else:
            self.flag = 0
            print('paf')


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
