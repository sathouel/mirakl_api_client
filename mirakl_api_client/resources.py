import json
from mirakl_api_client import utils

from mirakl_api_client.utils import urljoin

class ResourcePool:
    def __init__(self, endpoint, session):
        """Initialize the ResourcePool to the given endpoint. Eg: products"""
        self._endpoint = endpoint
        self._session = session

    def get_url(self):
        return self._endpoint

class CreatableResource:
    def create_item(self, item):
        res = self._session.post(self._endpoint, data=json.dumps(item))
        return res

class GettableResource:
    def fetch_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.get(url)
        return res

class ListableResource:
    def fetch_list(self, args=None):
        res = self._session.get(self._endpoint, params=args)
        return res

class SearchableResource:
    def search(self, query):
        params = {
            'query': query
        }
        res = self._session.get(self._endpoint, params=params)
        return res

class UpdatableResource:
    def update_create_item(self, item, code=None):
        if code is None:
            code = item.get('id')
        url = urljoin(self._endpoint, code)
        res = self._session.put(url, data=json.dumps(item))
        return res

class DeletableResource:
    def delete_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.delete(url)
        return res

# Pools

# Invoices
class InvoicesPool(
    ResourcePool,
    GettableResource,
    ListableResource):
    pass

# sellerpayment Transactions
class TransactionsLogsPool(
    ResourcePool,
    ListableResource):
    pass

# Threads

class ThreadsPool(
    ResourcePool,
    GettableResource,
    ListableResource):
    
    def message(self, thread_id):
        return ThreadsMessagePool(
            urljoin(self._endpoint, thread_id, 'message'), self._session
        )

    def attachment(self, attachment_id):
        return ThreadsAttachmentPool(
            urljoin(self._endpoint, attachment_id, 'download'), self._session
        )

class ThreadsMessagePool(
    ResourcePool,
    CreatableResource):
    pass

class ThreadsAttachmentPool(
    ResourcePool,
    GettableResource):
    pass

# Shipments

class ShipmentsPool(
    ResourcePool,
    GettableResource,
    ListableResource):
    
    @property
    def tracking(self):
        return ShipmentsPool(
            urljoin(self._endpoint, 'tracking'), self._session
        )

    @property
    def ship(self):
        return ShipmentsShipPool(
            urljoin(self._endpoint, 'ship'), self._session
        )

class ShipmentsTrackingPool(
    ResourcePool,
    CreatableResource):
    pass

class ShipmentsShipPool(
    ResourcePool,
    UpdatableResource):
    pass

# Offers

class OffersPool(
    ResourcePool,
    CreatableResource,
    GettableResource,
    ListableResource
    ):

    @property
    def imports(self):
        return OffersImportsPool(
            urljoin(self._endpoint, 'imports'), self._session
        )

    @property
    def export(self):
        return OffersExportPool(
            urljoin(self._endpoint, 'export'), self._session
        )

class OffersImportsPool(
    ResourcePool,
    CreatableResource,
    GettableResource,
    ListableResource):
    
    def error_report(self, import_id):
        return OffersImportsErrorReportPool(
            urljoin(self._endpoint, import_id, 'error_report'), self._session
        )

class OffersImportsErrorReportPool(
    ResourcePool,
    ListableResource):
    pass

class OffersExportPool(
    ResourcePool, 
    ListableResource):
    pass
# Orders

class OrdersPool(
    ResourcePool,
    ListableResource,
    UpdatableResource):
    pass

    @property
    def shipping_from(self):
        return OrdersShippingFromPool(
            urljoin(self._endpoint, 'shipping_from'), self._session
        )

    @property
    def refund(self):
        return OrdersRefundPool(
            urljoin(self._endpoint, 'refund'), self._session
        )        

    @property
    def cancel_lines(self):
        return OrdersCancelPool(
            urljoin(self._endpoint, 'cancel'), self._session
        )
    
    @property
    def adjust(self):
        return OrdersAdjustPool(
            urljoin(self._endpoint, 'adjust'), self._session
        )
    
    def accept(self, order_id):
        return OrdersAcceptPool(
            urljoin(self._endpoint, order_id, 'accept'), self._session
        )

    def tracking(self, order_id):
        return OrdersTrackingPool(
            urljoin(self._endpoint, order_id, 'tracking'), self._session
        )   

    def ship(self, order_id):
        return OrdersShipPool(
            urljoin(self._endpoint, order_id, 'ship'), self._session
        )

    def cancel(self, order_id):
        return OrdersCancelPool(
            urljoin(self._endpoint, order_id, 'cancel'), self._session
        )

    def additional_fields(self, order_id):
        return OrdersAdditionalFieldsPool(
            urljoin(self._endpoint, order_id, 'additional_fields'), self._session
        )

    def evaluation(self, order_id):
        return OrdersEvaluationPool(
            urljoin(self._endpoint, order_id, 'evaluation'), self._session
        )


class OrdersShippingFromPool(
    ResourcePool,
    UpdatableResource
    ):
    pass

class OrdersAcceptPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersTrackingPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersShipPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersRefundPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersCancelPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersAdditionalFieldsPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersAdjustPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersEvaluationPool(
    ResourcePool,
    ListableResource):
    pass

class OrdersLinesPool:
    pass

# IMPLEMENT ORDER THREAD CREATION /api/orders/{order_id}/threads

# Products 

# IMPLEMENT /api/products/offers