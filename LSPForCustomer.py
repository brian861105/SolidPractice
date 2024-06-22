class  Customer:
    def getDiscount(self, TotalSales):
        return TotalSales
    def add(self):
        pass
    

class GoldCustomer(Customer):
    def getDiscount(self, TotalSales):
        return super().getDiscount(TotalSales) - 5
    
    def add(self):
        print("GoldCustomer:Add")
        
class SilverCustomer(Customer):
    def getDiscount(self, TotalSales):
        return super().getDiscount(TotalSales) - 5
    def add(self):
        print("SilverCustomer:Add")
        
class Enquiry(Customer):
    def getDiscount(self, TotalSales):
        return super().getDiscount(TotalSales) - 5
    def add(self):
        print("not allowed")
        
def main():
    Customers = []
    Customers.append(SilverCustomer())
    Customers.append(GoldCustomer())
    Customers.append(Enquiry())
    
    for o in Customers:
        o.add()
        print(o.getDiscount(100))
        
if __name__ == '__main__':
    main()
        