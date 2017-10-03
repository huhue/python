# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1RuleWithOperations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_groups=None, api_versions=None, operations=None, resources=None):
        """
        V1alpha1RuleWithOperations - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_groups': 'list[str]',
            'api_versions': 'list[str]',
            'operations': 'list[str]',
            'resources': 'list[str]'
        }

        self.attribute_map = {
            'api_groups': 'apiGroups',
            'api_versions': 'apiVersions',
            'operations': 'operations',
            'resources': 'resources'
        }

        self._api_groups = api_groups
        self._api_versions = api_versions
        self._operations = operations
        self._resources = resources

    @property
    def api_groups(self):
        """
        Gets the api_groups of this V1alpha1RuleWithOperations.
        APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.

        :return: The api_groups of this V1alpha1RuleWithOperations.
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """
        Sets the api_groups of this V1alpha1RuleWithOperations.
        APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.

        :param api_groups: The api_groups of this V1alpha1RuleWithOperations.
        :type: list[str]
        """

        self._api_groups = api_groups

    @property
    def api_versions(self):
        """
        Gets the api_versions of this V1alpha1RuleWithOperations.
        APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.

        :return: The api_versions of this V1alpha1RuleWithOperations.
        :rtype: list[str]
        """
        return self._api_versions

    @api_versions.setter
    def api_versions(self, api_versions):
        """
        Sets the api_versions of this V1alpha1RuleWithOperations.
        APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.

        :param api_versions: The api_versions of this V1alpha1RuleWithOperations.
        :type: list[str]
        """

        self._api_versions = api_versions

    @property
    def operations(self):
        """
        Gets the operations of this V1alpha1RuleWithOperations.
        Operations is the operations the admission hook cares about - CREATE, UPDATE, or * for all operations. If '*' is present, the length of the slice must be one. Required.

        :return: The operations of this V1alpha1RuleWithOperations.
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this V1alpha1RuleWithOperations.
        Operations is the operations the admission hook cares about - CREATE, UPDATE, or * for all operations. If '*' is present, the length of the slice must be one. Required.

        :param operations: The operations of this V1alpha1RuleWithOperations.
        :type: list[str]
        """

        self._operations = operations

    @property
    def resources(self):
        """
        Gets the resources of this V1alpha1RuleWithOperations.
        Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.

        :return: The resources of this V1alpha1RuleWithOperations.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1alpha1RuleWithOperations.
        Resources is a list of resources this rule applies to.  For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required.

        :param resources: The resources of this V1alpha1RuleWithOperations.
        :type: list[str]
        """

        self._resources = resources

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1RuleWithOperations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
