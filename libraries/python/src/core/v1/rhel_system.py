# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = rhel_system_from_dict(json.loads(json_string))

from typing import Any, Optional, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


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


class SystemClass:
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
    def from_dict(obj: Any) -> 'SystemClass':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        host_url = from_union([from_str, from_none], obj.get("host_url"))
        hostname = from_union([from_str, from_none], obj.get("hostname"))
        inventory_id = from_str(obj.get("inventory_id"))
        rhel_version = from_union([from_str, from_none], obj.get("rhel_version"))
        tags = from_union([lambda x: from_list(RHELSystemTag.from_dict, x), from_none], obj.get("tags"))
        return SystemClass(display_name, host_url, hostname, inventory_id, rhel_version, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["host_url"] = from_union([from_str, from_none], self.host_url)
        result["hostname"] = from_union([from_str, from_none], self.hostname)
        result["inventory_id"] = from_str(self.inventory_id)
        result["rhel_version"] = from_union([from_str, from_none], self.rhel_version)
        result["tags"] = from_union([lambda x: from_list(lambda x: to_class(RHELSystemTag, x), x), from_none], self.tags)
        return result


class RHELSystem:
    """Event data for a RHEL system."""
    system: SystemClass

    def __init__(self, system: SystemClass) -> None:
        self.system = system

    @staticmethod
    def from_dict(obj: Any) -> 'RHELSystem':
        assert isinstance(obj, dict)
        system = SystemClass.from_dict(obj.get("system"))
        return RHELSystem(system)

    def to_dict(self) -> dict:
        result: dict = {}
        result["system"] = to_class(SystemClass, self.system)
        return result


def rhel_system_from_dict(s: Any) -> RHELSystem:
    return RHELSystem.from_dict(s)


def rhel_system_to_dict(x: RHELSystem) -> Any:
    return to_class(RHELSystem, x)
