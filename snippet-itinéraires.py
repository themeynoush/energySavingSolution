#This liberary is avialble only inside the VM
import mobility
import json
# Put your token here
token = '72576909-6377-4962-8929-97bcedaf5d01'

# creating  carte.html
mob = mobility.Mobility(token)

# reading from the chosen panel in json format and name it "file"
with open('/home/etudiant612/Panels/panel_13.json', 'r') as file:

    # Read the contents of the file
    contents = file.read()

# Parse the JSON panel13
panel13 = json.loads(contents)

# Demonstrate the json's file contents
# print(panel13)

###########################################
##############PHASE2#######################
###########################################

# Extract the commuter's street address
stAddr = [commuter['adresse.Domicile.Premiere.Ligne.1'] for commuter in panel13]

# Extract the city's name
villes = [commuter['adresse.Domicile.Ville.1'] for commuter in panel13]

addressList = list(zip(homeAddr, villes))
print(addressList)

# call the function  addStarOnMap(self, coord, lab) for checking work location

Beaulieu=[48.12223311008758, -1.6389235808471818]
#mob.addStarOnMap(Beaulieu,"Campus de Beaulieu")

# Retrive your address's GEO location values 

#from class Mobility, call geocode function and put 'self' = 3 r Louis Armand
# and town: "Bruz" and put the values into a var called coord_domicile
p_i = 0
for addr in addressList:
    st = addr[0]
    ville = addr[1]
    coord_domicile = mob.geocode(st,ville)
    try:
        itineraires = mob.computeItinerary(coord_domicile,Beaulieu)
    except:
        continue
  
    with open('person_'+str(p_i)+'.json', 'w') as f:
    # Read the contents of the file
        json.dump(itineraires, f, indent=2)
        #print(json.dumps(itineraires, file=f) 
    p_i +=1
    #print(coord_domicile)
    
    #end of the main for
    

