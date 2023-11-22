class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return self.__mul__(other)


a = Vector(1, 2)
b = Vector(3, 4)

print(a + b)
print(a - b)
print(b + a)
print(b - a)

a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)

# TEST_3:
vectors = [(Vector(11, 65), Vector(24, 40)), (Vector(74, 100), Vector(44, 65)), (Vector(32, 46), Vector(46, 27)),
           (Vector(60, 12), Vector(7, 86)), (Vector(11, 92), Vector(35, 42)), (Vector(60, 11), Vector(30, 87)),
           (Vector(63, 28), Vector(38, 89)), (Vector(30, 72), Vector(41, 29)), (Vector(55, 33), Vector(72, 80)),
           (Vector(32, 80), Vector(55, 80)), (Vector(21, 98), Vector(78, 76)), (Vector(39, 38), Vector(46, 68)),
           (Vector(45, 83), Vector(52, 23)), (Vector(98, 86), Vector(61, 75)), (Vector(42, 89), Vector(57, 65)),
           (Vector(20, 18), Vector(25, 70)), (Vector(33, 19), Vector(41, 72)), (Vector(60, 10), Vector(58, 41)),
           (Vector(28, 41), Vector(91, 87)), (Vector(95, 5), Vector(27, 73)), (Vector(25, 65), Vector(66, 36)),
           (Vector(83, 22), Vector(11, 29)), (Vector(80, 82), Vector(92, 41)), (Vector(18, 15), Vector(29, 78)),
           (Vector(46, 60), Vector(67, 33)), (Vector(72, 34), Vector(63, 51)), (Vector(53, 95), Vector(25, 40)),
           (Vector(81, 67), Vector(19, 34)), (Vector(95, 37), Vector(79, 57)), (Vector(60, 39), Vector(60, 98)),
           (Vector(71, 99), Vector(100, 62)), (Vector(84, 56), Vector(89, 89)), (Vector(38, 21), Vector(18, 73)),
           (Vector(41, 63), Vector(99, 41)), (Vector(63, 25), Vector(48, 65)), (Vector(22, 28), Vector(39, 35)),
           (Vector(16, 14), Vector(69, 32)), (Vector(76, 10), Vector(82, 14)), (Vector(53, 25), Vector(53, 76)),
           (Vector(60, 6), Vector(86, 100)), (Vector(14, 55), Vector(31, 60)), (Vector(51, 52), Vector(38, 38)),
           (Vector(80, 31), Vector(88, 32)), (Vector(87, 56), Vector(59, 6)), (Vector(67, 73), Vector(14, 81)),
           (Vector(6, 90), Vector(92, 88)), (Vector(91, 26), Vector(44, 10)), (Vector(68, 88), Vector(99, 22)),
           (Vector(98, 70), Vector(89, 11)), (Vector(33, 40), Vector(92, 55)), (Vector(88, 13), Vector(5, 45)),
           (Vector(65, 52), Vector(16, 44)), (Vector(21, 11), Vector(92, 67)), (Vector(43, 75), Vector(18, 15)),
           (Vector(12, 61), Vector(45, 83)), (Vector(81, 69), Vector(67, 22)), (Vector(26, 89), Vector(91, 81)),
           (Vector(67, 15), Vector(100, 26)), (Vector(11, 91), Vector(50, 66)), (Vector(55, 55), Vector(42, 25)),
           (Vector(61, 12), Vector(57, 39)), (Vector(52, 6), Vector(50, 45)), (Vector(32, 74), Vector(27, 9)),
           (Vector(73, 66), Vector(79, 19)), (Vector(58, 99), Vector(32, 5)), (Vector(61, 55), Vector(79, 82)),
           (Vector(50, 20), Vector(49, 95)), (Vector(37, 82), Vector(7, 32)), (Vector(37, 72), Vector(48, 29)),
           (Vector(17, 14), Vector(15, 90)), (Vector(51, 6), Vector(34, 94)), (Vector(71, 91), Vector(5, 63)),
           (Vector(84, 17), Vector(31, 81)), (Vector(42, 33), Vector(73, 60)), (Vector(63, 66), Vector(50, 68)),
           (Vector(12, 89), Vector(55, 21)), (Vector(81, 29), Vector(77, 84)), (Vector(39, 85), Vector(46, 95)),
           (Vector(69, 71), Vector(76, 30)), (Vector(37, 90), Vector(97, 52)), (Vector(85, 76), Vector(64, 8)),
           (Vector(86, 29), Vector(89, 90)), (Vector(7, 39), Vector(52, 36)), (Vector(58, 100), Vector(27, 40)),
           (Vector(25, 49), Vector(10, 63)), (Vector(95, 76), Vector(18, 11)), (Vector(42, 68), Vector(10, 12)),
           (Vector(17, 82), Vector(54, 81)), (Vector(13, 42), Vector(31, 77)), (Vector(19, 12), Vector(87, 54)),
           (Vector(100, 67), Vector(13, 71)), (Vector(74, 89), Vector(62, 78)), (Vector(28, 96), Vector(34, 97)),
           (Vector(7, 53), Vector(69, 59)), (Vector(41, 7), Vector(12, 92)), (Vector(48, 55), Vector(13, 29)),
           (Vector(21, 46), Vector(25, 15)), (Vector(33, 93), Vector(72, 69)), (Vector(88, 64), Vector(82, 64)),
           (Vector(66, 29), Vector(73, 81))]

