from functools import lru_cache


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    @lru_cache
    def __call__(self, *args):
        if self.cache.get(args):
            return self.cache[args]
        else:
            self.cache[args] = self.func(*args)
        return self.func(*args)


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print(slow_fibonacci(100))

@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

slow_fibonacci(5)

for args, value in sorted(slow_fibonacci.cache.items()):
    print(args, value)

# TEST_5:
@CachedFunction
def tribonacci(n):
    if n in (1, 2, 3):
        return 1
    return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)


print(tribonacci(200))
print(len(tribonacci.cache))

# TEST_4:
@CachedFunction
def quadratic_polinomial(a, b, c, x):
    return a * x ** 2 + b * x + c


data = [(286, 375, 286, 318), (43, 65, 446, 156), (382, 127, 228, 425), (271, 416, 467, 221), (14, 441, 108, 272),
        (257, 113, 203, 292), (117, 80, 86, 157), (354, 479, 323, 296), (315, 111, 482, 20), (431, 141, 75, 229),
        (152, 32, 494, 139), (61, 116, 239, 335), (296, 122, 62, 173), (158, 177, 126, 77), (101, 222, 160, 101),
        (292, 117, 143, 287), (228, 422, 397, 155), (153, 92, 278, 158), (307, 459, 120, 341), (129, 8, 358, 367),
        (101, 140, 165, 350), (153, 423, 28, 148), (481, 249, 341, 43), (265, 265, 84, 477), (65, 488, 274, 369),
        (62, 237, 300, 387), (396, 127, 419, 364), (146, 235, 412, 170), (412, 305, 47, 450), (253, 53, 478, 385),
        (202, 332, 196, 139), (335, 221, 375, 463), (300, 376, 144, 155), (338, 170, 14, 432), (327, 286, 373, 400),
        (409, 305, 260, 196), (472, 423, 167, 436), (189, 54, 184, 395), (91, 9, 36, 356), (278, 394, 362, 395),
        (356, 424, 67, 361), (333, 249, 169, 299), (344, 276, 61, 343), (118, 458, 486, 287), (86, 91, 128, 422),
        (182, 83, 35, 122), (192, 188, 138, 487), (23, 404, 334, 24), (241, 230, 281, 138), (74, 142, 254, 384),
        (257, 113, 203, 292), (117, 80, 86, 157), (354, 479, 323, 296), (315, 111, 482, 20), (431, 141, 75, 229),
        (152, 32, 494, 139), (61, 116, 239, 335), (296, 122, 62, 173), (158, 177, 126, 77), (101, 222, 160, 101),
        (292, 117, 143, 287), (228, 422, 397, 155), (153, 92, 278, 158), (307, 459, 120, 341), (129, 8, 358, 367),
        (101, 140, 165, 350), (153, 423, 28, 148), (481, 249, 341, 43), (265, 265, 84, 477), (65, 488, 274, 369),
        (62, 237, 300, 387), (396, 127, 419, 364), (146, 235, 412, 170), (412, 305, 47, 450), (253, 53, 478, 385),
        (202, 332, 196, 139), (335, 221, 375, 463), (300, 376, 144, 155), (458, 198, 293, 430), (358, 177, 80, 235),
        (28, 218, 430, 59), (471, 215, 390, 432), (246, 34, 105, 308), (428, 280, 27, 218), (270, 171, 209, 273),
        (145, 311, 135, 74), (250, 235, 29, 334), (141, 165, 451, 235), (346, 262, 421, 34), (316, 216, 111, 388),
        (499, 238, 31, 291), (39, 460, 177, 316), (155, 404, 338, 243), (234, 214, 237, 10), (172, 177, 102, 13),
        (241, 373, 61, 337), (486, 161, 439, 94), (104, 353, 27, 75), (267, 88, 442, 284), (238, 184, 7, 454)]

for a, b, c, x in data:
    quadratic_polinomial(a, b, c, x)

for arg, value in sorted(quadratic_polinomial.cache.items()):
    print(arg, value)

print(len(data))
print(len(quadratic_polinomial.cache))

# beauty
# class CachedFunction:
#     def __init__(self, func):
#         self.func = func
#         self.cache = {}
#
#     def __call__(self, *args):
#         result = self.cache.get(args) or self.func(*args)
#         self.cache.setdefault(args, result)
#         return result
