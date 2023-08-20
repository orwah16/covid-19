#!/usr/bin/env python
import unittest
import app

class Test(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test(self):
        rv = self.app.get('/status')
        # rv.data = rv.data.decode("utf-8").encode('ascii', 'ignore')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, bytes("{status: success}",'utf-8'))

        # rv = self.app.get('/newCasesPeak?country=israel')
        # # rv.data = rv.data.decode("utf-8").encode('ascii', 'ignore')
        # self.assertEqual(rv.status, '200 OK')
        # self.assertEqual(rv.data, bytes('{“country”:”israel”,“method”:“newCasesPeak”,”date”:“9/12/20”,“value”:4158}','utf-8'))  
        
        rv = self.app.get('/dskjhlkdjfg')
        self.assertEqual(rv.data, bytes('{ }','utf-8'))   




if __name__ == '__main__':
    unittest.main()