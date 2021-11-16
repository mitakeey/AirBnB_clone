#!/usr/bin/python3
"""
Defines all common attributes for other classes
"""
import json
import uuid
from datetime import datetime
from pathlib import Path


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs["id"]
            self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%d %H:%M:%S.%f")
            self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%d %H:%M:%S.%f")
            self.name = kwargs["name"]
            self.my_number = kwargs["my_number"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        return f"{self.__class__} {self.id} {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at,
            **self.__dict__  # appends
        }


class FileStorage:
    __file_path = Path("file.json")
    __objects = {}

    """
    check if at creation, __objects is empty
    insert an object, then that the object was insert
    """

    def all(self):
        return self.__objects

    """
    Does not have a implicit test case
    """

    def new(self, obj: BaseModel):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    """
    Check if a new file was created after save operation
    Check for the last edit time
    if we know the state of the file before saving, then we can compare
    """

    def save(self):
        with open(self.__file_path, mode="a", newline="\n") as file:
            json.dump(self.__objects, file, default=str,)

    """
    Check that __objects has elements after reload
    """

    def reload(self):
        if self.__file_path.exists():
            pass


# private instance method
# def __str__(self):
# print [<class name>] (<self.id>) <self.__dict__>

# my_model = BaseModel(
#     **{"id": "gagged", "name": "Lucien", "my_number": 45, "created_at": "2021-11-13 08:14:51.195287",
#        "updated_at": "2021-11-13 08:14:51.195287"})
my_model = BaseModel()
storage = FileStorage()
my_model.name = "My First Model"
my_model.my_number = 89
storage.new(my_model)
storage.save()

# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
#
#
# def func(*args, **kwargs):
#     print(kwargs["age"], args[0])
#
#
# kw = {"age": 12, "name": "lucien", "gender": "male"}
# func(1, 2, 3, 4, 5, 6, 7, 8, age=12, name="lucien")
