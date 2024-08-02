states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]

cadena = "Mi estado favorito es Florida"
numeros = [2,4,5,7]


#evitando el estado de VERMONT
for state in states:
    if state ==  "Tennessee":
        continue
    print(f"I will visit {state}")
      
      
    
for state in states:
    if state ==  "Florida":
        break
    print(f"I will visit {state}")
    
    
#recorrer una cadena de texto

for letra in cadena :
    print(letra)
    
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)