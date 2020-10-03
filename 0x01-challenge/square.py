#!/usr/bin/python3
'''module defines a class square'''


class Square():
    '''Class Square'''

    def __init__(self, width=0, height=0):
        '''init function to happen every time obj instantiated'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @property
    def width(self):
        '''width getter'''
        return self.__height

   @width.setter
    def width(self, v):
        '''width setter'''
        if v < 1:
            raise('width must be greater that 0')
        elif type(v) not int:
            raise('width must be an integer')
        else:
            self.__width = v

   @height.setter
    def height(self, v):
    '''height setter'''
        if v < 1:
            raise('height must be greater that 0')
        elif type(v) not int:
            raise('height must be an integer')
        else:
            self.__height = v


    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        ''' peremiter of the square '''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        ''' str representation when you print(obj)'''
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
