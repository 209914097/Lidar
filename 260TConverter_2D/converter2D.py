import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

TH1 = 1
TR1 = 2
TH2 = 1
TR2 = 4
MH=8
MR=4
BH1 = 1
BR1 = 3
BH2=1

class converter:
    def __init__(self,TH1 = 1,TR1 = 2,TH2 = 1,TR2 = 4,MH=8,MR=4,BH1 = 1,BR1 = 3,BH2=1):
        self.TH1 = TH1
        self.TR1 = TR1
        self.TH2 = TH2
        self.TR2 = TR2
        self.MH = MH
        self.MR = MR
        self.BH1 = BH1
        self.BR1 = BR1
        self.BH2 = BH2
        self.Path = mpath.Path
        self.fig, self.ax = plt.subplots()



    def Lside(self,offset=0):

        return mpatches.PathPatch(
            self.Path([(-self.BR1, 0 + offset), (-self.MR, self.BH1 + offset),
            (-self.MR, self.BH1 + offset), (-self.MR,self.MH+self.BH1 + offset),
            (-self.TR2, self.MH+self.BH1 + offset), (-self.TR1, self.TH2 +self.MH+self.BH1 + offset),
            (-self.TR1, self.TH2 +self.MH+self.BH1 + offset), (-self.TR1, self.TH1+self.TH2 +self.MH+self.BH1 + offset)
                       ],
                      [self.Path.MOVETO, self.Path.LINETO,
                       self.Path.LINETO, self.Path.LINETO,
                       self.Path.LINETO, self.Path.LINETO,
                       self.Path.LINETO, self.Path.LINETO]
                      ),
            fc="none", transform=self.ax.transData)

    def Rside(self, offset=0):
        return mpatches.PathPatch(
            self.Path([(self.BR1, 0 + offset), (self.MR, self.BH1 + offset),
                       (self.MR, self.BH1 + offset), (self.MR, self.MH + self.BH1 + offset),
                       (self.TR2, self.MH + self.BH1 + offset), (self.TR1, self.TH2 + self.MH + self.BH1 + offset),
                       (self.TR1, self.TH2 + self.MH + self.BH1 + offset),(self.TR1, self.TH1 + self.TH2 + self.MH + self.BH1 + offset)
                       ],
                      [self.Path.MOVETO, self.Path.LINETO,
                       self.Path.LINETO, self.Path.LINETO,
                       self.Path.LINETO, self.Path.LINETO,
                       self.Path.LINETO, self.Path.LINETO]
                      ),
            fc="none", transform=self.ax.transData)

    def Bside(self,offset=0):
     return mpatches.PathPatch(
         self.Path([(-self.BR1, self.BH2+offset), (0, 0+offset), (self.BR1, self.BH2+offset)],
             [self.Path.MOVETO, self.Path.CURVE3, self.Path.CURVE3]),
        fc="none", transform=self.ax.transData)

    def label(self,offset=0):
        #------------水平箭头---------#
        self.ax.annotate('', (self.BR1, 0 + offset),
                         xytext=(-self.BR1, 0 + offset), arrowprops={'arrowstyle': "<->"})
        self.ax.text(0,  offset*1.15,str(self.BR1*2) , va="center", ha="center", rotation=0)

        self.ax.annotate('', (-self.MR, self.BH1 + offset),
                         xytext=(self.MR, self.BH1 + offset), arrowprops={'arrowstyle': "<->"})
        self.ax.text(0, self.BH1+offset *1.15, str(self.MR * 2), va="center", ha="center", rotation=0)

        self.ax.annotate('', (-self.TR1, self.TH2 + self.MH + self.BH1 + offset),
                         xytext=(self.TR1, self.TH2 + self.MH + self.BH1 + offset), arrowprops={'arrowstyle': "<->"})
        self.ax.text(0, self.TH2 + self.MH + self.BH1 + offset * 1.15, str(self.TR1 * 2), va="center", ha="center", rotation=0)

        # ------------垂直箭头---------#
        self.ax.annotate('', (-self.MR-self.MR/10, self.BH1 + offset),
                         xytext=(-self.MR-self.MR/10, self.MH+ self.BH1 + offset), arrowprops={'arrowstyle': "<->"})
        self.ax.text(-self.MR-self.MR/10- offset * 0.15, self.MH/2+ self.BH1 + offset, str(self.MH ), va="center", ha="center",
                     rotation=90)

        self.ax.annotate('', (+self.MR + self.MR / 10, 0 + offset/2),
                         xytext=(self.MR + self.MR / 10,  self.TH1 +self.TH2 + self.MH + self.BH1 + offset),
                         arrowprops={'arrowstyle': "<->"})
        self.ax.text(self.MR + self.MR / 10 + offset * 0.2, (self.TH1 +self.TH2 + self.MH + self.BH1+offset*3/2)/2, str(self.TH1 +self.TH2 + self.MH + self.BH1+ self.BH2),
                     va="center", ha="center",
                     rotation=90)

    def draw(self):

        self.ax.add_patch(self.Lside(offset=self.BH2))
        self.ax.add_patch(self.Rside(offset=self.BH2))
        self.ax.add_patch(self.Bside())
        self.ax.axis("equal")
        self.label(offset=self.BH2)
        plt.show()


C=converter(TH1 = 1.2,TR1 = 3.2,TH2 = 4,TR2 = 6.5,MH=10,MR=6.5,BH1 = 3,BR1 = 5.8,BH2=3)
C.draw()
