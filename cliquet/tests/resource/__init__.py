import mock

from cliquet.authorization import RouteFactory
from cliquet.storage import memory
from cliquet.tests.support import unittest, DummyRequest
from cliquet.resource import BaseResource


class BaseTest(unittest.TestCase):
    resource_class = BaseResource

    def setUp(self):
        self.storage = memory.Memory()
        request = self.get_request()
        self.resource = self.resource_class(request=request,
                                            context=RouteFactory(request))
        self.collection = self.resource.collection
        self.patch_known_field = mock.patch.object(self.resource,
                                                   'is_known_field')

    def tearDown(self):
        mock.patch.stopall()

    def get_request(self):
        request = DummyRequest(method='GET')
        request.registry.storage = self.storage
        return request

    @property
    def last_response(self):
        return self.resource.request.response
