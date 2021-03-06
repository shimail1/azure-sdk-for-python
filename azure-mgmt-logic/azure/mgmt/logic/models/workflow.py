# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Workflow(Resource):
    """Workflow.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: The resource id.
    :type id: str
    :param name: Gets the resource name.
    :type name: str
    :param type: Gets the resource type.
    :type type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict
    :ivar provisioning_state: Gets the provisioning state. Possible values
     include: 'NotSpecified', 'Accepted', 'Running', 'Ready', 'Creating',
     'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded',
     'Moving', 'Updating', 'Registering', 'Registered', 'Unregistering',
     'Unregistered', 'Completed'
    :vartype provisioning_state: str or :class:`WorkflowProvisioningState
     <azure.mgmt.logic.models.WorkflowProvisioningState>`
    :ivar created_time: Gets the created time.
    :vartype created_time: datetime
    :ivar changed_time: Gets the changed time.
    :vartype changed_time: datetime
    :param state: The state. Possible values include: 'NotSpecified',
     'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended'
    :type state: str or :class:`WorkflowState
     <azure.mgmt.logic.models.WorkflowState>`
    :ivar version: Gets the version.
    :vartype version: str
    :ivar access_endpoint: Gets the access endpoint.
    :vartype access_endpoint: str
    :param sku: The sku.
    :type sku: :class:`Sku <azure.mgmt.logic.models.Sku>`
    :param integration_account: The integration account.
    :type integration_account: :class:`ResourceReference
     <azure.mgmt.logic.models.ResourceReference>`
    :param definition: The definition.
    :type definition: object
    :param parameters: The parameters.
    :type parameters: dict
    """ 

    _validation = {
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'changed_time': {'readonly': True},
        'version': {'readonly': True},
        'access_endpoint': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'WorkflowProvisioningState'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'changed_time': {'key': 'properties.changedTime', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'WorkflowState'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'access_endpoint': {'key': 'properties.accessEndpoint', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'integration_account': {'key': 'properties.integrationAccount', 'type': 'ResourceReference'},
        'definition': {'key': 'properties.definition', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': '{WorkflowParameter}'},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None, state=None, sku=None, integration_account=None, definition=None, parameters=None):
        super(Workflow, self).__init__(id=id, name=name, type=type, location=location, tags=tags)
        self.provisioning_state = None
        self.created_time = None
        self.changed_time = None
        self.state = state
        self.version = None
        self.access_endpoint = None
        self.sku = sku
        self.integration_account = integration_account
        self.definition = definition
        self.parameters = parameters
