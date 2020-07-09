# A Review of "Application of Neural Networks in Oil Refinery"
Reference paper authored by Ali Zilouchian and Khalid Bawazir \
EEL5934 SUMMER 2019 \
Intelligent Systems \
Hector Lopez

## Summary of "Application of Neural Networks in Oil Refinery"
### Building the Artificial Network
At the Tanura Oil Refinery the processes outputs are sent to a lab and the quality is measured. If the sample of the quality is not good enough the process needs to be "re-worked" resulting in costly expenses. The goal of applying a neural net to the process is to have the system learn the quality outcome based on the inputs. This will allow for the system to measure quality in a parallel way that can reduce the need for costly analyzers every time the outputs are sampled.  

The use of soft computing methodologies; Neural Networks, Fuzzy Logic, Genetic Algorithms allow for more effective methods to help control highly nonlinear relationships. Neural Nets can be used for predictions by using mathematical coefficients that can be trained on historical data. The historical data is used to generalize the patterns that result in a desired outcome. The technique to train the neural net is called back-propagation. The data is split into training data for the model creation and test data to verify that the model is accurate enough to provide results given the known outcome. This helps to trust the model with unknown data in the real world.

Neural Nets require large data sets with a varied range to be able to accurately understand all the states it can come across during a real-world scenario. It is best that a many process variable as possible are fed into the dataset for the neural net to train on. The edge cases are best discovered by either running specific tests during plant operations to be able to capture the outcomes. The data would also need to be consistent. It is better for the data to be repeatable rather than accurate. An inaccurate sensor that measures a value consistently with an error is better than a sensor that varies its error in an unknown way. This type of noise is hard to train against since it cannot be abstracted from the true value. Systems like SCADA's or DCS's that capture sensor data and log it is more effective than handwritten logs for example. Sensors with flow or pressure can be averaged to remove noise.
All the input data should be collected in a reliable manner making sure that there is no lapse in the values and that they are all in sync so that the values are all captured at the same moment that the output is measured. A 3-month steady state data set was used in the experiment. The steady state of the data was found by making sure it was at least two time constant from the beginning of signal.

### Data Analysis 
By coordinating a 'good' lab value result and the measured value results the ability for the model to accurately find what makes a given "lab" value becomes better. Eliminating bad values becomes a case of testing the data sets and discovering outliers. The method used in the paper was to utilize all 180 datasets except for 3 and rotate them through testing the three data sets and determining if it fell outside any repeatability tolerances found in the lab. The method identified the corrupt datasets.

Engineering knowledge is used to initially elminate the process inputs but then the weights of the neural nets can be used to determine the what other process inputs can be removed. During the backpropogation training wieghts are associated to each of the inputs of hte neural net. These weights can be used along side engineering understanding so they can be prioritized. Albeit a lower wieght does not necessarily mean the input is not needed. 

The nerual net can only be scored by how well it perfroms against a desired outcome. The outcomes that are desired in the project is hte prediction of the Reid Vapor Pressure and the Naphta 95% Cut-Point. These lab values are measured for 180 different input states. The input values are marked against the 180 samples taken. The idea would be to train a NN to provide the same lab measurement given the inputs. The results of hte simulation show that there are many variables to consider when looking for its network performance.


### Results
The training for the Naphta 95% cut-point consisted of 33 process variables with the sampled Naphta 95% cutpoint output. The dataset consisted of 70 for training and 15 for testing. A single hidden layer with 5 neurons was trained achieving an error of 0.01 in 10k itterations. To improve the model additional parameters where introduced and even an adaptive learning rate was added . These improvements resulting in a sum-squared error of 0.01 within only 3180 itterations. Attempts to further improve the outcome of the predictions resulting in adding hidden layers, and more neurons. Doing this resulting in memorization of the datasets and creating overfitting scenarios.


## Advantage of Using Nueral Network

The application of a neural net has its advantages in this sisutation because the project can provide consistent data from industrial control systems. The data collected is reliable even though its not accurate. This type of data collection can be captured and then synchronized to match the same time the sampled output was taken. This creates a clean data set that can be used to train the neural net. The expert knowledge available can be used to reduce process inputs but the expert knowledge might not capture all of the highly nonlinear behaviour. The attempt to model the behvaiour may result in complex computations that may not be accurate enough to compare to the lab values. 

## Major Drawbacks of Design

The down side to using a neural net in this application is the lack of full variance of the data. It is costly to make changes to the plant in order to test for edge-cases. The data-sets operational ranges might be normal but the nonlinear relationships may only be understood given a wider variance of the inputs. Not exposing the neural net to these edge-cases could restric the ability of the network to capture the high dimensional patterns intrinsic to time variant behaviours. Capturing the data at synchronized time stamps helped to tie the output to known lab value results. These measurements where costly and limited the ability for larger sets of data to be captured. Only capturing 180 datasets with 33 input variables may not be enough. What ended up happening is tha the neural net began to overfit the given data and was not able to generalize enough. Performing the plant tests and creating potential outages may be too costly and not justify the work compared to just installing more sensors through out the process. 

## Comments and Suggestions

A possible improvement ot the implmenation woul dof been a continuous data cpature could of been implemented by building a script that would synchronize all input variables given a indexed time. The script will then allow operator inputs for the lab measurement. The measurements will then be aligned automatically with the timeseries inputs captured through the DCS historian. This method would of automatically created a more robust continous dataset that could then be used to "interpolate" gaps between the lab sampled values and the inputs that did not have a lab sample value. Different interpolation methods could of been implemented given expert engineering knowledge. The timeseries data could also be averaged, max'd, min'd, standard deviated, and added as inputs to the neural net training to capture time variant conditions such as ramp up or ramp down variability.

Another possible improvement would of been to create simulated edg-cases from engineering knowledge and feed it into a model based control system. The output of the model could be compared to the plat tests. The model could then be used to provide valid datasets and fill in the variability at the edge cases without having to incurr extra plant outages and push equipment to extreme limits.



