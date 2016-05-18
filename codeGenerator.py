class CodeGenerator:
    tmpCommands = []

    def searchTree(self, node):
        if node is not None:
            self.searchTree(node.left)
            self.searchTree(node.right)
            self.tmpCommands.append(node.value)	
	    

    def createCommands(self, node):
        #print node        
        commands = []
        self.searchTree(node)      
        
        for item in self.tmpCommands:
            if item == "+":
                commands.append("add")
            elif item == "*":
                commands.append("mul")
            elif item == "-":
				commands.append("sub")
            elif item == "/":
				commands.append("div")
            elif item == "%":
				commands.append("mod")
            elif item == "^":
				commands.append("pow")
            elif item is not None:
                commands.append("put " + item)
        
        commands.append("end")
        return commands

