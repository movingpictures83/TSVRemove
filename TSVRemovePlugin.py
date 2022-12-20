import PyIO
import PyPluMA
class TSVRemovePlugin:
    def input(self, infile):
       self.parameters = PyIO.readParameters(infile)
       self.tsvfile = open(PyPluMA.prefix()+"/"+self.parameters["tsvfile"], 'r')
       self.indexfile = open(PyPluMA.prefix()+"/"+self.parameters["indexfile"], 'r')

    def run(self):
       self.rows = []
       self.cols = []
       for line in self.indexfile:
           contents = line.strip().split('\t')
           if (contents[0] == "row"):
               self.rows.append(int(contents[1]))
           elif (contents[0] == "column"):
               self.cols.append(int(contents[1]))
       self.tsvcontents = []
       pos = 0
       for line in self.tsvfile:
           contents = line.strip().split('\t')
           contents2 = []
           if (pos not in self.rows):
              for i in range(len(contents)):
                  if (i not in self.cols):
                      contents2.append(contents[i])
              self.tsvcontents.append(contents2)
           pos += 1
    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        for i in range(len(self.tsvcontents)):
            for j in range(len(self.tsvcontents[i])):
                outfile.write(self.tsvcontents[i][j])
                if (j == len(self.tsvcontents[i])-1):
                    outfile.write('\n')
                else:
                    outfile.write('\t')
