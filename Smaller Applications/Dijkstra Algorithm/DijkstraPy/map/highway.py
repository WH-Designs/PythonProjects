from dataclasses import dataclass

from DijkstraPy.map.city import City


@dataclass
class Highway:
    name: str
    average_mph: int

    def __str__(self) -> str:
        return f'{self.name}'

    def __eq__(self, other) -> bool:
        if other is not None and isinstance(other, Highway):
            return self.name == other.name and self.average_mph == other.average_mph

        return False

