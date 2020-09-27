#Loes, Marja, Niels, Erik en Joep wonen in een gebouw met 5 verdiepingen, elk op een eigen verdieping. Loes
#woont niet in de bovenste verdieping. Marja woont niet op de begane grond. Niels woont niet op de begane
#grond en ook niet op de bovenste verdieping. Erik woont (tenminste één verdieping) hoger dan Marja. Joep
#woont niet op een verdieping één hoger of lager dan Niels. Niels woont niet op een verdieping één hoger of
#lager dan Marja. Waar woont iedereen?
import itertools

floors = "LMNEJ"

permutations =itertools.permutations(floors)
for a in list(permutations):
    #dit had je je natuurlijk beter een keer kunnen doen in variabelen en dan checken.
    #had vast ook anders gekund.
    if not a.index("L") == 4 and not a.index("M") == 0:
        if not a.index("N") == 4 and not a.index("N") == 0:
            if a.index("E") > a.index("M"):
                if a.index("J") > a.index("N")+1 or a.index("J") < a.index("N")-1:
                    if a.index("N") > a.index("M")+1 or a.index("N") < a.index("M")-1:
                        print(a)