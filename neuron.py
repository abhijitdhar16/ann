import sys
#------------------------------------------------------------------------------
# Artificial neurons can be used to emulate simple logic functions like
# AND, OR, XOR etc. This library defines three simple class "neuron", "link"
# and "timer" to build a simple neural network and emulate logic functions.
#------------------------------------------------------------------------------
class annErrors () :
    def __init__(self) :
        self.errMsg = {}
        self.errMsg['001'] = """
        Cannot take input using 'input' method if the associated link type
        is not 'input'.
        """
        
        self.errMsg['002'] = """
        Cannot extract values from a link using 'output' method if the 
        respective link type is not 'output'.
        """
        
        self.errMsg['004'] = """
        An undefined link type specified. Valid link types are 'input',
        'output', and 'bias'.
        """
        
        self.errMsg['005'] = """
        Can not set a bias input using setBiasInput to a link which 
        is not a bias.
        """
    # end def
    
    def error (self, code) :
        print(self.errMsg[code])
        raise() 
    # end def
# end class    

#-------------------------------------------------------------------------------
# This class is used to emulate a neuron. The neuron class has the following 
# attributes or properties.
#    1) The lower threshold and upper threshold. If the total input is less than
#       the lower threshold or greater than the upper threshold then output of
#       the neurone is zero, one otherwise.
#    2) Array of incoming links.
#    3) Array of outgoing links.
#    4) The architectural layer in which the neuron belongs to.
#    5) The timer data structure that decides when this neuron should be 
#       activated.
# Methods (public)
#    1) input()    : Send input signal to the neuron.
#    2) output()   : Read output signal from the neuron.
#    3) activate() : activate the neuron. You will get the output after
#                    activating the neuron only.
# Methods (private)
#    1. __activation_func__ : This function actually does the "computation"
#                             inside the neuron.
# Assumption:
# Our activation function is a binary step function with threshold range
# min_threshold and max_threshold. Input within the threshold range yields 
# output 1, whereas Input outside the threshold yields output 0.
#------------------------------------------------------------------------------
class neuron (annErrors) :
    def __init__ (self, threshold_range, in_link, out_link, layer, timer, name = {}):
        self.name = name
        self.min_threshold = threshold_range[0]
        self.max_threshold = threshold_range[1]
        self.in_link = []
        self.out_link = []
        self.timer = timer
        self.layer = layer
        self.init_state = 0
 
        for l in in_link :                   
            self.in_link.append(l)
        # end for
            
        for o in out_link :
            self.out_link.append(o)
        # end for 
    # end def __init __ ()

    def input (self, value) :
        i = 0
        for val in value :
            if (self.in_link[i].type() == 'input') :
                self.in_link[i].send(val)
                i = i + 1
            else :
                annErr.error('001')
            # end for
        # end for            
    # end def

    def output (self)  :
        outlist = []
        for o in self.out_link :
            if o.type() == 'output' :
                outlist.append(o.get())
            else :
                annErr.error('002') 
            # end if
        # end for
        return outlist
    # end def

    def __activation_func__ (self, val) :
        if ((val >= self.min_threshold) and (val <= self.max_threshold)):
            return 1.0
        else :
            return 0.0
        # end if
    # end def    
    
    def activate (self) :
        total_in =  0
        for i in self.in_link :
            total_in = total_in + i.get()
        # end for
        output = self.__activation_func__(total_in)
        # end if
        if (self.timer.getTime()) >= self.layer :
            for o in self.out_link :
                if (o.type() == 'output') or (o.type() == 'input') :
                    o.send(output)
                else :
                    annErr.error('003')
                # end if
            # end for
        # end if
    # end def
# end class

#-------------------------------------------------------------------------------
# This class is used to emulate a link between two neuron. A link class must 
# have the property called weight. A signal passing through the link must be 
# multiplied by its weight.
#-------------------------------------------------------------------------------
class link (annErrors) :
    def __init__ (self, weight = 1, type = 'link') :
        self.weight = weight
        self.in_signal  = 0
        self.out_signal = 0
        if ((type == 'input')   or
            (type == 'output')  or
            (type == 'bias')) :
            self.link_type =  type
        else :
            annErr.error('004') 
        # end if
    # end def

    def send (self, val) :
        self.in_signal = val      
    # end def

    def get (self) :
        self.out_signal = self.in_signal * self.weight
        return self.out_signal
    # end def

    def type (self) :
        return self.link_type
    # end def

    def setWeight(self, value) :
        self.weight = value
    # end def
    
    def setBiasInput(self, val) :
        if (self.link_type == 'bias') :
            self.send(val)
        else :
            annErr.error('005')
        # end if
    # end def
# end class

#-------------------------------------------------------------------------------
# This class is used as timer which determine the sequence in which neurons
# should be fired. The set of neurons that are architecturally at the same 
# layer should be fired at the same time.
#-------------------------------------------------------------------------------
class timer () :
    def __init__ (self, max_layers) :
        self.current_time = 0
        self.max_layers = max_layers   
    # end def

    def tick(self):
        if (self.current_time <= self.max_layers):
            self.current_time = self.current_time + 1
            return self.current_time
        else:
            self.reset()
            return self.current_time
        # end if
    # end def
    
    def getTime (self):
        return self.current_time
    # end def

    def reset (self):
        self.current_time = 0
    # end def        
# end class
