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


class V1beta1ResourceAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, group=None, name=None, namespace=None, resource=None, subresource=None, verb=None, version=None):
        """
        V1beta1ResourceAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group': 'str',
            'name': 'str',
            'namespace': 'str',
            'resource': 'str',
            'subresource': 'str',
            'verb': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'group': 'group',
            'name': 'name',
            'namespace': 'namespace',
            'resource': 'resource',
            'subresource': 'subresource',
            'verb': 'verb',
            'version': 'version'
        }

        self._group = group
        self._name = name
        self._namespace = namespace
        self._resource = resource
        self._subresource = subresource
        self._verb = verb
        self._version = version

    @property
    def group(self):
        """
        Gets the group of this V1beta1ResourceAttributes.
        Group is the API Group of the Resource.  \"*\" means all.

        :return: The group of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1beta1ResourceAttributes.
        Group is the API Group of the Resource.  \"*\" means all.

        :param group: The group of this V1beta1ResourceAttributes.
        :type: str
        """

        self._group = group

    @property
    def name(self):
        """
        Gets the name of this V1beta1ResourceAttributes.
        Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.

        :return: The name of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1ResourceAttributes.
        Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.

        :param name: The name of this V1beta1ResourceAttributes.
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this V1beta1ResourceAttributes.
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview

        :return: The namespace of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1beta1ResourceAttributes.
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview

        :param namespace: The namespace of this V1beta1ResourceAttributes.
        :type: str
        """

        self._namespace = namespace

    @property
    def resource(self):
        """
        Gets the resource of this V1beta1ResourceAttributes.
        Resource is one of the existing resource types.  \"*\" means all.

        :return: The resource of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this V1beta1ResourceAttributes.
        Resource is one of the existing resource types.  \"*\" means all.

        :param resource: The resource of this V1beta1ResourceAttributes.
        :type: str
        """

        self._resource = resource

    @property
    def subresource(self):
        """
        Gets the subresource of this V1beta1ResourceAttributes.
        Subresource is one of the existing resource types.  \"\" means none.

        :return: The subresource of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._subresource

    @subresource.setter
    def subresource(self, subresource):
        """
        Sets the subresource of this V1beta1ResourceAttributes.
        Subresource is one of the existing resource types.  \"\" means none.

        :param subresource: The subresource of this V1beta1ResourceAttributes.
        :type: str
        """

        self._subresource = subresource

    @property
    def verb(self):
        """
        Gets the verb of this V1beta1ResourceAttributes.
        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.

        :return: The verb of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """
        Sets the verb of this V1beta1ResourceAttributes.
        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.

        :param verb: The verb of this V1beta1ResourceAttributes.
        :type: str
        """

        self._verb = verb

    @property
    def version(self):
        """
        Gets the version of this V1beta1ResourceAttributes.
        Version is the API Version of the Resource.  \"*\" means all.

        :return: The version of this V1beta1ResourceAttributes.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this V1beta1ResourceAttributes.
        Version is the API Version of the Resource.  \"*\" means all.

        :param version: The version of this V1beta1ResourceAttributes.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, V1beta1ResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
