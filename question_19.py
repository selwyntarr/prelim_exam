import unittest

class Pedro(unittest.TestCase):
    
    def testPedro(self):
        name_fail = 'Selwyn'
        name = 'Pedro'
        self.assertEqual(name, 'Pedro')

if __name__ == '__main__':
    Pedro().testPedro()