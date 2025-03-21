# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from __future__ import annotations

from typing import Literal, Mapping, Optional, Sequence, Union

from pydantic import BaseModel, Extra, Field, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class Counter(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    aggregate: Optional[Union[bool, Literal['only']]]
    average: Optional[bool]
    metric_name: Optional[str]
    name: Optional[str]
    type: Optional[str]


class InstanceCounts(BaseModel):
    class Config:
        allow_mutation = False

    monitored: Optional[str]
    total: Optional[str]
    unique: Optional[str]


class ExtraMetrics(BaseModel):
    class Config:
        allow_mutation = False

    counters: Sequence[Mapping[str, Union[str, Counter]]]
    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]
    instance_counts: Optional[InstanceCounts]
    name: str
    tag_name: Optional[str]
    use_localized_counters: Optional[bool]


class Counter1(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    aggregate: Optional[Union[bool, Literal['only']]]
    average: Optional[bool]
    metric_name: Optional[str]
    name: Optional[str]
    type: Optional[str]


class InstanceCounts1(BaseModel):
    class Config:
        allow_mutation = False

    monitored: Optional[str]
    total: Optional[str]
    unique: Optional[str]


class Metrics(BaseModel):
    class Config:
        allow_mutation = False

    counters: Sequence[Mapping[str, Union[str, Counter1]]]
    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]
    instance_counts: Optional[InstanceCounts1]
    name: str
    tag_name: Optional[str]
    use_localized_counters: Optional[bool]


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    disable_generic_tags: Optional[bool]
    empty_default_hostname: Optional[bool]
    enable_health_service_check: Optional[bool]
    extra_metrics: Optional[Mapping[str, ExtraMetrics]]
    metrics: Optional[Mapping[str, Metrics]]
    min_collection_interval: Optional[float]
    namespace: Optional[str] = Field(None, regex='\\w*')
    password: Optional[str]
    server: Optional[str]
    server_tag: Optional[str]
    service: Optional[str]
    tags: Optional[Sequence[str]]
    username: Optional[str]

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))
