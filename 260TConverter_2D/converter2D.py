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

    # def Top1(self,offset=0):
    #     return mpatches.PathPatch(
    #         self.Path([(-self.TR1, self.TH1+offset), (-self.TR1, 0+offset), (self.TR1, self.TH1+offset), (self.TR1, 0+offset)],
    #              [self.Path.MOVETO, self.Path.LINETO, self.Path.MOVETO, self.Path.LINETO]),
    #         fc="none", transform=self.ax.transData)
    # def Top2(self,offset=0):
    #     return  mpatches.PathPatch(
    #         self.Path([(-self.TR1, self.TH2+offset), (-self.TR2, 0+offset), (self.TR1, self.TH2+offset), (self.TR2, 0+offset), ],
    #          [self.Path.MOVETO, self.Path.LINETO, self.Path.MOVETO, self.Path.LINETO]),
    #     fc="none", transform=self.ax.transData)
    #
    # def M(self,offset=0):
    #     return mpatches.PathPatch(
    #         self.Path([(-self.MR, self.MH+offset), (-self.MR, 0+offset), (self.MR, MH+offset), (self.MR, 0+offset)],
    #          [self.Path.MOVETO, self.Path.LINETO, self.Path.MOVETO, self.Path.LINETO]),
    #     fc="none", transform=self.ax.transData)
    #
    # def Bot1(self,offset=0):
    #  return mpatches.PathPatch(
    #      self.Path([(-self.MR, self.BH1 +offset), (-self.BR1, 0+offset), (self.MR, self.BH1+offset), (self.BR1, 0+offset)],
    #          [self.Path.MOVETO, self.Path.LINETO, self.Path.MOVETO, self.Path.LINETO]),
    #     fc="none", transform=self.ax.transData)
    # def Bot2(self,offset=0):
    #  return mpatches.PathPatch(
    #      self.Path([(-self.BR1, self.BH2+offset), (0, 0+offset), (self.BR1, self.BH2+offset)],
    #          [self.Path.MOVETO, self.Path.CURVE3, self.Path.CURVE3]),
    #     fc="none", transform=self.ax.transData)

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
    def draw(self):
        # self.ax.add_patch(self.Bot2())
        # self.ax.add_patch(self.Bot1(offset=self.BH2))
        # self.ax.add_patch(self.M(offset=self.BH2+self.BH1))
        # self.ax.add_patch(self.Top2(offset=self.BH2 + self.BH1 + self.MH))
        # self.ax.add_patch(self.Top1(offset=self.BH2 + self.BH1 + self.MH + self.TH2))

        self.ax.add_patch(self.Lside(offset=self.BH2))
        self.ax.add_patch(self.Rside(offset=self.BH2))
        self.ax.add_patch(self.Bside())
        self.ax.axis("equal")

        plt.show()


C=converter(TH1 = 1.2,TR1 = 3.2,TH2 = 4,TR2 = 6.5,MH=10,MR=6.5,BH1 = 3,BR1 = 5.8,BH2=3)
C.draw()