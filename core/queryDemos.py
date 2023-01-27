from .models import *

#***(1)Returns all customers from customer table
customer = Customer.objects.all()

#(2)Returns first customer in table
firstCustomer = Customer.objects.first()

#(3)Returns last customer in table
lastCustomer = Customer.objects.last()

#(4)Returns single customer by name
customerByName = Customer.objects.get(first_name='Martin')

#***(5)Returns single customer by id
customerById = Customer.objects.get(id=4)

#***(6)Returns all orders related to customer (firstcustomer variable set above)
customerById = Order.all()

#***(7)Returns all orders customer name (Query parent model value)
order = Order.objects.first()
parentName = order.customer.first_name

#***(8)Returns products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(categoty="Out Door")

#***(9)Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

#***(10)Returns all products with tag of "Sports": (Query many to many fields)
productsFilterd = Product.objects.filter(tags_name='Sports')

#Returns total count for each product ordered
allOrders = {}

for order in firstCustomer.Order.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

#Related SET example
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()