for vector1, vector2 in vectors:
    print(vector1 + vector2)

# TEST_4:
vectors = [(Vector(74, 12), Vector(55, 98)), (Vector(66, 28), Vector(78, 9)), (Vector(22, 85), Vector(68, 29)),
           (Vector(28, 6), Vector(37, 23)), (Vector(26, 81), Vector(35, 91)), (Vector(49, 36), Vector(13, 9)),
           (Vector(14, 92), Vector(69, 17)), (Vector(7, 38), Vector(26, 86)), (Vector(89, 27), Vector(92, 100)),
           (Vector(62, 48), Vector(19, 75)), (Vector(91, 90), Vector(15, 28)), (Vector(19, 60), Vector(84, 52)),
           (Vector(73, 34), Vector(89, 73)), (Vector(70, 97), Vector(44, 5)), (Vector(98, 70), Vector(39, 84)),
           (Vector(85, 33), Vector(89, 74)), (Vector(90, 77), Vector(42, 73)), (Vector(68, 60), Vector(55, 45)),
           (Vector(63, 46), Vector(61, 83)), (Vector(50, 6), Vector(97, 6)), (Vector(39, 89), Vector(50, 98)),
           (Vector(24, 90), Vector(77, 44)), (Vector(68, 100), Vector(67, 71)), (Vector(32, 13), Vector(63, 22)),
           (Vector(52, 14), Vector(45, 77)), (Vector(35, 65), Vector(56, 33)), (Vector(90, 41), Vector(46, 69)),
           (Vector(47, 46), Vector(54, 30)), (Vector(77, 53), Vector(5, 52)), (Vector(18, 28), Vector(13, 85)),
           (Vector(81, 39), Vector(31, 99)), (Vector(60, 23), Vector(57, 47)), (Vector(67, 9), Vector(75, 36)),
           (Vector(59, 8), Vector(20, 80)), (Vector(45, 44), Vector(13, 40)), (Vector(80, 45), Vector(24, 50)),
           (Vector(35, 94), Vector(27, 86)), (Vector(81, 98), Vector(25, 10)), (Vector(28, 18), Vector(98, 29)),
           (Vector(85, 58), Vector(80, 58)), (Vector(19, 76), Vector(12, 64)), (Vector(31, 19), Vector(78, 93)),
           (Vector(100, 60), Vector(26, 51)), (Vector(91, 67), Vector(8, 70)), (Vector(22, 95), Vector(71, 35)),
           (Vector(14, 51), Vector(13, 12)), (Vector(83, 82), Vector(95, 20)), (Vector(18, 59), Vector(37, 20)),
           (Vector(43, 16), Vector(48, 97)), (Vector(88, 85), Vector(70, 44)), (Vector(52, 22), Vector(22, 9)),
           (Vector(65, 61), Vector(24, 81)), (Vector(71, 31), Vector(92, 40)), (Vector(60, 41), Vector(50, 5)),
           (Vector(78, 63), Vector(62, 12)), (Vector(63, 27), Vector(84, 37)), (Vector(78, 98), Vector(7, 56)),
           (Vector(52, 39), Vector(99, 64)), (Vector(92, 32), Vector(61, 81)), (Vector(18, 31), Vector(32, 52)),
           (Vector(79, 62), Vector(79, 25)), (Vector(51, 11), Vector(56, 29)), (Vector(17, 37), Vector(17, 63)),
           (Vector(11, 25), Vector(56, 76)), (Vector(65, 82), Vector(86, 97)), (Vector(41, 58), Vector(77, 11)),
           (Vector(93, 37), Vector(48, 69)), (Vector(7, 77), Vector(15, 72)), (Vector(25, 100), Vector(80, 96)),
           (Vector(89, 87), Vector(19, 29)), (Vector(34, 83), Vector(8, 45)), (Vector(44, 38), Vector(81, 79)),
           (Vector(8, 66), Vector(65, 24)), (Vector(54, 62), Vector(40, 83)), (Vector(69, 100), Vector(47, 94)),
           (Vector(36, 10), Vector(73, 65)), (Vector(94, 25), Vector(68, 71)), (Vector(91, 71), Vector(62, 95)),
           (Vector(81, 11), Vector(34, 65)), (Vector(27, 61), Vector(28, 88)), (Vector(5, 96), Vector(97, 78)),
           (Vector(61, 67), Vector(72, 50)), (Vector(82, 76), Vector(66, 49)), (Vector(88, 85), Vector(80, 89)),
           (Vector(12, 20), Vector(47, 52)), (Vector(9, 30), Vector(9, 26)), (Vector(14, 69), Vector(36, 98)),
           (Vector(100, 78), Vector(35, 81)), (Vector(87, 58), Vector(49, 23)), (Vector(59, 13), Vector(31, 45)),
           (Vector(24, 21), Vector(71, 41)), (Vector(33, 12), Vector(48, 70)), (Vector(22, 14), Vector(80, 6)),
           (Vector(14, 25), Vector(53, 23)), (Vector(99, 56), Vector(84, 42)), (Vector(44, 35), Vector(78, 65)),
           (Vector(7, 59), Vector(67, 76)), (Vector(92, 61), Vector(63, 52)), (Vector(42, 32), Vector(51, 46)),
           (Vector(58, 86), Vector(91, 88))]

