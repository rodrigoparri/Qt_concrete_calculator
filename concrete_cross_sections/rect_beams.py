from math import sqrt
class RectBeam:

    cracking_exposure_classes = {
        "X0": 0.4,
        "XC1": 0.4,
        "XC2": 0.3,
        "XC3": 0.3,
        "XC4": 0.3,
        "XD1": 0.2,
        "XD2": 0.2,
        "XD3": 0.2,
        "XS1": 0.2,
        "XS2": 0.2,
        "XS3": 0.1,
        "XF1": 0.3,
        "XF2": 0.2,
        "XF3": 0.3,
        "XF4": 0.2,
        "XA1": 0.2,
        "XA2": 0.1,
        "XA3": 0.1,
    }
    c = {
        "X0": 15,
        "XC1":20,
        "XC2":20,
        "XC3":20,
        "XC4":20,
        "XD1":35,
        "XD2":35,
        "XD3":35,
        "XS1":25,
        "XS2":30,
        "XS3":45,
        # "XF1":,
        # "XF2":,
        # "XF3":,
        # "XF4":,
        # "XA1":,
        # "XA2":,
        # "XA3":
    }
    steel = {
        6: 28.27,
        8: 50.27,
        10: 78.54,
        12: 113.10,
        14: 153.94,
        16: 201.06,
        20: 314.16,
        25: 490.87,
        32: 804.25,
        40: 1256.64
    }

    def __init__(self, b, h, expo, fck, yc, fyk, ys, dg, Md, x_d):
        self.b = b
        self.h = h
        try:
            self.c = self.c[expo]
        except KeyError:
            self.c = 30

        self.fck = fck
        self.yc = yc
        self.fcd = self.fck / self.yc
        self.fyk = fyk
        self.ys = ys
        self.fyd = self.fyk / self.ys
        self.dg = dg
        self.Md = Md * 1E6
        self.x_d = x_d
        # distance from tension reinforcement to top fibre
        self.ds1 = self.h - self.c
        # compression block depth introduced by the user
        self.x = self.ds1 * self.x_d
        self.y = 0.8 * self.x

    @staticmethod
    def next_aprox(value, interval):
        """
        the provided real value will be approximated to the next higher value in a set of
        discrete equally spaced numbers within the real numbers. Ex: n = 3.426 --> 4; n = 5.659 --> 6
        :return:
        aprox: approximated value
        """
        a = int(value / interval) * value + value
        return a

    def As(self):
        """
        this function calculates the necessary reinforcement so the beam´s capacity is bigger
        than Md
        :return:
        prevAs1: is the tensioned reinforcement result
        prevAs2: is the compressed reinforcement result
        """

        # compression block depth needed for solicitation Md
        y = (-self.b*self.ds1*self.fcd+sqrt(
            pow(self.b*self.ds1*self.fcd,2) - 2*self.b*self.fcd*self.Md)) / -(self.b * self.fcd)

        As1 = self.y * self.b * self.fcd / self.fyd
        As2 = 0

        # check if user´s compression depth is enough
        if y > self.y:
            incre_y = y - self.y
            increAs = incre_y * self.b * self.fcd / self.fyd
            As1 += increAs
            As2 += increAs

        return As1, As2

    def reinforcement_layout(self, As):
        """
        the reinforcement is converted to actual comercial bars evenly spaced. only one bar is selected,
        :param As: is the passive reinforcement area you need to convert
        :return:
        n: number of bars
        bar: diameter of the comercial bar
        spacing: space in mm between bars
        """
        for bar in self.steel:
            As_phi = self.steel[bar]
            # calculate the number of bars
            n = As / As_phi
            # aproximate the number to the next higher integer
            n_phi = self.next_aprox(n, 1)
            # calculate the width of all the bars and spacings
            b = n_phi * As_phi + 2 * self.c + (n_phi - 1) * (self.dg + 5)

            if self.b >= b:
                return n, bar

        pass
if __name__ == "__main__":
    beam = RectBeam(200, 300, "X0", 25, 1.5, 500, 1.15, 100, 0.3)
    print(beam.As())