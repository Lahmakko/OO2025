# Tool class (Base class)
class Tool:
    def __init__(self, manufacturer, model, rpm):
        assert isinstance(manufacturer, str) and len(manufacturer) > 0, "Manufacturer must be a non-empty string"
        assert isinstance(model, str) and len(model) > 0, "Model must be a non-empty string"
        assert isinstance(rpm, int) and rpm > 0, "RPM must be a positive integer"
        
        self.__manufacturer = manufacturer
        self.__model = model
        self.__rpm = rpm
    
    # Getter methods for encapsulation
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_model(self):
        return self.__model
    
    def get_rpm(self):
        return self.__rpm
    
    # Setter methods for encapsulation
    def set_manufacturer(self, manufacturer):
        assert isinstance(manufacturer, str) and len(manufacturer) > 0, "Manufacturer must be a non-empty string"
        self.__manufacturer = manufacturer
    
    def set_model(self, model):
        assert isinstance(model, str) and len(model) > 0, "Model must be a non-empty string"
        self.__model = model
    
    def set_rpm(self, rpm):
        assert isinstance(rpm, int) and rpm > 0, "RPM must be a positive integer"
        self.__rpm = rpm


# Drill class (Subclass of Tool)
class Drill(Tool):
    def __init__(self, manufacturer, model, rpm, max_diameter):
        super().__init__(manufacturer, model, rpm)
        assert isinstance(max_diameter, float) and max_diameter > 0, "Max diameter must be a positive float"
        
        self.__max_diameter = max_diameter
        self.__attached_bit = None  # No bit attached initially
    
    def get_max_diameter(self):
        return self.__max_diameter
    
    def get_attached_bit(self):
        return self.__attached_bit
    
    def attach_bit(self, bit):
        if self.__attached_bit is not None:
            print(f"Cannot attach {bit.get_diameter()} mm bit. A bit is already attached.")
            return
        if bit.get_diameter() > self.__max_diameter:
            print(f"Cannot attach {bit.get_diameter()} mm bit. It exceeds the max diameter of {self.__max_diameter} mm.")
            return
        if bit.get_rpm() > self.get_rpm():
            print(f"Cannot attach {bit.get_diameter()} mm bit. RPM exceeds the limit of the drill.")
            return
        self.__attached_bit = bit
        print(f"Attached {bit.get_diameter()} mm bit to the drill.")
        
    def detach_bit(self):
        if self.__attached_bit is None:
            print("No bit attached.")
            return
        self.__attached_bit = None
        print("Detached the bit.")


# CordlessDrill class (Subclass of Drill)
class CordlessDrill(Drill):
    def __init__(self, manufacturer, model, rpm, max_diameter):
        super().__init__(manufacturer, model, rpm, max_diameter)
    
    def attach_bit(self, bit):
        # Cordless drills only accept bits with a diameter <= 10 mm
        if bit.get_diameter() > 10:
            print(f"Cannot attach {bit.get_diameter()} mm bit. Only bits with diameter <= 10 mm can be used with a cordless drill.")
            return
        super().attach_bit(bit)


# DrillBit class
class DrillBit:
    def __init__(self, diameter, rpm_limit):
        assert isinstance(diameter, float) and diameter > 0, "Diameter must be a positive float"
        assert isinstance(rpm_limit, int) and rpm_limit > 0, "RPM limit must be a positive integer"
        
        self.__diameter = diameter
        self.__rpm_limit = rpm_limit
    
    def get_diameter(self):
        return self.__diameter
    
    def get_rpm(self):
        return self.__rpm_limit


# Example Usage
if __name__ == "__main__":
    # Create a DrillBit
    bit1 = DrillBit(8.0, 1500)  # 8 mm diameter, 1500 RPM limit
    bit2 = DrillBit(12.0, 2000)  # 12 mm diameter, 2000 RPM limit
    
    # Create a Cordless Drill (max diameter 10 mm)
    cordless_drill = CordlessDrill("Bosch", "Cordless Pro", 1500, 10.0)
    cordless_drill.attach_bit(bit1)  # Should succeed
    cordless_drill.attach_bit(bit2)  # Should fail due to diameter being > 10 mm
    
    # Create a regular Drill (max diameter 15 mm)
    regular_drill = Drill("Makita", "Drill Master", 1800, 15.0)
    regular_drill.attach_bit(bit2)  # Should succeed as 12 mm bit is within the max diameter

    # Detach the bit from the regular drill
    regular_drill.detach_bit()  # Should succeed
