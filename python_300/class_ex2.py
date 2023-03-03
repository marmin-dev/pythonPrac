class Stock:
    def __init__(self,cor,code):
        self.name = cor
        self.code = code
    def set_name(self,cor):
        self.name = cor
    def set_code(self,code):
        self.code = code

samsung = Stock("삼성전자", "005930")
a = Stock(None,None)
a.set_code('005933')
a.set_name("LG전자")
print(a.name,a.code)


