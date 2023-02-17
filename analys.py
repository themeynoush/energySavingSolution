#This liberary is avialble only inside the VM
import mobility
import json


# Read the contents of the file 
# For each commuter, read their data
# And then create a dictionary 
# Which ontains only useful useful information 

        
# We're going to change the range to (15)
# These are the values per user

for p_i in range (1):
    sum_person_1 = {} 
    with open('/home/etudiant612/pages_etudiant/person_'+str(p_i)+'.json', 'r') as file:
        
        # personData is equvalent to each person's json file
        personData = json.load(file)
        
        # Question 1
        print('\nQuestion 1: le coût carbone d’un trajet en voiture')
        co2_emission = personData['context']['car_direct_path']['co2_emission']['value']
        print(co2_emission)
        
        # Question 2
        print('\nQuestion 2: le temps de transport en voiture')
        car_value = personData['journeys'][0]['durations']['car']

        if car_value != 0 :
            print(car_value,'\n')

        
        # Question 3
        print('\nQuestion 3: des possibilités de transport doux (marche, vélo)')
        mode = personData['journeys'][0]['sections'][0]['mode']
        print(mode,'\n')
        
        # This must be defined per journey
        sections = personData['journeys'][0]['sections']
        
        for section in sections:
            path_type = section['type']
            print(path_type)
        
        # Question 4
        print('\nQuestion 4: le temps de transport de chacun des itinéraires et les modes de transport utilisés')
 
        transportation_time = personData['journeys'][0]['arrival_date_time']
        print(transportation_time,'\n')
        

        # Question 5
        # Sur votre panel, de combien peut-on potentiellement réduire le bilan carbone si les usagers
        # basculent sur un mode doux ou transport en commun et combien de temps de transport supplémentaire 
        # cela implique ?

        # define a var called distance, check if 
        # distance = personData['journeys'][0]['distances'] 

        # check the condition in case the commuter switches to soft transport
        # if distance <= 2:
        #     # walk
        # elif distance >= 4:
        #     #go by car
        # else
        #     #go by bike
        
        # Calculate the emission reduction
        # considering 6 litres d’essence / 100km et 2317 gEC/litre

        # emission value when the commuter takes soft_emission
        # soft_emission = 

        # Subtract co2_emission value where condition soft_transport exist 
        # co2_reduction =  co2_emission - soft_emission

        # print(co2_reduction)

        # calculte the extra time when the commuter takes the soft transport 
        
        # print(extra_time)


        sum_person_1['co2_emission: '] = co2_emission
        sum_person_1['time_by_car: '] = car_value
        sum_person_1['soft_transport: '] = path_type
        sum_person_1['transportation_time: '] = transportation_time
        
        print ('\n', sum_person_1)
        

