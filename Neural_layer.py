input = [1,2,3,2.5]
weight1 = [0.2,0.8,-0.5,1.0]
weight2 = [0.5,-0.91,0.26,-0.5]
weight3 = [-0.26,-0.27,0.17,0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5
output =[input[0]*weight1[0]+input[1]*weight1[1]+input[2]*weight1[2]+ input[3]*weight1[3]+ bias1,
         input[0]*weight2[0]+input[1]*weight2[1]+input[2]*weight2[2]+ input[3]*weight2[3]+ bias2,
         input[0]*weight3[0]+input[1]*weight3[1]+input[2]*weight3[2]+ input[3]*weight3[3]+ bias3]

print(output)

# Created a layer of neurons containing 3 neurons each neuron has 4 inputs

# input = [1,2,3,2.5]
# weights = [[0.2,0.8,-0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
# biases = [2,3,0.5]

# output = []

# for neuron_weights, neuron_bias in zip(weights,biases):
#     neuron_out = 0 #output of a single neuron in the layer
#     for neuron_input,weight in zip(input,neuron_weights):
#         neuron_out += neuron_input*weight
#     neuron_out += neuron_bias
#     output.append(neuron_out)

# print(output)

# The abouve code represets the smarter way to code :)