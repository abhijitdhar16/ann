# A Simple implementation of Artificial Neural Network (ANN)
Let us define two building blocks of our ANN. 
1.  Neuron
2.  Link
3.  Layer
### Neuron 
A neuron is a basic computing unit which can process a signal **s** (actually a floating point number), such that **0 <= s <= certain max value**, 
based on one more input signal(s). Output signal of a neuron can by simply 0 or 1.

### Link
Link is computing unit like a pipe, which connects two neurons by carrying output of one neuron to the input of another.
Additionally, a link has weight. Output/yield of the link is **input-signal * weight**. The link that does not have any neuron
at the input end, receives the signal form external world, and the link that does not have neuron at the output end sends
the signal to the output world.

![alt text](./images/ann.svg)

In the above diagram N1, N2, and N3 are neurones. L1 (w1), L2 (w2), L3 (w3), ... are the links with weights w1, w2, w3, ... w5 respectively.

### Layer
Layers are architectural element of ANN which groups the neurons such a way that next layer (or group of neurons) can start computations after all 
the neurons in the previous layer completed their computation.

# A sample simulation of ANN in python
This code base tried to implement above ANN using four classes. Of course, implementation of the classes will change due to optimization, above 
concept may change etc. in future. But for the time being we have four classes
1. neuron - to implement neuron
2. link - to implement link
3. timer - to replace layer
4. annErrors - to handle the run time errors.

Definition of each class is available on the top of each class in the file [neuron.py](./neuron.py).

