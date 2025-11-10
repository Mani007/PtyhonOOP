class item:
    def __init__(self,name,price,qty=0): #magic method constructor
        print(f"An instance created for {name}") #string formatting
        self.name = name 
        self.price = price
        self.qty = qty
    def calculate(self, x , y):
        print("The total price is " + str(x*y))

item1 = item('abc',10,5) #instance of class item
# item1.name = "abc" # adding attribute to the instance of class
# item1.price = 10
# item1.qty = 5
print("Item1 name is " + item1.name + " item1 price is " + str(item1.price) + " item1 qty is " + str(item1.qty))
item1.calculate(item1.price, item1.qty)
## new instance
item2 = item('xyz',100,25) #instance of class item
# item2.name = "xyz" # adding attribute to the instance of class
# item2.price = 100
# item2.qty = 20
print("Item1 name is " + item2.name + " item1 price is " + str(item2.price) + " item2 qty is " + str(item2.qty))
item2.calculate(item2.price, item2.qty)