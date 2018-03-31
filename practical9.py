class Vol():
    """Find volume of cube and cylinder using method overloading."""
    def __init__(self):
        print("")
    def volume(self,data1 = None, data2 = None):
        if data1 and not data2:
            print("Volume of cube is ", data1**3)
        elif data1 and data2:
            print("volume of cylinder is ", 3.14*data1*data1*data2)
object = Vol()
object.volume(12)
object.volume(10,11)
