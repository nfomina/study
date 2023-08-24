class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.mapping = {'a': 0,
                        'b': 1,
                        'c': 2,
                        'd': 3,
                        'e': 4,
                        'f': 5,
                        'g': 6,
                        'h': 7}

    def get_char(self):
        return 'N'

    def can_move(self, letter, number):
        horse_new_horizontal = self.mapping.get(letter)
        horse_new_vertical = int(number)
        if (abs(self.mapping.get(self.horizontal)-horse_new_horizontal) == 2 and
            abs(int(self.vertical)-horse_new_vertical) == 1) or (abs(self.mapping.get(self.horizontal) -
                                                                     horse_new_horizontal) == 1 and abs(
            int(self.vertical)-horse_new_vertical) == 2):
            return True
        return False

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):

        n = 8
        matrix = [['.'] * n for _ in range(n)]

        horse = (self.horizontal, self.vertical)
        horse_c = [n - int(horse[1]), self.mapping.get(horse[0])]

        matrix[horse_c[0]][horse_c[1]] = 'N'

        if n - horse_c[0] < 7:
            if n - horse_c[1] < 8:
                matrix[horse_c[0] - 2][horse_c[1] - 1] = '*'
            if n - horse_c[1] > 1:
                matrix[horse_c[0] - 2][horse_c[1] + 1] = '*'

        if horse_c[0] + 2 < 8:
            if n - horse_c[1] < 8:
                matrix[horse_c[0] + 2][horse_c[1] - 1] = '*'
            if n - horse_c[1] > 1:
                matrix[horse_c[0] + 2][horse_c[1] + 1] = '*'

        if n - horse_c[1] < 7:
            if n - horse_c[0] < 8:
                matrix[horse_c[0] - 1][horse_c[1] - 2] = '*'
            if horse_c[0] + 2 <= 8:
                matrix[horse_c[0] + 1][horse_c[1] - 2] = '*'

        if horse_c[1] + 2 < 8:
            if n - horse_c[0] < 8:
                matrix[horse_c[0] - 1][horse_c[1] + 2] = '*'
            if horse_c[0] + 2 <= 8:
                matrix[horse_c[0] + 1][horse_c[1] + 2] = '*'

        for row in matrix:
            print(''.join(row))


knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

knight = Knight('c', 3, 'white')

knight.draw_board()

print(knight.can_move('e', 15))