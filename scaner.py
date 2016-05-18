#from __future__ import division

class Scaner:
    token_list = []
    n = []

    def scan(self, string):
        string = string.replace(" ", "")
        self.scan1(string)
        for i in range (0, len(self.token_list)-1):
            if i < len(self.token_list)-1:
                if  self.token_list[i+1] == ".":
                    self.token_list.pop(i+1)
                if self.token_list[i] == "-":
                    self.token_list[i] = "+"
                    self.token_list[i+1] = "-" + self.token_list[i+1]
                elif self.token_list[i] == "/":
                    self.token_list[i] = "*"
                    self.token_list[i+1] = (str)(1.0 / (float)(self.token_list[i+1]))
        self.token_list.remove("\n")
        return self.token_list            
    
    def sca(self,string):
        string = string.replace(" ","")
        self.test(string)
        self.token_list.remove("\n")
        return self.token_list    

    def scan1(self, string):
        if len(string) < 1:
            return self.token_list
        
        if len(string) > 1 and string[0].isdigit() and string[1].isdigit():
            self.n.append(string[0])
        
        elif len(string) > 2 and string[0].isdigit() and string[1] == "." and string[2].isdigit():
            self.n.append(string[0])
            self.n.append(".")
            #string.replace(".", "")
        
        elif string[0].isdigit():
            self.n.append(string[0])
            self.token_list.append(''.join(self.n))
            del self.n[:]
        else:
            self.token_list.append(string[0])
        string = string[1:]
        return self.scan1(string)
    
    def test(self, string):
        if len(string) < 1:
            return self.token_list
        
        if len(string) > 1 and string[0].isdigit() or string[0]==".":
            self.n.append(string[0])
    
        else:
            if(len(self.n)>0):
                self.token_list.append(''.join(self.n))
            del self.n[:]
            self.token_list.append(string[0])
        
        string = string[1:]
        return self.test(string)

    #def trim(string):
     #   string = string.replace(" ", "")
      #  string.remove("\n)          
        
            
     
