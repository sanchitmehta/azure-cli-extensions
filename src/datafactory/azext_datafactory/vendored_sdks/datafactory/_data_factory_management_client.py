# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import DataFactoryManagementClientConfiguration
from .operations import OperationOperations
from .operations import FactoryOperations
from .operations import ExposureControlOperations
from .operations import IntegrationRuntimeOperations
from .operations import IntegrationRuntimeObjectMetadataOperations
from .operations import IntegrationRuntimeNodeOperations
from .operations import LinkedServiceOperations
from .operations import DatasetOperations
from .operations import PipelineOperations
from .operations import PipelineRunOperations
from .operations import ActivityRunOperations
from .operations import TriggerOperations
from .operations import TriggerRunOperations
from .operations import DataFlowOperations
from .operations import DataFlowDebugSessionOperations
from . import models


class DataFactoryManagementClient(object):
    """The Azure Data Factory V2 management API provides a RESTful set of web services that interact with Azure Data Factory V2 services.

    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.datafactory.operations.OperationOperations
    :ivar factory: FactoryOperations operations
    :vartype factory: azure.mgmt.datafactory.operations.FactoryOperations
    :ivar exposure_control: ExposureControlOperations operations
    :vartype exposure_control: azure.mgmt.datafactory.operations.ExposureControlOperations
    :ivar integration_runtime: IntegrationRuntimeOperations operations
    :vartype integration_runtime: azure.mgmt.datafactory.operations.IntegrationRuntimeOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations operations
    :vartype integration_runtime_object_metadata: azure.mgmt.datafactory.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_node: IntegrationRuntimeNodeOperations operations
    :vartype integration_runtime_node: azure.mgmt.datafactory.operations.IntegrationRuntimeNodeOperations
    :ivar linked_service: LinkedServiceOperations operations
    :vartype linked_service: azure.mgmt.datafactory.operations.LinkedServiceOperations
    :ivar dataset: DatasetOperations operations
    :vartype dataset: azure.mgmt.datafactory.operations.DatasetOperations
    :ivar pipeline: PipelineOperations operations
    :vartype pipeline: azure.mgmt.datafactory.operations.PipelineOperations
    :ivar pipeline_run: PipelineRunOperations operations
    :vartype pipeline_run: azure.mgmt.datafactory.operations.PipelineRunOperations
    :ivar activity_run: ActivityRunOperations operations
    :vartype activity_run: azure.mgmt.datafactory.operations.ActivityRunOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: azure.mgmt.datafactory.operations.TriggerOperations
    :ivar trigger_run: TriggerRunOperations operations
    :vartype trigger_run: azure.mgmt.datafactory.operations.TriggerRunOperations
    :ivar data_flow: DataFlowOperations operations
    :vartype data_flow: azure.mgmt.datafactory.operations.DataFlowOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session: azure.mgmt.datafactory.operations.DataFlowDebugSessionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataFactoryManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.factory = FactoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.exposure_control = ExposureControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime = IntegrationRuntimeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_node = IntegrationRuntimeNodeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_service = LinkedServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dataset = DatasetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline = PipelineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_run = PipelineRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.activity_run = ActivityRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger_run = TriggerRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow = DataFlowOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataFactoryManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
