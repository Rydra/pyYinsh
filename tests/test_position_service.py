import pytest

from domain.basic_types import Position
from domain.direction import Direction
from domain.position_service import PositionService


class TestPositionService:

    @pytest.mark.parametrize("src_pos,dest_pos,expected_direction", [
        (Position('D', 5), Position('H', 9), Direction.TOP_RIGHT),
        (Position('E', 1), Position('E', 10), Direction.TOP),
        (Position('G', 8), Position('J', 8), Direction.BOTTOM_RIGHT),
        (Position('G', 8), Position('D', 5), Direction.BOTTOM_LEFT),
        (Position('G', 8), Position('E', 8), Direction.TOP_LEFT),
        (Position('E', 8), Position('G', 8), Direction.BOTTOM_RIGHT),
    ])
    def test_calculate_direction_properly(self, src_pos, dest_pos, expected_direction):
        position_service = PositionService()
        direction = position_service.determine_direction(src_pos, dest_pos)

        assert direction == expected_direction
