from datetime import datetime
from bson.objectid import ObjectId
from Interface.IPyMongoDb import IPyMongoDb


class Base(IPyMongoDb):

    def __init__(self):
        self.m_internal_id = ObjectId()
        self.m_created_at = datetime.now()
        
    def to_dict(self):
        pass
    
    @staticmethod
    def from_dict(dictionary):
        pass