for vector1, vector2 in vectors:
    print(vector1 - vector2)

# TEST_5:
data = [(33, 20, 24), (40, 47, 43), (26, 69, 10), (78, 70, 26), (86, 23, 48), (49, 88, 65), (12, 51, 31),
           (78, 53, 57), (58, 60, 96), (81, 29, 36), (8, 17, 87), (32, 46, 80), (34, 68, 22), (71, 79, 63),
           (21, 78, 31), (83, 42, 74), (47, 69, 90), (49, 40, 94), (46, 90, 33), (81, 98, 18), (44, 66, 9), (5, 52, 65),
           (48, 52, 88), (55, 80, 7), (60, 71, 36), (22, 41, 50), (17, 89, 98), (10, 77, 30), (50, 26, 42),
           (41, 60, 26), (95, 63, 53), (68, 73, 20), (36, 97, 54), (50, 98, 44), (62, 98, 34), (87, 65, 81),
           (73, 76, 44), (37, 67, 28), (22, 5, 70), (65, 83, 80), (91, 91, 26), (79, 94, 60), (56, 69, 47), (18, 6, 50),
           (88, 14, 53), (69, 78, 25), (35, 7, 53), (88, 97, 79), (41, 51, 27), (84, 71, 99), (61, 59, 57),
           (20, 20, 44), (95, 85, 88), (60, 67, 17), (16, 8, 91), (32, 25, 22), (59, 24, 83), (76, 28, 34),
           (28, 42, 87), (52, 19, 89), (18, 61, 98), (89, 9, 51), (66, 8, 95), (90, 79, 32), (76, 74, 63), (35, 51, 68),
           (36, 57, 51), (40, 84, 75), (90, 43, 61), (100, 99, 13), (82, 67, 71), (38, 9, 84), (76, 7, 27),
           (53, 49, 93), (40, 17, 90), (33, 82, 36), (58, 95, 81), (70, 17, 45), (90, 65, 83), (87, 53, 50),
           (90, 8, 32), (88, 21, 44), (18, 72, 24), (16, 91, 13), (80, 20, 53), (63, 13, 81), (6, 90, 15), (96, 82, 87),
           (39, 19, 85), (54, 58, 55), (52, 97, 19), (54, 86, 69), (100, 17, 90), (51, 91, 28), (26, 62, 83),
           (86, 70, 20), (22, 13, 41), (100, 39, 85), (34, 92, 39), (75, 68, 9)]

