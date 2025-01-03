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
       + category.no_of_products+=1

a1=Category("TV","111",0)
a2=Category("MOBILE","112",0)
a3=Category("AC","113",0)

p1=Product("Samsung",1101,a1,1500)
p2=Product("OPPO",1102,a2,1000)
p3=Product("LAVA",1103,a1,2500)
p4=Product("voltas",1104,a3,1200)
p5=Product("samsung",1105,a3,7000)
p6=Product("lg",1106,a3,6500)

pro=[p1,p2,p3,p4,p5,p6]
def asc_sort():
    for i in range(len(pro)):
        for j in range(i+1,len(pro)):
            if pro[j].price<pro[i].price:
                temp=pro[i]
                pro[i]=pro[j]
                pro[j]=temp
def desc_sort():
    for i in range(len(pro)):
        for j in range(i+1,len(pro)):
            if pro[j].price>pro[i].price:
                temp=pro[i]
                pro[i]=pro[j]
                pro[j]=temp
def search(code):
    x=False
    for i in range(len(pro)):
        if code==pro[i].pcode:
            x=True
            print("Your Search Product is :", pro[i].pname," ",pro[i].category.name, "  Code:", pro[i].pcode, "  Price:", pro[i].price)
    if x==False:
        print("Product is not found from this code")
a1.display_cat()
a2.display_cat()
a3.display_cat()
asc_sort()
for i in range(len(pro)):
    print("Product:",pro[i].pname,"  ",pro[i].category.name,"  Code:",pro[i].pcode,"  Price:",pro[i].price)
print("after search")
search(int(input("Search element : ")))



# pro=[[p1.pname,p2.pname,p3.pname,p4.pname,p5.pname,p6.pname],[p1.pcode,p2.pcode,p3.pcode,p4.pcode,p5.pcode,p6.pcode],[p1.price,p2.price,p3.price,p4.price,p5.price,p6.price]]
# a1.display_cat()
# a2.display_cat()
# a3.display_cat()
# print(pro[2])
# print(pro)
# def asc_sort():
#     for i in range(0,len(pro[2]),1):
#
#         for j in range(i+1,len(pro[2]),1):
#
#             if pro[2][j]<pro[2][i]:
#
#                 temp=pro[2][i]
#                 pro[2][i]=pro[2][j]
#                 pro[2][j]=temp
#
#                 temp1 = pro[0][i]
#                 pro[0][i]=pro[0][j]
#                 pro[0][j]=temp1
#
#                 temp2=pro[1][i]
#                 pro[1][i] = pro[1][j]
#                 pro[1][j] = temp2
# def desc_sort():
#     for i in range(0, len(pro[2]), 1):
#         for j in range(i + 1, len(pro[2]), 1):
#             if pro[2][j] >pro[2][i]:
#                 temp = pro[2][i]
#                 pro[2][i] = pro[2][j]
#                 pro[2][j] = temp
#
#                 temp1 = pro[0][i]
#                 pro[0][i] = pro[0][j]
#                 pro[0][j] = temp1
#
#                 temp2 = pro[1][i]
#                 pro[1][i] = pro[1][j]
#                 pro[1][j] = temp2
# def search(code):
#     found=0
#     for i in range(0,len(pro[2])):
#         if int(code)==pro[1][i]:
#             found+=1
#             print("your search product:",pro[0][i]," Code:",pro[1][i]," Price:",pro[2][i])
#     if found==0:
#         print("NO Data Found")
# desc_sort()
# for i in range(0,len(pro[2])):
#     print("Product:",pro[0][i],"  Code:",pro[1][i],"  Price:",pro[2][i])
# print(" after sort")
# search(input("Enter Search Code: "))
#
