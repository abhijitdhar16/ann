# A Simple implementation of Artificial Neural Network (ANN)
Let us define two building blocks of our ANN. 
1.  Link
2.  Neuron
### Neuron 
A neuron is a basic computing unit which can generate a signal **s** (actually a floating point number), such that **0 <= s <= certain max value**, 
based on one more input signal(s).

### Link
Link is computing unit like a pipe, which connects two neurons by carrying output of one neuron to the input of another.
Additionally, a link has weight. Output/yleld of the link is **input-signal * weight**. The link that does not have any neuron
at the input end, receives the signal form external world, and the link that does not have neuron at the output end sends
the signal to the output world.

