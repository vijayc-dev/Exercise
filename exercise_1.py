class Category:
    def __init__(self,name,code,no_of_products=0):
        self.name=name
        self.code=code
        self.no_of_products=no_of_products
    def add(self):
        self.no_of_products+=1
    def display_cat(self):
        print("Name : ",self.name," // Code : ",self.code," // No of Products : ",self.no_of_products)
class Product:
    def __init__(self,name,code,category,price):
        self.pname=name
        self.pcode=code
        self.category=category
        self.price=price
        category.no_of_products+=1
class Sort_search:
    def __init__(self,pro):
        self.pro=pro
    def asc_sort(self):
        for i in range(len(self.pro)):
            for j in range(i+1,len(self.pro)):
                if self.pro[j].price<self.pro[i].price:
                    temp=self.pro[i]
                    self.pro[i]=self.pro[j]
                    self.pro[j]=temp
    def desc_sort(self):
        for i in range(len(self.pro)):
            for j in range(i+1,len(self.pro)):
                if self.pro[j].price>self.pro[i].price:
                    temp=self.pro[i]
                    self.pro[i]=self.pro[j]
                    self.pro[j]=temp
    def search(self,code):
        x=False
        for i in range(len(self.pro)):
            if code==self.pro[i].pcode:
                x=True
                print("Your Search Product is :", self.pro[i].pname," ",self.pro[i].category.name, "  Code:", self.pro[i].pcode, "  Price:", self.pro[i].price)
        if x==False:
            print("Product is not found from this code")
    def display_product(self):
        for i in range(len(self.pro)):
            print("Product:",self.pro[i].pname,"  ",self.pro[i].category.name,"  Code:",self.pro[i].pcode,"  Price:",self.pro[i].price)
a1=Category("TV","111",0)
a2=Category("MOBILE","112",0)
a3=Category("AC","113",0)

p1=Product("Samsung",1101,a1,1500)
p2=Product("OPPO",1102,a2,1000)
p3=Product("LAVA",1103,a1,2500)
p4=Product("voltas",1104,a3,1200)
p5=Product("samsung",1105,a3,7000)
p6=Product("lg",1106,a3,6500)
# Dispalay Category with No_of_Product
a1.display_cat()
a2.display_cat()
a3.display_cat()
pro=[p1,p2,p2,p3,p4,p5,p6]
se=Sort_search(pro)
# Sorting
se.asc_sort()
se.display_product()
# search product using code
se.search(int(input("Search product code: ")))
