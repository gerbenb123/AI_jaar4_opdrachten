# Zoals besproken in het college: een boer heeft een wolf, een geit en een kool. 
# Hij moet zichzelf met beide dieren en de kool naar de andere oever brengen. 
# Er is een kleine boot waarin hij slechts één ding tegelijk kan meenemen. 
# Echter, als de wolf en de geit alleen gelaten worden, eet de wolf de geit op. 
# Als de geit en de kool alleen gelaten worden, eet de geit de kool op.
#
# Schrijf een python programma dat alle oplossingen geeft. Het kan in minder dan 80 regels. Je hoeft geen GUI te
# maken, het mag gewoon met een CLI en gebaseerd op tekst.
# Enkele aanwijzingen. Een toestand (state) is een weergave van linker- en rechteroever. Bijvoorbeeld, 'FGCW|' is
# de begin-toestand en '|FGCW' de eindtoestand. Een toestand kan overgaan in een volgende toestand doordat
# de boer met een item de rivier oversteekt. Wanneer we de toestanden zien als knooppunten en de transities
# als takken krijgen we een boomstructuur (tree) die wel kunnen doorzoeken met DFS. Zie verder ook de sheets
# van het college.
# 
# Vraag: wat is de tijdcomplexiteit van je oplossing?

#boer geit kool vis
links = ["b","g","k","v"]
rechts = []
states = []
statecachelinks = []
statecacherechts = []



def links_to_rechts(letter,links,rechts):
        if(letter in links):
            links.remove(letter)
            links.remove("b")
            rechts.append(letter)
            rechts.append("b")
            return True
        

def rechts_to_links(letter,links,rechts):
    if letter == "b":
        rechts.remove(letter)
        links.append(letter)
    elif("b" in rechts):
        if(letter in rechts):
            rechts.remove(letter)
            rechts.remove("b")
            links.append(letter)
            links.append("b")
            return True

def boer_to_links():
    if("b" in rechts):
            rechts.remove("b") 
            links.append("b")


def check_state(links,rechts):
    if "v" in rechts and "k" in rechts and "b" in rechts:
        return True
    
    if "g" in links and "v" in links and  "b" in links and "k" in links:
        return False
    if "g" in links and "v" in links and "b" not in links:
        return False
    if"g" in links and "k" in links and "b" not in links:
        return False
    else:
        if "g" in rechts and "v" in rechts and "b" not in rechts:
            return False
        elif "g" in rechts and "k" in rechts and "b" not in rechts:
            return False
        else:
            return True
        
#isfinished funcite

def uitwerkings_functie(links,rechts,steps):
    if"g" in rechts and "k" in rechts and "b" in rechts and "v" in rechts:
        print("finished") 
        exit

    stap = steps
    states.append([links,rechts])
    print(states)
    links1= list(links)
    rechts1= list(rechts)
    print("stap:" , stap)
    #bepalen aan welke kant we staan
    if (stap % 2) == 0:
        for i in links1:
            if i != "b" :
                statecachelinks = list(links1)
                statecacherechts = list(rechts1)
                links_to_rechts(i,statecachelinks,statecacherechts)
                if check_state(statecachelinks,statecacherechts):
                    uitwerkings_functie(statecachelinks,statecacherechts,stap+1)
                else:
                    print("fout")
    else:  
        for i in rechts1:
            statecachelinks = list(links1)
            statecacherechts = list(rechts1)
            rechts_to_links(i,statecachelinks,statecacherechts)
            if check_state(statecachelinks,statecacherechts):
                uitwerkings_functie(statecachelinks,statecacherechts,stap+1)
            else:
                print("fout")
                
                
                
                    

     

    
    
        
uitwerkings_functie(links,rechts,0)   
print(states)   

       