for x, y, digit in data:
    vector = Vector(x, y)
    print(vector * digit)

# TEST_6:
vectors = [Vector(160, 880), Vector(440, 820), Vector(450, 190), Vector(590, 470), Vector(700, 760), Vector(190, 480),
           Vector(490, 150), Vector(210, 980), Vector(690, 940), Vector(820, 320), Vector(590, 570), Vector(650, 420),
           Vector(520, 200), Vector(380, 870), Vector(1000, 360), Vector(200, 950), Vector(860, 480), Vector(980, 850),
           Vector(420, 950), Vector(500, 460), Vector(140, 520), Vector(280, 1000), Vector(170, 550), Vector(550, 330),
           Vector(60, 470), Vector(890, 60), Vector(880, 140), Vector(170, 170), Vector(210, 950), Vector(720, 960),
           Vector(470, 120), Vector(130, 720), Vector(390, 500), Vector(900, 710), Vector(810, 710), Vector(290, 790),
           Vector(200, 270), Vector(400, 680), Vector(450, 810), Vector(180, 650), Vector(190, 730), Vector(330, 560),
           Vector(560, 260), Vector(830, 120), Vector(600, 220), Vector(460, 300), Vector(950, 130), Vector(300, 340),
           Vector(230, 740), Vector(970, 900), Vector(710, 630), Vector(360, 1000), Vector(740, 580), Vector(370, 450),
           Vector(140, 450), Vector(700, 160), Vector(850, 250), Vector(860, 670), Vector(810, 850), Vector(900, 560),
           Vector(580, 310), Vector(350, 330), Vector(210, 960), Vector(480, 310), Vector(350, 310), Vector(900, 230),
           Vector(300, 270), Vector(1000, 120), Vector(640, 810), Vector(300, 340), Vector(200, 300), Vector(240, 50),
           Vector(250, 890), Vector(110, 320), Vector(950, 450), Vector(250, 200), Vector(170, 970), Vector(350, 90),
           Vector(110, 310), Vector(80, 120), Vector(910, 810), Vector(110, 510), Vector(80, 280), Vector(710, 500),
           Vector(550, 210), Vector(520, 740), Vector(170, 180), Vector(750, 540), Vector(420, 480), Vector(910, 800),
           Vector(420, 490), Vector(870, 780), Vector(630, 570), Vector(460, 820), Vector(340, 730), Vector(440, 100),
           Vector(860, 50), Vector(100, 890), Vector(710, 520), Vector(530, 120)]

for vector in vectors:
    print(vector / 10)

# TEST_7:
vector1 = Vector(5, 10)
vector2 = Vector(10, 15)

vector3 = vector1 - vector2
vector4 = vector2 - vector1

print(vector3)
print(vector4)

# TEST_8:
vector = Vector(10, 20)
print(vector.__add__([]))
print(vector.__sub__(()))
print(vector.__mul__({}))
print(vector.__truediv__(set()))
