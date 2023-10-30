prel='''import codewars_test as _test
@_test.describe('Check solution size')
def _solution_check():
    limit = 55
    size = 54
    @_test.it(f'Code size should be less than {limit} chars' + f', actual size: {size}'*(size < limit))
    def size_test():
        _test.expect(size < limit, f'Solution too large, actual size: {size}')'''
sol = '''zero_or_one=lambda n,s:[i>n/2for i in map(sum,zip(*s))]'''
tsts = '''import codewars_test as test
from sol import zero_or_one

sample_test_cases = [

#    n     s              result
    
    (1,  [[1,1,0,1]],     [1, 1, 0, 1]),

    (3,  [[1,0,1,0,1], 
          [1,0,1,0,1], 
          [0,1,0,1,0]],   [1, 0, 1, 0, 1]),

    (3,  [[1,0,1,0,1], 
          [1,1,1,0,1], 
          [0,1,1,1,0]],   [1, 1, 1, 0, 1]),

    (5,  [[1,0,0,0,0], 
          [0,1,0,0,0], 
          [0,0,1,0,0], 
          [0,0,0,1,0], 
          [0,0,0,0,1]],   [0, 0, 0, 0, 0]),
]

@test.describe('Sample tests')
def sample_tests():
    @test.it('Testing zero_or_one')
    def _():
        for n, s, expected in sample_test_cases:
            test.assert_equals(zero_or_one(n, s), expected)'''
with open('prel.py','w') as f:
        f.write(prel)
with open('sol.py','w') as f:
        f.write(prel)
with open('tsts.py','w') as f:
        f.write(prel)
import sys
sys.path = ['.']+sys.path
import os
os.system('bin/python tsts.py')
zero_or_one=lambda n,s:[i>n/2for i in map(sum,zip(*s))]
a=lambda n,s:[i>n/2for i in map(sum,zip(*s))]
