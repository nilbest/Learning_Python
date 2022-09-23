# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)

###### Test Import Data Hat ######
hat1 = prob_calculator.Hat(yellow=3, blue=2, green=6)
hat1.set_name('hat1')
hat2 = prob_calculator.Hat(red=5, orange=4)
hat2.set_name('hat2')
hat3 = prob_calculator.Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
hat3.set_name('hat3')
print(hat1)
#print(hat1.contents)
print(hat2)
print(hat3)
######################################


hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)


# Run unit tests automatically
main(module='test_module', exit=False)
