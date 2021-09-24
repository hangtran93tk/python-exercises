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

    def __str__(self):
        return f'{self.__name}\n{self.phones}\n{self.emails}\n{self.address}\n{self.note}\n{self.tags}'

    def set_phone(self,phones):
        #Check phone value
        self.phones = phones

    def set_emails(self,emails):
        #Check email value
        self.emails = emails

    def check_tag(self,tag):
        return tag in self.tags

    def edit_field(self, field, new_value):
        if (field in Contact):
            self.field = new_value

    def is_friend(self):
        return "ban be" in self.tags

    def say_hello(self):
        print("Hello, I'm " + self.__name)