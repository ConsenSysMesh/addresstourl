import unittest

from ethjsonrpc import EthJsonRpc


class AddressToUrlTestCase(unittest.TestCase):

    def setUp(self):
        with open('compiled.evm') as f:
            compiled = f.read().rstrip()
        self.c = EthJsonRpc()
        self.c._call('evm_reset')
        self.cb = self.c.eth_coinbase()
        self.contract_addr = self.AddressToUrl(self.cb, compiled)

    def tearDown(self):
        pass

    def test_set(self):
        url = 'http://www.yahoo.com'
        self.set_url(self.cb, self.contract_addr, url)

        result = self.get_url(self.contract_addr, self.cb[2:])
        self.assertEqual(url, result)

    def test_set_clear(self):
        url = 'http://www.yahoo.com'
        self.set_url(self.cb, self.contract_addr, url)

        result = self.get_url(self.contract_addr, self.cb[2:])
        self.assertEqual(url, result)

        self.set_url(self.cb, self.contract_addr, '')

        result = self.get_url(self.contract_addr, self.cb[2:])
        self.assertEqual('', result)

    def test_get(self):
        result = self.get_url(self.contract_addr, self.cb[2:])
        self.assertEqual('', result)

################################################################################

    def AddressToUrl(self, sender, compiled):
        '''
        constructor
        '''
        sig = 'AddressToUrl()'
        args = []
        tx = self.c.create_contract(sender, compiled, 300000, sig, args)
        return self.c.get_contract_address(tx)

    def set_url(self, sender, contract_addr, ip):
        sig = 'set_url(string)'
        args = [ip]
        self.c.call_with_transaction(sender, contract_addr, sig, args)

    def get_url(self, contract_addr, addr):
        sig = 'get_url(address)'
        args = [addr]
        result_types = ['string']
        return self.c.call(contract_addr, sig, args, result_types)[0]


if __name__ == '__main__':
    unittest.main()
