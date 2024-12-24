# create attribute
class Cookie:
    pass

# we can add attribute like
# a = Cookie()
# a.color = 'red'
# print(star_cookie1.weight)


class Cookie1:
    # global
    milk = 0.1

    def __init__(self, color, weight=None):
        self.color = color
        self.weight = weight


star_cookie1 = Cookie1('red', 30)
star_cookie2 = Cookie1('green', 30)

print(star_cookie1.color)
star_cookie1.weight = 20
print(star_cookie1.weight)
print(star_cookie1.milk)
print(star_cookie2.milk)
