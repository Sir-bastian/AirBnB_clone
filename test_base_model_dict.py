#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
<<<<<<< HEAD
my_model.name = "My_First_Model"
=======
my_model.name = "Holberton"
>>>>>>> 64999a53527c19229b2938550cca989d1ce86976
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
<<<<<<< HEAD
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
=======
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(my_model is my_new_model)

>>>>>>> 64999a53527c19229b2938550cca989d1ce86976