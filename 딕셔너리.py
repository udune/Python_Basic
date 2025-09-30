names = ["철수", "영희", "민수"]
scores = [90, 95, 100]

scores_dict = {
    "철수": 90,
    "영희": 95,
    "민수": 100
}

print(scores_dict["철수"])  # 90
print(scores_dict["영희"])  # 95
print(scores_dict["민수"])  # 100

scores_dict["철수"] = 100
print(scores_dict)  # {'철수': 100, '영희': 95, '민수': 100}

print(scores_dict.keys())  # dict_keys(['철수', '영희', '민수'])
print(scores_dict.values())  # dict_values([100, 95, 100])
print(scores_dict.items())  # dict_items([('철수', 100), ('영희', 95), ('민수', 100)])

for key, value in scores_dict.items():
    print(key, value)  # 철수 100 영희 95 민수 100
    
