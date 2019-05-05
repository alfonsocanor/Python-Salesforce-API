from psapiApp import model
from psapiApp.Helpers import AlquemyEncoder
import random

number = random.randrange(0,10000,1)
dni = random.randrange(10000000, 99999999,1)
print('The number is: ' + str(number))
model.CRUMTest().insertTest(number)
#insert.insertTest(number)
model.CRUMAccount().insertAccount(dni,'fooName','fooApellido',str(dni)+'@gmail.com')


class Queries():
    def allAccount(self):
        jsonList = []
        queryResult = model.Account.query.all()
        for obj in queryResult:
            value = AlquemyEncoder.AlchemyEncoder().default(obj)
            jsonList.append(value) 
        return jsonList


        