dic = {
    "name": 'Victor',
    "last_name": 'Fedatto',
    "age": 21,
    "gender": 'male',
    "city": "Joao Pessoa",
    "watch_list": ["Hunger Games", "Star Wars VIII", "FNAF 2"]
}

print(f"Name: {dic["name"]}")
print(f"Age: {dic["age"]}")
print(f"Watch List: {dic["watch_list"]}")

# Adicionar
dic["favorite_color"] = "Crimson Violet"
dic["color_hex"] = "#4E132C"
del dic["city"]

pares = dic.items() # 
pares_list = list(dic.items()) # 

print(pares)
print(pares_list)
print(pares_list[0])

