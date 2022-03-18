#nickiminaj

import random
pokemon1= str (input("Enter First Pokemon: "))
level1= int (input("Level : "))
spAtk= int (input("Attacking Pokemon Attack Stat: "))
power= int (input("Power : "))
pokemon2= str (input("Enter Second Pokemon: "))
level2= int (input("Level : "))
spDef= int (input("Pokemon Defense Stat: "))

#Modifier

print ("Type '0.5' if morethan 1 target \n"
       "Type '1' otherwise")
target= float(input(" TARGET : "))

print ("Type '1.5' if weather is beneficial to type \n"
       "Type '0.5' if weather is against to type; \n"
       "Type 1 otherwise")
weather= float (input(" WEATHER : "))

print(" Applied in Generation II only")
print ("Type '1.25' if Badge for the type is held by the player \n"
       "Type '1' otherwise")
badge= float(input(" BADGE: "))

print ("Type '2' for critical hit \n"
       "Type '1' otherwise")
critical= float (input(" CRITICAL: "))

rdm = random.uniform(0.85, 1)

print ("Same-type Attack Bonus \n"
       "Type '1.5' if move is similar to any type user's type; \n"
       "Type 1 otherwise")
stab= float(input(" STAB: "))

print ("EFFECTIVENESS \n"
       "0.5 - ineffective        0.25-0.5 - not very effective \n"
       "1 - normal               2 or 4 - super effective")
ptype= float (input(" TYPE: "))

print ("Type '0.5' if attacker is burned\n"
       "Type '1' otherwise")
burn= int (input("BURN: "))

other = 1;

#COMPUTATION
modifier = (target*weather*badge*critical*rdm*stab*ptype*burn*other)
damage = ((((((2 * level1 / 5) + 2) * power) * (spAtk / spDef))) / (50 + 2) * modifier)


if ptype == 0:
    print (pokemon1 + " attack deal is " + "ineffective to " + pokemon2)
elif ptype == 0.25:
    print (pokemon1 + " attack deal is " + "not very effective to " + pokemon2)
elif ptype == 0.5:
    print (pokemon1 + " attack deal is " + "not very effective to " + pokemon2)
elif ptype == 1:
    print (pokemon1 + " attack deal is " + "normal to " + pokemon2)
elif  ptype == 2:
    print (pokemon1 + " attack deal is " + "super effective to " + pokemon2)
elif  ptype == 4:
    print (pokemon1 + " attack deal is " + "super effective to " + pokemon2)    

print (pokemon1 + " dealt damage to " + pokemon2 + " is " + str(damage) )







