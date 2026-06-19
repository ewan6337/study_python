class Person:
    def __init__(self, name, mphone, ophone, email) -> None:
        self.name = name
        self.mphone = mphone
        self.ophone = ophone
        self.email = email

    def __str__(self) -> str:
        return f"name = {self.name}, mphone = {self.mphone}, ophone = {self.ophone}, email = {self.email}"

    def set_name(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_mphone(self, mphone) -> None:
        self.mphone = mphone

    def get_mphone(self) -> str:
        return self.mphone

    def set_ophone(self, ophone) -> None:
        self.ophone = ophone

    def get_ophone(self) -> str:
        return self.ophone

    def set_email(self, email) -> None:
        self.email = email

    def get_email(self) -> str:
        return self.email
