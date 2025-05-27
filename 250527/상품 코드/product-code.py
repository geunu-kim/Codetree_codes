product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product :
    def __init__ (self,a = "codetree",b = 50):
        self.n = a
        self.c = b

Product1 = Product()
print("product",Product1.c,"is",Product1.n)

Product2 = Product(product_name , product_code)
print("product",Product2.c,"is",Product2.n)