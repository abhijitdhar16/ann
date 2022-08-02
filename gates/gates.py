import  sys
sys.path.append("../")

import neuron
#-------------------------------------------------------------------------------
# Define your neural network architecture
#   1) one timer - t
#   2) Two synapses - l1 and l2
#   3) Two inputs - i1 and i2
#   4) One output - o
#   5) Two neurons - x1 and x2
#-------------------------------------------------------------------------------
class my_network () :
    #---------------------------------------------------------------------------
    # Testing the implementation of the neuron class using the architecture 
    # as shown below. The neurons X1, X2 and Y are connected like picture below
    #
    #        layer 1                   layer 2
    #
    #        +------+
    #    i1  |      | l1
    #   ---->|  X1  +--------+
    #        |      |        |        +------+
    #        +------+        +------->|      |
    #                                 |  Y   +--------->
    #        +------+        +------->|      |  o1
    #    i2  |      | l2     |        +------+
    #   ---->|  X2  +--------+
    #        |      |
    #        +------+
    #
    #  1) The weight between the connection X1 --> Y (L1) is 1.
    #  2) The threshold value of X1 is 1.
    #  3) The weight between the connection X2 --> Y (L2) is 1.
    #  4) The threshold value of X2 is 1
    #  5) The threshold value of Y is 1.
    #
    # The python code below represents this entire scenario.
    #---------------------------------------------------------------------------

    def __init__(self, thresholds) :
        # No loop fixed layer neurone
        num_layer = 2

        # Define timer
        self.timer = neuron.timer(max_layers=num_layer)

        # Define link L1 i.e. X1 --> Y
        self.l1 = neuron.link(type='input')

        # Define link L2 i.e. X1 --> Y
        self.l2 = neuron.link(type='input')

        # Input is also a link
        self.i1 = neuron.link(type='input')

        # Input is also a link
        self.i2 = neuron.link(type='input')

        # output
        self.o = neuron.link(type='output')

        # Define neuron x1
        self.x1 = neuron.neuron(
            threshold_range=thresholds[0],
            in_link=[self.i1],
            out_link=[self.l1], 
            layer=1,
            timer=self.timer, 
            name='x1'
        )

        # Define neuron x2
        self.x2 = neuron.neuron(
            threshold_range=thresholds[1],
            in_link=[self.i2],
            out_link=[self.l2], 
            layer=1,
            timer=self.timer, 
            name='x2'
        )

        # Define neuron Y
        self.y = neuron.neuron(
            threshold_range =  thresholds[2],
            in_link=[self.l1, self.l2],
            out_link=[self.o], 
            layer=2,
            timer=self.timer,
            name='y1'
        )
    
    def set_input1(self, val):
        self.x1.input([val])

    def set_input2(self, val):
        self.x2.input([val])
   
    def set_weight1(self, val):
        self.l1.setWeight(val)

    def set_weight2(self, val):
        self.l2.setWeight(val)

    def process(self):
        self.timer.reset()
        self.timer.tick()
        self.x1.input([a])
        self.x2.input([b])
        self.x1.activate()
        self.x2.activate()
        self.timer.tick()
        self.y.activate()
        retval = self.y.output()
        return retval

#-------------------------------------------------------------------------------
# End definition of AND neural network
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# The above neural network can be used to implement simple logic gate, like 
# and, or, xor, nand and not . We only changed the activation threshold range 
# of the neuron Y.
#-------------------------------------------------------------------------------
print("-----------------------------------------------")
print("use of neural network to implement logic gates")
print("-----------------------------------------------\n")


#-------------------------------------------------------------------------------
# Define activation function of the all the three neurons of the our neural
# network N1, N2, N3 respectively. 
#             +---->
#             | = 1  (1.0 <= x <= 1) 
#     f (x) = + 
#             | = 0  x < 1.0 or > 1
#             +---->
# Assumption - activation function is same for all the neurons. We will only
#              adjust weights of the links to implements the gates.
# Note:
#      There are three neurons.
#      => there are three activation functions - one per neuron.
#      => We need a list of three tuples to specify max and min each neuron's
#         activation function. (In each tuple first value defines the 
#         min_threshold and second value defines the max_threshold of the 
#         activation function.
#-------------------------------------------------------------------------------
nnet = my_network(thresholds=[(0.1, 1), (0.1, 1), (0.1, 1)])
print("""Threshold function is defined as :
             +---->
             | = 1  (1.0 <= x <= 1)
     f (x) = +
             | = 0  x < 1.0 or > 1
             +---->
for all neurons.
""")

#-------------------------------------------------------------------------------
# Implementation of OR gate. Adjust the link weights to implement OR gate.
#-------------------------------------------------------------------------------
print("Implementation of OR gate")
nnet.set_weight1(0.5)
nnet.set_weight2(0.5)
for a in [0, 1] :
    for b in [0, 1] :
        nnet.set_input1(a)
        nnet.set_input1(b)
        retval = nnet.process()
        print("%s or %s = %s" %(a, b, retval))
print("\n")

#-------------------------------------------------------------------------------
# Implementation of AND gate. Adjust the link weights to implement AND gate.
#-------------------------------------------------------------------------------
print("Implementation of AND gate")
nnet.set_weight1(.06)
nnet.set_weight2(.06)
for a in [0, 1] :
    for b in [0, 1] :
        nnet.set_input1(a)
        nnet.set_input1(b)
        retval = nnet.process()
        print("%s and %s = %s" %(a, b, retval))
print("\n")

#-------------------------------------------------------------------------------
# Implementation of XOR gate. Adjust the link weights to implement XOR gate.
#-------------------------------------------------------------------------------
print("Implementation of XOR gate")
nnet.set_weight1(1.0)
nnet.set_weight2(1.0)
for a in [0, 1] :
    for b in [0, 1] :
        nnet.set_input1(a)
        nnet.set_input1(b)
        retval = nnet.process()
        print("%s xor %s = %s" %(a, b, retval))
print("\n")

#-------------------------------------------------------------------------------
# Implementation of NOT gate. Implementation of not gate is bit tricky. It
# is basically a NAND gate with one of the input always 1. Say input 1 is 
# always 1.
#-------------------------------------------------------------------------------
print("Implementation of NOT gate")
nnet.set_weight1(1)
nnet.set_weight2(.75)
for b in [0, 1] :
    nnet.set_input1(1)
    nnet.set_input1(b)
    retval = nnet.process()
    print("%s not = %s" %(b, retval))
print("\n")

print("-----------------------------------------------")

