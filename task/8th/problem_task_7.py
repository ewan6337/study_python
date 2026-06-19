class Contactinformation:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class Phonebook:
    def __init__(self):
        self.contactinformation_list = {}

    def set_list(self, name, phone, email):
        self.contactinformation_list[name] = Contactinformation(name, phone, email)

    def get_list(self, name):
        if name in self.contactinformation_list:
            return self.contactinformation_list[name]
        else:
            print("해당 이름의 연락처가 존재하지 않습니다")
            return None

    def del_list(self, name):
        if name in self.contactinformation_list:
            del self.contactinformation_list[name]
        else:
            print("해당 이름의 연락처가 존재하지 않습니다")
            return None

