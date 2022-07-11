# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = advisor_recommendations_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, Optional, List, TypeVar, Callable, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AdvisorRecommendation:
    publish_date: datetime
    reboot_required: bool
    rule_description: str
    rule_id: str
    rule_url: str
    total_risk: str

    def __init__(self, publish_date: datetime, reboot_required: bool, rule_description: str, rule_id: str, rule_url: str, total_risk: str) -> None:
        self.publish_date = publish_date
        self.reboot_required = reboot_required
        self.rule_description = rule_description
        self.rule_id = rule_id
        self.rule_url = rule_url
        self.total_risk = total_risk

    @staticmethod
    def from_dict(obj: Any) -> 'AdvisorRecommendation':
        assert isinstance(obj, dict)
        publish_date = from_datetime(obj.get("publish_date"))
        reboot_required = from_bool(obj.get("reboot_required"))
        rule_description = from_str(obj.get("rule_description"))
        rule_id = from_str(obj.get("rule_id"))
        rule_url = from_str(obj.get("rule_url"))
        total_risk = from_str(obj.get("total_risk"))
        return AdvisorRecommendation(publish_date, reboot_required, rule_description, rule_id, rule_url, total_risk)

    def to_dict(self) -> dict:
        result: dict = {}
        result["publish_date"] = self.publish_date.isoformat()
        result["reboot_required"] = from_bool(self.reboot_required)
        result["rule_description"] = from_str(self.rule_description)
        result["rule_id"] = from_str(self.rule_id)
        result["rule_url"] = from_str(self.rule_url)
        result["total_risk"] = from_str(self.total_risk)
        return result


class RHELSystemTag:
    key: str
    namespace: str
    value: str

    def __init__(self, key: str, namespace: str, value: str) -> None:
        self.key = key
        self.namespace = namespace
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'RHELSystemTag':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        namespace = from_str(obj.get("namespace"))
        value = from_str(obj.get("value"))
        return RHELSystemTag(key, namespace, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["namespace"] = from_str(self.namespace)
        result["value"] = from_str(self.value)
        return result


class RHELSystem:
    """A RHEL system managed by console.redhat.com"""
    display_name: Optional[str]
    host_url: Optional[str]
    hostname: Optional[str]
    inventory_id: str
    rhel_version: Optional[str]
    tags: Optional[List[RHELSystemTag]]

    def __init__(self, display_name: Optional[str], host_url: Optional[str], hostname: Optional[str], inventory_id: str, rhel_version: Optional[str], tags: Optional[List[RHELSystemTag]]) -> None:
        self.display_name = display_name
        self.host_url = host_url
        self.hostname = hostname
        self.inventory_id = inventory_id
        self.rhel_version = rhel_version
        self.tags = tags

    @staticmethod
    def from_dict(obj: Any) -> 'RHELSystem':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        host_url = from_union([from_str, from_none], obj.get("host_url"))
        hostname = from_union([from_str, from_none], obj.get("hostname"))
        inventory_id = from_str(obj.get("inventory_id"))
        rhel_version = from_union([from_str, from_none], obj.get("rhel_version"))
        tags = from_union([lambda x: from_list(RHELSystemTag.from_dict, x), from_none], obj.get("tags"))
        return RHELSystem(display_name, host_url, hostname, inventory_id, rhel_version, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["host_url"] = from_union([from_str, from_none], self.host_url)
        result["hostname"] = from_union([from_str, from_none], self.hostname)
        result["inventory_id"] = from_str(self.inventory_id)
        result["rhel_version"] = from_union([from_str, from_none], self.rhel_version)
        result["tags"] = from_union([lambda x: from_list(lambda x: to_class(RHELSystemTag, x), x), from_none], self.tags)
        return result


class AdvisorRecommendations:
    """Event data for Advisor Recommendations."""
    """Advisor recommendations for a system"""
    advisor_recommendations: List[AdvisorRecommendation]
    system: RHELSystem

    def __init__(self, advisor_recommendations: List[AdvisorRecommendation], system: RHELSystem) -> None:
        self.advisor_recommendations = advisor_recommendations
        self.system = system

    @staticmethod
    def from_dict(obj: Any) -> 'AdvisorRecommendations':
        assert isinstance(obj, dict)
        advisor_recommendations = from_list(AdvisorRecommendation.from_dict, obj.get("advisor_recommendations"))
        system = RHELSystem.from_dict(obj.get("system"))
        return AdvisorRecommendations(advisor_recommendations, system)

    def to_dict(self) -> dict:
        result: dict = {}
        result["advisor_recommendations"] = from_list(lambda x: to_class(AdvisorRecommendation, x), self.advisor_recommendations)
        result["system"] = to_class(RHELSystem, self.system)
        return result


def advisor_recommendations_from_dict(s: Any) -> AdvisorRecommendations:
    return AdvisorRecommendations.from_dict(s)


def advisor_recommendations_to_dict(x: AdvisorRecommendations) -> Any:
    return to_class(AdvisorRecommendations, x)
