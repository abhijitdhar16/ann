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
        self.timer = neuron.timer()

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
        print(self.y.output())

#-------------------------------------------------------------------------------
# End definition of AND neural network
#-------------------------------------------------------------------------------
nnet = my_network(thresholds=[(1,1), (1,1), (0, 1)])

nnet.set_weight1(1)
nnet.set_weight2(1)
for a in [0, 1] :
    for b in [0, 1] :
        nnet.set_input1(a)
        nnet.set_input1(b)
        nnet.process() 

