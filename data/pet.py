from dataclasses import dataclass


@dataclass
class PetData:
    id: int
    name: str
    category: dict
    photoUrls: list[str]
    tags: list[dict]
    status: str
