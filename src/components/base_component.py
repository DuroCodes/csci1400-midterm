from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.engine import Engine
    from src.entity import Entity
    from src.game_map import GameMap


class BaseComponent:
    parent: Entity

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.parent.parent.engine
