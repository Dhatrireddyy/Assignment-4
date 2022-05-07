# CBSE Probability Grade 10
# Ex 16.3 Q1

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
Which of the following cannot be valid assignment of probabilities for outcomes of sample
"""


def main():
    a_1 = 0.1 
    a_2 = 0.01  
    a_3 = 0.05  
    a_4 = 0.03 
    a_5 = 0.01  
    a_6 = 0.2 
    a_7 = 0.6

    if (prob(a_1,a_2,a_3,a_4,a_5,a_6,a_7) > 0):
        print("Invalid")
    else:
        print("Valid")

    b_1 = 1/7
    b_2 = 1/7
    b_3 = 1/7
    b_4 = 1/7
    b_5 = 1/7
    b_6 = 1/7
    b_7 = 1/7

    if (prob(b_1,b_2,b_3,b_4,b_5,b_6,b_7) > 0):
        print("Invalid")
    else:
        print("Valid")

    c_1 = 0.1 
    c_2 = 0.2  
    c_3 = 0.3 
    c_4 = 0.4
    c_5 = 0.5 
    c_6 = 0.6
    c_7 = 0.7

    if (prob(c_1,c_2,c_3,c_4,c_5,c_6,c_7) > 0):
        print("Invalid")
    else:
        print("Valid")

    d_1 = 0.1 
    d_2 = 0.2  
    d_3 = 0.3 
    d_4 = 0.4
    d_5 = 0.5 
    d_6 = 0.6
    d_7 = 0.7

    if (prob(d_1,d_2,d_3,d_4,d_5,d_6,d_7) > 0):
        print("Invalid")
    else:
        print("Valid")

    e_1 = 1/14
    e_2 = 2/14
    e_3 = 3/14
    e_4 = 4/14
    e_5 = 5/14
    e_6 = 6/14
    e_7 = 15/14

    if (prob(e_1,e_2,e_3,e_4,e_5,e_6,e_7) > 0):
        print("Invalid")
    else:
        print("Valid")

def prob(x_1,x_2,x_3,x_4,x_5,x_6,x_7) -> int:
    """ Returns the value of x """

    x = 0

    if (x_1 < 0 or x_1 > 1 or x_2 < 0 or x_2 > 1 or x_3 < 0 or x_3 > 1 or x_4 < 0 or x_4 > 1 
    or x_5 < 0 or x_5 > 1 or x_6 < 0 or x_6 > 1 or x_7 < 0 or x_7 > 1 or x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 != 1 ):
        x = x + 1
    return x
    
if __name__ == '__main__':
       main()
