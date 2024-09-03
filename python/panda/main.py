import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur_color": ["grey", "Cinnamon", "Black"],
    "count": [grey_squirrels_count, Cinnamon_squirrels_count, Black_squirrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("new_data.csv")


