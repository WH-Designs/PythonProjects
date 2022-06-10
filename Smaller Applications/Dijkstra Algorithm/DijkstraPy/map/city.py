from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int

    def __str__(self) -> str:
        return f'{self.name}'

    def __eq__(self, other) -> bool:
        if other is not None and isinstance(other, City):
            return self.name == other.name and self.population == other.population

        return False
