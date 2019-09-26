import login
import test_login
import psw

def test_login():

        username=login.username()
        assert True
        
        pd=psw.psw()
        assert pd=='psw'
