class Scaner:
    tokens = []
    tmp = []

    def scan(self,string):
        string = string.replace(" ","")
        self.prepare(string)
        self.tokens.remove("\n")
        return self.tokens    
   
    def prepare(self, string):
        if len(string) < 1:
            return self.tokens
        
        if len(string) > 1 and string[0].isdigit() or string[0]==".":
            self.tmp.append(string[0])
    
        else:
            if len(self.tmp) > 0:
                self.tokens.append(''.join(self.tmp))
            
            del self.tmp[:]
            self.tokens.append(string[0])
        
        string = string[1:]
        return self.prepare(string)
         
        
            
     
