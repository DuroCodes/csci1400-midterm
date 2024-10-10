from engine import Engine
from entity import Entity


class BaseComponent:
    entity: Entity

    @property
    def engine(self) -> Engine:
        return self.entity.parent.engine
