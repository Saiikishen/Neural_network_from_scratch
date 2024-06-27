import numpy as np 

input = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

output =  np.dot(weights,input) + biases
'''
Note: The operation np.dot(input,weights) is invalid as the dot func requires the multi-dimensional(matrix) array
(weights) to be the 1st operand '''

print(output)

'''The above is an implementation of dot product it can also be called as the cosine pdt, operation we had done 
earlier was also dot pdt, here we are using the module numpy to do the math for us'''

