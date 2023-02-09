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

    def __init__(self, b, h, expo, fck, yc, fyk, ys, Md, x_d):
        self.b = b
        self.h = h
        try:
            self.c = self.cracking_exposure_classes[expo]
        except KeyError:
            self.c = None

        self.fck = fck
        self.yc = yc
        self.fyk = fyk
        self.ys = ys
        self.Md = Md
        self.x_d = x_d
        # distance from tension reinforcement to top fibre
        self.ds1 = self.h - self.c
        # compression block depth
        self.x = self.ds1 * self.x_d

    @staticmethod
    def next_aprox(value, interval):
        """
        the provided real value will be approximated to the next higher value in a set of
        discrete equally spaced numbers within the real numbers. Ex: n = 3.426 --> 4; n = 5.659 --> 6
        :return:
        aprox: approximated value
        """
        a = int(value / interval) * value + value
        pass

    def As(self):
        """
        this function calculates the necessary reinforcement so the beam´s capacity is bigger
        than Md
        :return:
        prevAs1: is the tensioned reinforcement result
        prevAs2: is the compressed reinforcement result
        """

        z = self.ds1 - 0.8 * self.x / 2
        M = 0.8 * self.x * self.fck * self.b * z / self.yc
        prevAs1 = 0
        prevAs2 = 0
        # might look redundant but think of the case Md<M
        if self.Md > M:
            while self.Md > M:
                increAs1 = (self.Md - M) * self.ys / (z * self.fyk)  # passive reinforcement necessary
                prevAs1 += increAs1
                self.x = self.yc * (prevAs1 * self.fyk - prevAs2 * self.fyk) / (
                            self.ys * .8 * self.b * self.fck)  # recalculate neutral fibre.

                if self.x / self.ds1 > self.x_d:  # strain needs to be checked.
                    increAs2 = increAs1  # increment in top reinforcement is equal to the difference between
                    # the current As1 and the previous value for As1.
                    prevAs2 += increAs2

                M = (prevAs1 * self.fyk / self.ds1 - prevAs2 * self.fyk / self.c) / self.ys - 0.32 * self.x ** 2 * self.b * self.fck / self.yc

        else:
            prevAs1 = M * self.ys /(z * self.fyk)

        return prevAs1, prevAs2

    def reinforcement_layout(self, As):
        """
        the reinforcement is converted to actual comercial bars evenly spaced. only one bar is selected,
        :param As: is the passive reinforcement area you need to convert
        :return:
        n: number of bars
        bar: diameter of the comercial bar
        spacing: space in mm between bars
        """

        n = self.next_aprox(As, )
        pass


if __name__ == "__main__":
    beam = RectBeam(200, 300, 30, 25, 1.5, 500, 1.15, 50*1E6, 0.3)
    print(beam.As())