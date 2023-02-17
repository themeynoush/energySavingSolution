# coding: utf-8
import mobility

#Mettre ici votre token Navitia
token = '72576909-6377-4962-8929-97bcedaf5d01'
mob = mobility.Mobility(token)
coord_domicile = mob.geocode("3 r Louis Armand","Bruz")
print(coord_domicile)

#Ajout de la position sur la carte
mob.addMarkerOnMap(coord_domicile,"3 r Louis Armand")


#Ecriture de la carte dans pages_etudiant/carte.html 
mob.saveMap()