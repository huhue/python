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
from kubernetes.client.models.v1alpha1_external_admission_hook import V1alpha1ExternalAdmissionHook


class TestV1alpha1ExternalAdmissionHook(unittest.TestCase):
    """ V1alpha1ExternalAdmissionHook unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1ExternalAdmissionHook(self):
        """
        Test V1alpha1ExternalAdmissionHook
        """
        model = kubernetes.client.models.v1alpha1_external_admission_hook.V1alpha1ExternalAdmissionHook()


if __name__ == '__main__':
    unittest.main()
