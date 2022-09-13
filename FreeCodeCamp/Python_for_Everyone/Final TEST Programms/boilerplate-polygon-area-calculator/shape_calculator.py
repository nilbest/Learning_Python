class Rectangle:
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def __str__(self):
        output = f"Rectangle(width={self.width}, height={self.height})"
        return output

#to do
    def set_width (self,width):
        self.width=int(width)
        
    def set_height (self,height):
        self.height=int(height)
        
    def get_area (self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        lines = []
        for i in range(0,self.height):
            lines.append("*"*self.width+"\n")
        output=("".join(lines))
        return output
    
    def get_amount_inside(self,other_shape):
        if self.width >= other_shape.width and self.height >= other_shape.height:
            #number_w = int(self.width / other_shape.width)
            #number_h = int(self.height / other_shape.height)
            return int(self.get_area() / other_shape.get_area())
        else:
            return 0

    def __del__(self):
        print("\n"+"#"*40+"\nA Rectangle has been deleted.\n"+"#"*40+"\n")



class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
        #self.width,self.height=length
    
    def __str__(self):
        output = f"Square(side={self.width})"
        return output
        
    def set_side(self,length):
        self.width=length
        self.height=length
    
    def __del__(self):
        print("\n"+"#"*40+"\nA Square has been deleted.\n"+"#"*40+"\n")

