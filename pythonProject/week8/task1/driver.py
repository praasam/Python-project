class Driver():
    def __init__(self, did=0, name='', address='', email='', licenseno=''):
        self.did = did
        self.name = name
        self.address = address
        self.email = email
        self.licenseno = licenseno
#getters
    def getDID(self):
        return self.did
    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getLicenseNo(self):
        return self.licenseno

    #Setters
    def setDID(self, did):
        self.did = did
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setEmail(self, email):
        self.email = email
    def setLicenseNo(self, licenseno):
        self.licenseno = licenseno
 # _ str _
    def __str__(self):
        return ("{}, {}, {}".format(self.did, self.name, self.address, self.email, self.licenseno))




