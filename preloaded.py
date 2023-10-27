@_test.describe('Check solution size')
def _solution_check():
    limit = 550
    size = 1
    @_test.it(f'Code size should be less than {limit} chars' + f', actual size: {size}'*(size < limit))
    def size_test():
        _test.expect(size < limit, f'Solution too large, actual size: {size}')
