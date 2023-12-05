from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, member_id, updated_member):
        for i, member in enumerate(self._members):
            if member['id'] == member_id:
            
                self._members[i] = updated_member
            return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members

