class Defection:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        qMonopoly = (self.a - self.c) / float(2 * self.b)
        q1 = qMonopoly / float(2)
        q2_reactive = ((self.a - self.c) / float(2 * self.b)) - (q1 / float(2))
        Q = q1 + q2_reactive

        Price = self.a - (self.b * Q)

        self.profitDefection_win = (Price * q2_reactive) - (self.c * q2_reactive)
        self.profitDefection_loss = (Price * q1) - (self.c * q1)

        victoryMargin = self.profitDefection_win / float(self.profitDefection_loss)
        self.victoryMargin = (victoryMargin - 1) * 100


