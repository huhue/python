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
from kubernetes.client.models.v1alpha1_initializer import V1alpha1Initializer


class TestV1alpha1Initializer(unittest.TestCase):
    """ V1alpha1Initializer unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1Initializer(self):
        """
        Test V1alpha1Initializer
        """
        model = kubernetes.client.models.v1alpha1_initializer.V1alpha1Initializer()


if __name__ == '__main__':
    unittest.main()
