import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self,**kwargs):
        self.contents = []
        self.name = str(None)
        for key,value in kwargs.items():
            for i in range(0,value):
                self.contents.append(key)
        

    def __str__(self):
        output = f"The Hat '{self.name}' has ({self.create_list()}) in it."
        return output
    
    def set_name(self,name):
        self.name = name
    
    def create_list(self):
        my_dict = {i:self.contents.count(i) for i in self.contents}
        return my_dict
    
    def draw(self, number):
        output = []
        if number >= len(self.contents):
            output = self.contents 
        else: 
            for i in range(0,number):
                i = self.contents.pop(random.randrange(len(self.contents)))
                output.append(i)
        
        return output
    
    def __del__(self):
        print("\n"+"#"*40+f"\nThe Hat '{self.name}' has been deleted.\n"+"#"*40+"\n")
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N=num_experiments
    M=0
    for i in range(0,num_experiments):
        copy_of_contents = copy.copy(hat.contents)
        drawn_content = hat.draw(num_balls_drawn)
        hat.contents = copy.copy(copy_of_contents)
        my_dict = {i:drawn_content.count(i) for i in drawn_content}
        Test = 0
        for key in expected_balls:
            if my_dict.get(key, 0) >= expected_balls.get(key):
                Test +=1
        if Test == len(expected_balls):    
            M = M+1 
        my_dict.clear()
    return M/N
        