from __future__ import annotations
from copy import deepcopy
from typing import TYPE_CHECKING, Optional, Type, Union
from level import Level
from render_order import RenderOrder
import math

if TYPE_CHECKING:
    from components.ai import BaseAI
    from components.consumable import Consumable
    from components.equippable import Equippable
    from components.equipment import Equipment
    from components.fighter import Fighter
    from components.inventory import Inventory
    from game_map import GameMap


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    parent: Union[GameMap, Inventory]

    def __init__(
        self,
        parent: Optional[GameMap] = None,
        x=0,
        y=0,
        char="?",
        color: tuple[int, int, int] = (255, 255, 255),
        name="<Unnamed>",
        blocks_movement=False,
        render_order=RenderOrder.CORPSE,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        self.render_order = render_order

        if parent:
            self.parent = parent
            parent.entities.add(self)

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def spawn[T](self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = deepcopy(self)
        clone.x = x
        clone.y = y
        clone.parent = gamemap
        gamemap.entities.add(clone)

        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location. Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "parent"):
                if self.parent is self.gamemap:
                    self.gamemap.entities.remove(self)
            self.parent = gamemap
            gamemap.entities.add(self)

    def distance(self, x: int, y: int) -> float:
        """
        Return the distance between the current entity and the given (x, y) coordinate.
        """
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)


class Item(Entity):
    def __init__(
        self,
        *,
        x=0,
        y=0,
        char="?",
        color: tuple[int, int, int] = (255, 255, 255),
        name="<Unnamed>",
        consumable: Optional[Consumable] = None,
        equippable: Optional[Equippable] = None,
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=False,
            render_order=RenderOrder.ITEM,
        )

        self.consumable = consumable
        self.equippable = equippable

        if self.consumable:
            self.consumable.parent = self

        if self.equippable:
            self.equippable.parent = self


class Actor(Entity):
    def __init__(
        self,
        *,
        x=0,
        y=0,
        char="?",
        color: tuple[int, int, int] = (255, 255, 255),
        name="<Unnamed>",
        ai_cls: Type[BaseAI],
        equipment: Equipment,
        fighter: Fighter,
        inventory: Inventory,
        level: Level,
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=True,
            render_order=RenderOrder.ACTOR,
        )

        self.ai: Optional[BaseAI] = ai_cls(self)

        self.equipment = equipment
        self.equipment.parent = self

        self.fighter = fighter
        self.fighter.parent = self

        self.inventory = inventory
        self.inventory.parent = self

        self.level = level
        self.level.parent = self

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)
