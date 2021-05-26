class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        print('area', self.area)
        return(self.area)

    def get_perimeter(self):
        self.perimeter = 2*self.width + 2*self.height
        print('perimeter', self.perimeter)
        return(self.perimeter)

    def get_diagonal(self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        print('diagonal', self.diagonal)
        return(self.diagonal)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            string = 'Too big for picture.'
            print(string)
            return(string)
        else:
            string = ''
            for row in range(self.height):
                for col in range(self.width):
                    string += '*'
                    #print('*', end='')
                string += '\n'
            string = string
            print(string)
            return(string)

    def get_amount_inside(self, shape): #width, height, and area are all attributes of Rectangle objects so the shape instance can use them to compare with self.method
        if self.width >= shape.width and self.height >= shape.height:
            numberinside = int(self.get_area() / shape.get_area())
            print('is inside:', numberinside, 'times')
            return(numberinside)
        else:
            print('is not inside')
            numberinside = 0
            print(numberinside)
            return(numberinside)

    def __str__(self):
        self.string = f'Rectangle(width={self.width}, height={self.height})'
        #print(self.string)
        return(self.string)

class Square(Rectangle):

    def __init__(self, side):
        #super().__init__(width, height)
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_side(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height



    def __str__(self):
        self.string = f'Square(side={self.side})'
        return(self.string)



r = Rectangle(4, 8)
r.set_height(10)
r.set_width(15)
r.get_area()
r.get_diagonal()
r.get_perimeter()
r.get_picture()
# s = Square(5)
# t = Rectangle(4, 4)
# s.get_picture()
# # p.get_picture()
# # print(s)
# r.get_amount_inside(s) # get amount doesn't account for change in set_height / set_width in final calulation
# r.get_amount_inside(t)
# # s.set_side(4)
# # s.get_area()
# # s.get_perimeter()
# # s.get_picture()
# # s.get_diagonal()
# s.get_amount_inside(r)

# print(s)
