import csv

data = [
    ["keyword", "name", "context", "year"],
    ["mausoleum", "Kwame Nkrumah Mausoleum",
     "Built in 1992 to honour Ghana's first president and the architect of Pan-Africanism. The black granite obelisk symbolises eternal remembrance.",
     "1992"],
    ["slave", "Cape Coast Castle",
     "A UNESCO World Heritage Site. Once a hub of the trans-Atlantic slave trade. Now a museum that confronts that history with dignity and education.",
     "1653"],
    ["food", "Jollof Rice",
     "A West African staple. Tomato-based rice cooked with spices and often paired with grilled chicken or beef. Ghana and Nigeria have a friendly rivalry over whose version reigns supreme.",
     "—"],
    ["kente", "Kente Cloth",
     "Handwoven silk and cotton from the Ashanti and Ewe people. Every colour and pattern carries meaning. The most famous African textile in the world.",
     "1700s"]
]

with open("facts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("facts.csv created successfully!")