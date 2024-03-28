from DataModels.Base import Base


class Owned (Base):
    def __init__(self, owner_id):
        super().__init__()
        self.m_owner_id = owner_id
