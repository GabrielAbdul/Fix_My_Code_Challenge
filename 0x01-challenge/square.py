#!/usr/bin/python3
'''module defines a class square'''


class Square():
    '''Class Square'''

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        '''init function to happen every time obj instantiated'''
        for key, value in kwargs.items():
            setattr(self, key, value)

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
