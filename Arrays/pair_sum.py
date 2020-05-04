import program 
import unittest

def pair_sum(array, target):

    l = []
    
    for n in array:
        
        # target = m + n
        m = target - n

        if m in array:
            l.append((m, n))

    return(l)        

class TestProgram(unittest.TestCase):

    def test_case_1(self):
        output = program.pair_sum([4, 6], 10)
        self.assertEqual(output, [(4, 6)])

    def test_case_2(self):
        output = program.pair_sum([4, 6, 2, 8], 10)
        self.assertEqual(output, [(4, 6), (2, 8)])


# Executing the `main` function 
if __name__ == "__main__":
    unittest.main()    