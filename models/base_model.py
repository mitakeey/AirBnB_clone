#!/usr/bin/python3
"""
Defines all common attributes for other classes
"""
class BaseModel :
    database = []
#Instance attributes
    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = created_at
        self.updated_at = updated_at
#private instance method
  def __str__(self):
      print [<class name>] (<self.id>) <self.__dict__>

      
