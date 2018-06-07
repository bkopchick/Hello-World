#Let's make this a little more exciting than:
#print('Hello you spaghetti monster forsaken world')
#My apologies to any readers offended by that statement

import numpy as np
from scipy.stats import binom

a = np.random.randint(10)
b = 0

while a != 7:
    print('You did not get the magic number!')
    a = np.random.randint(10)
    b += 1

if b > 0:
    prob = 1-binom.pmf(0, b, .1)
    print('It only took you {} tries.'.format(b+1))
    print('In a random set of {} attempts, there was a {} probability of getting the magic number at least once.'.format(b+1, prob))

    if prob < .5:
        print('Python has deemed you worthy!')
        print('Hello World!')
    else:
        print('Python would like me to tell you, to go to the depths of Fortran where you belong!')
        print('Goodbye cruel world!')

if b == 0:
    print('You had a 10% chance of getting it on your first try, you deserve a cookie!!')
    print('Python has deemed you more than worthy!')
    print('Hello World!')
