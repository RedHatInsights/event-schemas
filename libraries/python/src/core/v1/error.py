# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = error_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Severity(Enum):
    """The severity of the error."""
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"


class ErrorClass:
    """An error reported by an application."""
    """Machine-readable error code that identifies the error."""
    code: str
    """Human readable description of the error."""
    message: str
    """The severity of the error."""
    severity: Severity
    """The stack trace/traceback (optional)"""
    stack_trace: Optional[str]

    def __init__(self, code: str, message: str, severity: Severity, stack_trace: Optional[str]) -> None:
        self.code = code
        self.message = message
        self.severity = severity
        self.stack_trace = stack_trace

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorClass':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        message = from_str(obj.get("message"))
        severity = Severity(obj.get("severity"))
        stack_trace = from_union([from_str, from_none], obj.get("stack_trace"))
        return ErrorClass(code, message, severity, stack_trace)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_str(self.code)
        result["message"] = from_str(self.message)
        result["severity"] = to_enum(Severity, self.severity)
        result["stack_trace"] = from_union([from_str, from_none], self.stack_trace)
        return result


class Error:
    """Event data for an application error."""
    error: ErrorClass

    def __init__(self, error: ErrorClass) -> None:
        self.error = error

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        error = ErrorClass.from_dict(obj.get("error"))
        return Error(error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error"] = to_class(ErrorClass, self.error)
        return result


def error_from_dict(s: Any) -> Error:
    return Error.from_dict(s)


def error_to_dict(x: Error) -> Any:
    return to_class(Error, x)
