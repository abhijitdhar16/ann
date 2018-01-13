#--------------------------------------------------------------------------------
# Testing the implementation of the neuron class using the architecture as shown
# below. The neurons X1, X2 and Y are connected like picture shown below
#
#        layer 1                   layer 2
#        
#        +------+
#        |      |
#   ---->|  X1  +--------+
#        |      |        |        +------+
#        +------+        +------->|      |
#                                 |  Y   +--------->
#        +------+        +------->|      |
#        |      |        |        +------+
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
#--------------------------------------------------------------------------------
import neuron

#--------------------------------------------------------------------------------
# Define your nural network architecture
#   1) one timer - t
#   2) Two synapses - l1 and l2
#   3) Two inputs - i1 and i2
#   4) One output - o
#   5) Two neurons - x1 and x2
#--------------------------------------------------------------------------------

# Define timer
timer = neuron.timer()

# Define link L1 i.e. X1 --> Y
l1 = neuron.link(type = 'synapse')

# Define link L2 i.e. X1 --> Y
l2 = neuron.link(type = 'synapse')

# Input is also a link
i1 = neuron.link(type = 'input')

# Input is also a link
i2 = neuron.link(type = 'input')

# output
o = neuron.link(type = 'output')

# Define neuron x1
x1 = neuron.neuron(
    threshold = 1, 
    in_link   = [i1],
    out_link  = [l1], 
    layer     = 1,
    timer     = timer, 
    name      = 'x1'
)

# Define neuron x2
x2 = neuron.neuron(
    threshold = 1, 
    in_link   = [i2],
    out_link  = [l2], 
    layer     = 1,
    timer     = timer, 
    name      = 'x2'
)

# Define neuron Y
y = neuron.neuron(
   threshold = 2.0,
   in_link   = [l1, l2],
   out_link  = [o], 
   layer     = 2,
   timer     = timer,
   name      = 'y1'
)

#-------------------------------------------------------------------------------
# End defination of AND neural network
#-------------------------------------------------------------------------------


l1.setWeight(1)
l2.setWeight(1)
for a in [0, 1] :
    for b in [0, 1] :
        timer.reset()
        timer.tick()
        x1.input([a])
        x2.input([b])
        x1.activate()
        x2.activate()
        timer.tick()
        y.activate()
        print(y.output())
    # end for
# end for


l1.setWeight(2)
l2.setWeight(2)
for a in [0, 1] :
    for b in [0, 1] :
        timer.reset()
        timer.tick()
        x1.input([a])
        x2.input([b])
        x1.activate()
        x2.activate()
        timer.tick()
        y.activate()
        print(y.output())
    # end for
# end for




