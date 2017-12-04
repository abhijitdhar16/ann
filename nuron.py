class timer () :
    def __init__ (self) :
        self.current_time = 0
    # end def

    def tick(self) :
        self.current_time = self.current_time + 1
        return self.current_time
    # end def
    
    def getTime (self):
        return self.current_time
    # end def        
# end class    

class nuron () :
    def __init__ (self, threshold, in_link, out_link, layer, timer, name = {}):
        self.name       = name
        self.threshold  = threshold
        self.in_link    = []
        self.out_link   = []
        self.timer      = timer
        self.layer      = layer
        self.init_state = 0 
        if ((type(in_link) != type([])) and (type(in_link) != type([]))) :
            rise ("in_link or out_link type is not list")
        else :
            for l in in_link :                   
                self.in_link.append(l)
            # end for
            
            for o in out_link :
                self.out_link.append(o)
            # end for            
        # end if        
    # end def __init __ ()
 
    def activation_func (self, val) :
        if val >= self.threshold :
            return 1.0
        else :
            return 0.0
        # end if
    # end def    
    
    def activate (self) :
        total_in =  0
        for i in self.in_link :
            if (self.isFloatOrInt(i) == 1):
               total_in = total_in + i
            else :
               total_in = total_in + i.get()
            # end if
        # end for
        
        if (total_in >= self.threshold) : 
            output = self.activation_func(total_in)
        else : 
            output = 0.0
        # end if
        out_link_len = len(self.out_link)  
                     
        if (self.timer.getTime()) >= self.layer :
            if (out_link_len > 0):
               for o in self.out_link :
                   o.send(output)
                # end for
            else :
                self.out_link.append(output)
            # end if
        # end if
    # end def
    
    def isFloatOrInt(self, val) :
        if ((type(val) == type(1)) or (type(val) == type(1.0))) :
            return 1
        # end if
        return 0
    # end def
 
    #--------------------------------------------------------------------------
    # DEBUG
    #--------------------------------------------------------------------------
    def debug_in (self) :
        for i in self.in_link :
            if (self.isFloatOrInt(i) == 1):
                print("\tin = %s" %(i))
            else :
                print("\tin = %s" %(i.get()))
            # end if
        # end for        
    # end def

    def debug_out (self) :    
        print("outputs")
        for o in self.out_link :
            if (self.isFloatOrInt(o) == 1):
                print("\tout = %s" %(o))
            else :
                print("\tout = %s" %(o.get()))
            # end if
        # end for    
    # end if
    
    def debug_gen (self) :
        print("name      = %s" %(self.name))
        print("threshold = %s" %(self.threshold))
        print("time      = %s" %(self.timer.getTime()))
    # end def
    
    def debug (self) :
        print("------------------")
        self.debug_gen()
        self.debug_in()
        self.debug_out()
        print("------------------")
    # end def        
# end class    

class link () :
    def __init__ (self, weight) :
        self.wait = weight
        self.in_signal  = 0
        self.out_signal = 0        
    # end def

    def send (self, val) :
       self.in_signal = val
    # end def

    def get (self) :
        self.out_signal = self.in_signal *  self.wait
        return self.out_signal
    # end def
# end class

