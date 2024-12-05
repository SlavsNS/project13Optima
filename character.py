class Character:
    def __init__(self, name, age, description, image_url=None):
        self.name = name
        self.age = age
        self.description = description
        self.image_url = image_url

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Description: {self.description}, Image URL: {self.image_url or 'None'}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "description": self.description,
            "image_url": self.image_url
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["description"], data.get("image_url"))
