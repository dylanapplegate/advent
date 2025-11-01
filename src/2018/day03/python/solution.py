from typing import cast
import re

def get_fabric_tuple(line: str) -> tuple[int, int, int, int, int]:
    # Replace individual characters we don't really care about
    nums_str = re.findall(r'\d+', line)
    result_tuple = tuple(map(int, nums_str));

    if len(result_tuple) != 5:
        raise ValueError("Incorrect length")

    return result_tuple



def format_data(input: str) -> list[tuple[int, int, int, int, int]]:
     # (id, y, x, width, height)
     return [get_fabric_tuple(line) for line in input.strip().splitlines()
             if line.strip()]


def get_claims_map(claims: list[tuple[int, int, int, int, int]]) -> dict[tuple[int, int],  list[int]]:
    claims_map = {}

    for claim_id, oy, ox, h, w in claims:
        for dy in range(h):
            for dx in range(w):
                coord = (oy + dy, ox + dx)
                claims_map.setdefault(coord, []).append(claim_id)

    return claims_map

def part1(input):
    claims = format_data(input)
    claims_map = get_claims_map(claims)

    return sum(len(claim_ids) > 1 for claim_ids in claims_map.values())

def part2(input):
    claims = format_data(input)
    claims_map = get_claims_map(claims)

    possible_claims: set[int] = {c[0] for c in claims}
    invalid_claims: set[int] = set()

    for claim_ids in claims_map.values():
        if len(claim_ids) > 1:
            invalid_claims.update(claim_ids)

    valid_claims = possible_claims.difference(invalid_claims)

    return list(valid_claims)[0]

