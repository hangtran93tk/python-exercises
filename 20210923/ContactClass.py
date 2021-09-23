class Contact:
    def __init__(self,  name = "", phones =[], emails =[], address="", note="", tags=[]):
        self.__name = name
        self.phones = phones
        self.emails = emails
        self.address = address
        self.note = note
        self.tags = tags
    #setter
    def set_field(self,key, value):
        # self.__dict__[key] = value
        self.__setattr__(key,value)
    # def set_name(self, name):
    #     self.name = name
    #
    # def set_phone(self,phones):
    #     self.phones = phones
    #
    # def set_emails(self,emails):
    #     self.emails = emails
    #
    # def set_address(self, address):
    #     self.address = address
    #
    # def set_tags(self,tags):
    #     self.tags = tags

    def get_info(self):
        return f"""
        {"Name   : ":10}{self.name}
        {"Phone  : ":10}{self.phones}
        {"Email  : ":10}{self.emails}
        {"Address:":10}{self.address}
        {"Note   : ":10}{self.note}
        {"Tags   :":10}{self.tags}
        """
    def check_tag(self,tag):
        return tag in self.tags

    def edit_field(self, field, new_value):
        if (field in Contact):
            self.field = new_value

