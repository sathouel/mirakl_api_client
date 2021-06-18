import requests as rq

from mirakl_api_client import (
    resources,
    utils
)

class MirakleClient:
    def __init__(self, hostname, api_key):
        self._session = rq.Session()
        self._hostname = hostname
        self._api_key = api_key   

        self._base_url = utils.urljoin('https://', self._hostname, 'api')
        self._resources = {
            'invoices': resources.InvoicesPool(
                utils.urljoin(self._base_url, 'invoices'), self._session),
            'transactions_logs': resources.TransactionsLogsPool(
                utils.urljoin(self._base_url, 'sellerpayment/transactions_logs'), self._session),
        }        

        self._authenticate()

    def _authenticate(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self._api_key
        }
        self._session.headers = headers

    @property
    def resources(self):
        """Return all resources as a list of Resources"""
        return self._resources

    @property
    def invoices(self):
        return self.resources.get('invoices')