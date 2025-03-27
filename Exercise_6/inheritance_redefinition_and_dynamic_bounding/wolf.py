from mammal import Mammal

class Wolf(Mammal):
    def __init__(self, pack_name, name):
        assert isinstance(pack_name, str) and len(pack_name) > 0, "Pack name must be a non-empty string"
        assert isinstance(name, str) and len(name) > 0, "Name must be a non-empty string"
        
        super().__init__(name)  # Corrected constructor call with the name and default legs (4)
        self.__pack_name = pack_name

    def get_pack_name(self):
        return self.__pack_name

    def set_pack_name(self, pack_name):
        assert isinstance(pack_name, str) and len(pack_name) > 0, "Pack name must be a non-empty string"
        self.__pack_name = pack_name

    def another_make_sound(self):
        print("*wolf howling*")
