from abc import ABC, abstractmethod
class IDataProvider(ABC):
    @abstractmethod
    def OpenConnection(self):
        pass
    @abstractmethod
    def CloseConnection(self):
        pass
    @abstractmethod
    def ExcuteCommand(self):
        pass
    @abstractmethod
    def BeginTransaction(self):
        pass
    
class SqlDataProvider(IDataProvider):
    def OpenConnection(self):
        print("Open sql Connection")
    def CloseConnection(self):
        print("Close sql Connection")
    def ExcuteCommand(self):
        print("Execute sql Command")
    def BeginTransaction(self):
        print("Begin Transaction")
    
class IDataProviderWithoutBeginTransaction(ABC):
    @abstractmethod
    def OpenConnection(self):
        pass
    
    @abstractmethod
    def CloseConnection(self):
        pass
    
    @abstractmethod
    def ExecuteCommand(self):
        pass
    
class IBeginTransaction(ABC):
    @abstractmethod
    def BeginTransaction(self):
        pass



class SqlDataProviderCombine(IDataProviderWithoutBeginTransaction, IBeginTransaction):
    def OpenConnection(self):
        print("Open SQL Connection")
    
    def CloseConnection(self):
        print("Close SQL Connection")
    
    def ExecuteCommand(self):
        print("Execute SQL Command")
    
    def BeginTransaction(self):
        print("Begin Transaction")
def main():
    
    ### 由於 sqldataProvider 並沒有每個 function 都使用到 IDataProvider 中的每一項
    ### 因此我們需要將介面分割成多個小介面，在用一個大介面來進行 merge
    sqldataProvider = SqlDataProvider()
    sqldataProvider.OpenConnection()
    sqldataProvider.ExcuteCommand()
    sqldataProvider.CloseConnection()
    
    sqldataProvider2 = SqlDataProviderCombine()
    sqldataProvider2.OpenConnection()
    sqldataProvider2.ExecuteCommand()
    sqldataProvider2.BeginTransaction()
    sqldataProvider2.CloseConnection()
    

if __name__ == "__main__":
    main()