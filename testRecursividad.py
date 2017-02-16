__author__ = 'manuel'


def testOptimization():
    items = [1, 2, 3, 4, 5]

    def calulaPot(x):
        return x ** 2

    a = list(map(lambda x: x % 2, items))

    def square(x):
        return (x**2)
    def cube(x):
            return (x**3)

    funcs = [square, cube]
    value = []
    for r in range(5):
        value.append(map(lambda x: x(r), funcs))
        print value

if __name__ == "__main__":
    a = testOptimization()