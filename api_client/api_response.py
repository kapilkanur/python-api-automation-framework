from dataclasses import dataclass


@dataclass
class APIResponse:
    reason: str
    status_code: int
    text: str
    headers: dict
    as_dict: object