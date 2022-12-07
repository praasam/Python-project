class Customer():
    def __init__(self, cid=0, name='', address='', email='', telephoneno='', payment=''):
        self.cid = cid
        self.name = name
        self.address = address
        self.email = email
        self.telephoneno = telephoneno
        self.payment = payment


#getters
    def getCID(self):
        return self.cid
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getTelephoneNo(self):
        return self.telephoneno
    def getPayment(self):
        return self.payment

 #Setters
    def setCID(self, cid):
        self.cid = cid
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setEmail(self, email):
        self.email = email
    def setTelephoneNo(self, telephoneno):
        self.telephoneno = telephoneno
    def setPayment(self, payment):
        self.payment = payment


    def __str__(self):
        return ("{}, {}, {}".format(self.cid, self.name, self.address, self.email, self.telephoneno, self.payment))
