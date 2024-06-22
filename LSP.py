class Rectangle:
    def __init__(self):
        self._height = 0
        self._width = 0
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
        
class Square(Rectangle):
    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value
        
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
        

class LSPBehavior:
    @staticmethod
    def get_area(rectangle):
        if rectangle.width > 20:
            rectangle.width = 20
        return rectangle.width * rectangle.height
    

def main():
    o = Square()
    o.width = 40
    # o.height = 40  # Optional, already set width which also sets height
    area = LSPBehavior.get_area(o)
    print(area)
    
if __name__ == "__main__":
    main()