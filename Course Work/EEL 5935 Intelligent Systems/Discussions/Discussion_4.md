# Discussion 4

How Deep Neural Networks Work
Brandon Rohrer
https://www.youtube.com/watch?v=ILsA4nyG7I0&t=38s


Discuss the  classification using feed-forward NN. What type of neuron units  were use  for the example?

An input vector describes your input as a set of numbers. A receptive field describes what each of those inputs are at its maximum state. To build a neuron we add up all the values of the input vector and we weight all of those values as "weighted connections". After we add them we can squash them with an activation function like a "sigmoid" that forces the sum to be between -1 and 1. Once we expand to multiple neurons we see that each picks a receptive feild that indentifies distinct patterns such as max values of two pixels or subtraction of max values of another two pixels.

Calculating error requires computing the values through a feed forward neural net by multiplying all of our wieghts and summing  and activating etc. This is computationally expensive if we need to tweak millions of times. 

The technique we need is backpropogation. The ability to use the change between the weight and the error as a slope. We need to first identify an error function like, the square of the weight. this function helps to identify the slope at every value for w we choose. Utilizing the "chain" rule for derivatives the slope of a series of steps can be multiplied to get the full slope. This allow for faster computations . 

Other parts of the backpropogation is the summing in each neuron that results in a slope of 1, and lastly the sigmoid function can be propogated a a derivative and it just so happens that to get its derivative it only needs to be mulitplied by 1 minus itself. Similarly Relu function can be derived down to 1 or 0.

So finally the chain rule forces us ot start at the error and calculate the derivative at each step starting out the output neurons. This back propogation is done many times slowly trying to reduce the error to an acceptable slope of 0.

