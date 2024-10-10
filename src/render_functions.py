from __future__ import annotations
from typing import TYPE_CHECKING
import color

if TYPE_CHECKING:
    from tcod.console import Console
    from engine import Engine
    from entity import Actor
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()


def render_bar(
    console: Console, current_value: int, maximum_value: int, total_width: int
) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=0, y=45, width=total_width, height=1, ch=1, bg=color.bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=0, y=45, width=bar_width, height=1, ch=1, bg=color.bar_filled
        )

    console.print(
        x=1, y=45, string=f"HP: {current_value}/{maximum_value}", fg=color.bar_text
    )


def render_xp_bar(
    console: Console,
    player: Actor,
) -> None:
    bar_width = int(
        float(player.level.current_xp) / player.level.experience_to_next_level * 20
    )

    console.draw_rect(x=0, y=46, width=20, height=1, ch=1, bg=color.xp_bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=0, y=46, width=bar_width, height=1, ch=1, bg=color.xp_bar_filled
        )

    console.print(
        x=1,
        y=46,
        string=f"XP: {player.level.current_xp}/{player.level.experience_to_next_level}",
        fg=color.xp_bar_text,
    )


def render_floor(
    console: Console, dungeon_level: int, location: tuple[int, int]
) -> None:
    """
    Render the level the player is currently on, at the given location.
    """
    x, y = location

    console.print(x=x, y=y, string=f"Floor: {dungeon_level}")


def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x, y=mouse_y, game_map=engine.game_map
    )

    console.print(x=x, y=y, string=names_at_mouse_location)