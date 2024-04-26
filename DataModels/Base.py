from datetime import datetime
from bson.objectid import ObjectId
from Interface.IPyMongoDb import IPyMongoDb


class Base(IPyMongoDb):

    def __init__(self):
        self.internal_id = ObjectId()
        self.created_at = datetime.now()
        
    def to_dict(self):
        pass
    
    @staticmethod
    def from_dict(dictionary):
        pass

