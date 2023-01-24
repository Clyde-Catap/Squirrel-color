
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]

fur_color.sort_values()

gray = []

red = []

black = []

for g in fur_color:
    if g == "Gray":
        gray.append(g)

for r in fur_color:
    if r == "Cinnamon":
        red.append(r)

for b in fur_color:
    if b == "Black":
        black.append(b)
# print(type(len(gray)))

x = len(gray)
y = len(red)
z = len(black)

color_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [x, y, z]

}

#

colour = pandas.DataFrame(color_count)
colour.to_csv("squirrel_color.csv")
