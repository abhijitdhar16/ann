#--------------------------------------------------------------------------------
# Testing the implementation of the neuron class using the architecture as shown
# below. The neurons X1, X2 and Y are connected like picture shown below
#
#        layer 1                   layer 2           layer 3
#        
#        +------+
#    i1  |      |l1
#   ---->|  X1  +--------+
#        |      +---+    |        +------+
#        +------+ l2|    +------->|      |  l5
#                   |             |  Y1  +-------+
#        +------+   |    +------->|      |       |    +-----+
#    i2  |      | l3|    |        +------+       +--->|     | o1
#   ---->|  X2  +---|----+        +------+            |  Z  +---->
#        |      ++  |             |      | l6    +--->|     |
#        +------+|l4+------------>|  Y2  +-------+    +-----+
#    b1          +--------------->|      |
#  ------------------------------>+------+
#
#
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

t1 = neuron.timer()
l1 = neuron.link(type = 'synapse')
l2 = neuron.link(type = 'synapse')
l3 = neuron.link(type = 'synapse')
l4 = neuron.link(type = 'synapse')
l5 = neuron.link(type = 'synapse')
l6 = neuron.link(type = 'synapse')
i1 = neuron.link(type = 'input')
i2 = neuron.link(type = 'input')
b1 = neuron.link(type = 'bias')
o1 = neuron.link(type = 'output')

x1 = neuron.neuron(
    threshold = 1,
    in_link   = [i1],
    out_link  = [l1, l2],
    layer     = 1,
    timer     = t1,
    name      = 'x1'
)

x2 = neuron.neuron(
    threshold = 1,
    in_link   = [i2],
    out_link  = [l3, l4],
    layer     = 1,
    timer     = t1,
    name      = 'x1'
)

y1 = neuron.neuron(
    threshold = 2,
    in_link   = [l1, l3],
    out_link  = [l5],
    layer     = 1,
    timer     = t1,
    name      = 'y1'
)

y2 = neuron.neuron(
    threshold = 1,
    in_link   = [l2, l4, b1],
    out_link  = [l6],
    layer     = 2,
    timer     = t1,
    name      = 'y2'
)

z1 = neuron.neuron(
    threshold = 1,
    in_link   = [l5, l6],
    out_link  = [o1],
    layer     = 3,
    timer     = t1,
    name      = 'z1'
)

l1.setWeight(1)
l2.setWeight(-1)
l3.setWeight(1)
l4.setWeight(-1)
l5.setWeight(1)
l6.setWeight(1)

b1.setWeight(1)
b1.setBiasInput(1)

for a in [0, 1] :
    for b in [0, 1] :
        t1.reset()
        t1.tick()
        x1.input([a])
        x2.input([b])
        x1.activate()
        x2.activate()
        t1.tick()
        y1.activate()
        y2.activate()
        t1.tick()
        z1.activate()
        print("a = %s  b = %s out = %s" % (a, b, z1.output()))
    # end for
# end for