class CournotModel:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perfectCompetitiveEquilibrium(self):
        qEfficient = (self.a - self.c) / float(self.b)

        return qEfficient

    def cournotEquilibrium(self):
        qCournout = (2 / float(3)) * self.perfectCompetitiveEquilibrium()
        pCournout = (self.a  + (2 * self.c)) / float(3)
        profitCournout = (pCournout * qCournout) - (self.c * qCournout)

        return profitCournout

    def monopolyEquilibrium(self):
        qMonopoly = (self.a - self.c) / float(2 * self.b)
        pMonopoly = (self.a + self.c) / float(2)
        profitMonopoly = ((self.a - (self.b * qMonopoly)) * qMonopoly) - (self.c * qMonopoly)

        return profitMonopoly

    def collusionIncentive(self):
        collusionIncentive = self.monopolyEquilibrium() / float(self.cournotEquilibrium())
        collusionIncentive = (collusionIncentive - 1) * 100

        return collusionIncentive
