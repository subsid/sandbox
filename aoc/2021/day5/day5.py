from collections import defaultdict
from typing import List, Iterator


class LineSegment:
    def __init__(self, p1, p2):
        self.x1, self.y1 = p1
        self.x2, self.y2 = p2
        self.is_vertical = self.x1 == self.x2
        self.is_horizontal = self.y1 == self.y2
        if not (self.is_horizontal or self.is_vertical):
            self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        else:
            self.slope = 0
        self.is_diagonal = True if abs(self.slope) == 1 else False

    def points(self) -> List[int]:
        vals = []
        if self.is_vertical:
            end = max(self.y1, self.y2)
            curr = min(self.y1, self.y2)
            while curr <= end:
                vals.append((self.x1, curr))
                curr += 1
        elif self.is_horizontal:
            end = max(self.x1, self.x2)
            curr = min(self.x1, self.x2)
            while curr <= end:
                vals.append((curr, self.y1))
                curr += 1
        elif self.is_diagonal:
            ## Start from left point and go to right point along diagonal.
            if self.x1 < self.x2:
                curr_x = self.x1
                curr_y = self.y1
                end_x = self.x2
            else:
                curr_x = self.x2
                curr_y = self.y2
                end_x = self.x1

            while curr_x <= end_x:
                vals.append((curr_x, curr_y))
                curr_x += 1
                curr_y += self.slope
        else:
            raise ValueError(f"Unsupported line {self}")

        return vals

    def __repr__(self):
        return f"{(self.x1, self.y1)} -> {(self.x2, self.y2)}"


def get_input(mock=False) -> Iterator[LineSegment]:
    mock_input = [
        LineSegment((0, 9), (5, 9)),
        LineSegment((8, 0), (0, 8)),
        LineSegment((9, 4), (3, 4)),
        LineSegment((2, 2), (2, 1)),
        LineSegment((7, 0), (7, 4)),
        LineSegment((6, 4), (2, 0)),
        LineSegment((0, 9), (2, 9)),
        LineSegment((3, 4), (1, 4)),
        LineSegment((0, 0), (8, 8)),
        LineSegment((5, 5), (8, 2)),
    ]
    if mock:
        for l_seg in mock_input:
            yield l_seg
    else:
        for line in open("./input.txt", "r"):
            end_points = map(
                lambda v: map(int, v.strip().split(",")), line.strip().split("->")
            )

            yield LineSegment(*end_points)


def part1(line_segments):
    points = defaultdict(lambda: defaultdict(lambda: 0))

    for line in line_segments:
        if line.is_horizontal or line.is_vertical:
            for point in line.points():
                points[point[0]][point[1]] += 1

    result_ct = 0
    for _, v in points.items():
        for _, ct in v.items():
            if ct >= 2:
                result_ct += 1

    return result_ct


def part2(line_segments):
    points = defaultdict(lambda: defaultdict(lambda: 0))

    for line in line_segments:
        if line.is_horizontal or line.is_vertical or line.is_diagonal:
            for point in line.points():
                points[point[0]][point[1]] += 1

    result_ct = 0
    for _, v in points.items():
        for _, ct in v.items():
            if ct >= 2:
                result_ct += 1

    return result_ct


if __name__ == "__main__":

    assert part1(get_input(mock=True)) == 5
    assert part2(get_input(mock=True)) == 12

    print(part1(get_input(mock=False)))
    print(part2(get_input(mock=False)))
