# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_persistent_volume import V1PersistentVolume


class TestV1PersistentVolume(unittest.TestCase):
    """ V1PersistentVolume unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1PersistentVolume(self):
        """
        Test V1PersistentVolume
        """
        model = kubernetes.client.models.v1_persistent_volume.V1PersistentVolume()


if __name__ == '__main__':
    unittest.main()
