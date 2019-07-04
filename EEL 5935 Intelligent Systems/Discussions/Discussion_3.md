# Discussion 3

#1 But what *is* a Neural Network? | Deep learning, chapter 1
https://www.youtube.com/watch?v=aircAruvnKk
#2 Gradient descent, how neural networks learn | Deep learning, chapter 2
https://www.youtube.com/watch?v=IHZwWFHWa-w&t=1041s
#3 What is backpropagation really doing? | Deep learning, chapter 3
https://www.youtube.com/results?search_query=What+is+backpropagation+really+doing%3F+%7C+Deep+learning%2C+chapter+3


Neural Networks are inspired by the brain. But we can think of it as just a thing that holds a number. The layers of a neural net are trying to disect a surface using the activations of each nueron. With rudimentary neurons patterns are identified by each layer and we expect that these patterns become more identifieable as we dive deeper into more layers. This mechanisim of identifying patterns using mathematical combinations of activating neurons, coupled with a "learning" phase allows this "vannilla" example of a NN to do very powerful identification of patterns as complicated as human handwriting.

By assigning weights we can tweak sensitivities and dial back behaviours in recognizing regions of a pattern. A bias can be added to adjust when to actually activate on the recognized region. In a perfect world we would tweak these weights and biases on each layer considering its multiplicative effects into each layer to see a pattern as we see a pattern. But we start by randomizing these "knobs" and training it instead of sitting down and doing all this by hand.

An cost function can be used to implement "backpropogation" and adjust the neural net by modifying the "knobs" so that the error from an ideal state and the output of the NN to be reduced. Basically performing an optimization problem on the whole thing. Things we must be aware of is that we started in a random position to our otpimization to reduce error might just be reducing the error in a local minima, this is a problem we face when dealing with a multi-dimensional solution space.
