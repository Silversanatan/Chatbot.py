class Room:
    def __init__(self,name,length,breadth):
        self._name = name
        self._length = length
        self._breadth = breadth
    def get_name(self):
        return self._name
    def get_length(self):
        return self._length
    def get_breadth(self):
        return self._breadth
    def compute_area(self):
        return self._length * self._breadth
def main():
    liv = Room("myLivingRoom", 14, 20)
    bd1 = Room("firstBR", 10, 12)
    bd2 = Room("secondBR", 10, 9)
    print("Room Name: "+str(liv.get_name()))
    print("Room Area: "+str(liv.compute_area()))
    combined_area = bd1.compute_area() + bd2.compute_area()
    print("The two bedrooms have a combined area of: "+ str(combined_area))
main()