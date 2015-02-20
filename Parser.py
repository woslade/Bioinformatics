class Parser(object):
    
    def __init__(self, fileName):
        """
        self.file: the *.txt file containing sequences in fasta format
        self.result: dictionary used to store header:sequence information
        self.gcContent: dictionary used to store header:gcContent information for each entry
        """
        self.file = open(fileName)
        self.result = {}
        self.gcContent = {}
        
    def parse(self):
        """
        Input
        ---
        a *.txt file in fasta format
        
        Ouput
        ---
        self.result: a dictionary where the keys are the header information and
        the value is the sequence
        """
        for line in self.file:
            beginningFound = False
            
            if line.startswith(">"):
                beginningFound = True
                
                if beginningFound:
                    key = line.split('>')[-1].split('\n')[0]
                    self.result[key] = ''
                    beginningFound = False
            else:
                self.result[key] += line
                
    def clean(self):
        for key in self.result.keys():
            seq = ''.join(self.result[key].split('\n'))
            self.result[key] = seq
            
    def gc(self):
        for key in self.result.keys():
            temp = []
            self.gcContent[key] = []
            seq = self.result[key]
            
            for nt in seq:
                if nt == "G" or nt == "C":
                    temp.append(nt)
            self.gcContent[key] = float(len(temp)) / float(len(seq))
