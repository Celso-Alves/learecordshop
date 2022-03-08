import os
from my_app import app, db
import unittest


class learecordshopTestCase(unittest.TestCase):
    def setUp(self):
   
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mateme@localhost/learecordshop'
        self.app = app.test_client()
        db.create_all()
    
    
    
    def test_discos(self):
        "Teste Get Discos"
        rv = self.app.get('/api/discos')
        self.assertEqual(rv.status_code, 200)
        
        #self.assertTrue('No Previous Page' in rv.data.decode("utf-8"))
        #self.assertTrue('No Next Page' in rv.data.decode("utf-8"))
        #outra forma acima é 
        #self.assertTrue(b'Message' in rv.data)
    #verificar se o contudo é json
    def test_discos_conteudo(self):
        "Teste Conteudo Json discos"
        rv = self.app.get('/api/discos')
        self.assertEqual(rv.content_type, "application/json")
    

if __name__ == '__main__':
    unittest.main()
    