import datetime

class Counter:
    def __init__(self) -> None:
        self.marklist = []
        self.mm = 1
    
    def reset(self):
        self.marklist = []
    
    def start(self):
        self.startTime = datetime.datetime.now()

    def mark(self, id=None):
        markTime = datetime.datetime.now()
        if id == None: id="Mark "+str(self.mm)
        asp = [id, markTime]
        self.marklist.append(asp)
        self.mm += 1

    def end(self, show=False, marking=False):
        self.endTime = datetime.datetime.now()
        if show:
            self.show(marking)

    def show(self, marking=False):
        self.titlebar("Statistics")
        self.header("Points", "Time")
        self.liner("Start Time", str(self.startTime))
        self.liner("End Time", str(self.endTime))
        self.liner("Total Time Taken", str(self.endTime-self.startTime))
        
        if marking:
            self.titlebar("Markings")
            self.header("ID", "Mark Stamp", "Time From Previous Mark")
            self.liner("Start", str(self.startTime), "-")
            for index, ss in enumerate(self.marklist):
                if index==0:
                    self.liner(ss[0], str(ss[1]), str(ss[1] - self.startTime))
                else:
                    self.liner(ss[0], str(ss[1]), str(ss[1] - self.marklist[index-1][1]))
            self.liner("End", str(self.endTime), str(self.endTime - self.marklist[-1][1]))
        self.ender()
    
    def liner(self, a="", b="", c="-", d=""):
        print("| {:25}\t| {:25}\t| {:25}\t|{:1}".format(a, b, c, d))

    def titlebar(self, title="None"):
        x0 = "-"*31
        print(f"+{x0}+{x0}+{x0}+")
        print("| {:37}\t {:45}\t {:5}  |".format("", title, ""))
    
    def header(self, a="", b="", c="Not Used", d=""):
        x0 = "-"*31
        print(f"+{x0}+{x0}+{x0}+")
        print("| {:25}\t| {:25}\t| {:25}\t|{:1}".format(a, b, c, d))
        print(f"+{x0}+{x0}+{x0}+")
    
    def ender(self):
        x0 = "-"*31
        print(f"+{x0}+{x0}+{x0}+")