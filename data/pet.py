from dataclasses import dataclass


@dataclass
class PetData:
    id: int
    name: str
    category: dict
    photo_urls: list[str]
    tags: list[dict]
    status: str