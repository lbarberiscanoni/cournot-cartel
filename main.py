from cournot import CournotModel
from defection import Defection

class Simulation:

    def results(self, a, b, c):
        model = CournotModel(a, b, c)
        defection = Defection(a, b, c)

        #print model.cournotEquilibrium(), model.monopolyEquilibrium()
        #print model.collusionIncentive(), "%"
        #print defection.profitDefection_loss, defection.profitDefection_win
        #print defection.victoryMargin, "%"
        print "matrix as a function of monopoly profits"
        print "(Fix, Fix)", (model.monopolyEquilibrium() / float(2)) / float(model.monopolyEquilibrium())
        print "(Cut, Fix)", defection.profitDefection_win / float(model.monopolyEquilibrium())
        print "(Fix, Cut)", defection.profitDefection_loss / float(model.monopolyEquilibrium())
        print "(Cut, Cut)", (model.cournotEquilibrium() / float(2)) / float(model.monopolyEquilibrium())

    def run(self):

        for a in range(5, 100):
            for b in range(1, 20):
                b = b * .1
                for c in range(1, a):
                    print "-------------------------"
                    print a, b, c
                    self.results(a, b, c)

Simulation().run()
