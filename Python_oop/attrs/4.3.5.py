class Gun:
    def __init__(self):
        self.flag = 0
        self.count_shouts = 0

    def shoot(self):
        self.count_shouts += 1
        if self.flag == 0:
            print('pif')
            self.flag = 1
        else:
            self.flag = 0
            print('paf')

    def shots_count(self):
        return self.count_shouts

    def shots_reset(self):
        self.count_shouts = 0
        self.flag = 0


# gun = Gun()
#
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())

gun = Gun()

gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
gun.shoot()
