from item import Item
from phone import Phone



item1 = Item("myitem",20)

print(item1.name)


item1.name = "Otheritem"
print(item1.name)

item1.apply_increment(0.2)
print(item1.price)