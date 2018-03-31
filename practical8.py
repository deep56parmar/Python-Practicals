class ClassName():
    """Constructor overloading demo"""
    def __init__(self, data1 = None ,data2 = None):
        if data1 and  not data2:
            print("area of cicrcle is " , 3.14*data1*data1)
        elif data1 and data2 and data1 == data2:
            print("area of square is " , data1 * data2)
        elif data1 and data2 and data1 != data2:
            print("area of rectangle is ", data1*data2)

object1 = ClassName(3)
object1 = ClassName(3,3)
object1 = ClassName(3,4)
