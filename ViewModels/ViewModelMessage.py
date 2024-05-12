class ViewModelMessage(object):
    messages_list = list()
    color = None

    def __init__(self, messages, color = "green"):
        self.messages_list = messages
        self.color = color

