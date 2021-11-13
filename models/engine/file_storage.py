import json
from pathlib import Path

from ..base_model import BaseModel


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
            json.dump(self.__objects, file)

    """
    Check that __objects has elements after reload
    """
    def reload(self):
        if self.__file_path.exists():
            pass
