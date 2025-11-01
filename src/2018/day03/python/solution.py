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


def get_claims_map(claims):
    claims_map = {}

    for claim_id, oy, ox, h, w in claims:
        for dy in range(h):
            for dx in range(w):
                coord = (oy + dy, ox + dx)
                current_claims = claims_map.pop(coord, [])
                claims_map[coord] = [*current_claims, claim_id]
    return claims_map

def part1(input):
    claims = format_data(input)
    claims_map = get_claims_map(claims)

    return sum(len(claim_ids) > 1 for coord, claim_ids in claims_map.items())

def part2(input):
    claims = format_data(input)
    claims_map = get_claims_map(claims)
    possible_claims = {
        claim
        for claims in claims_map.values()
        for claim in claims
    }

    invalid_claims = {
        claim
        for claims in claims_map.values()
        for claim in claims
        if len(claims) > 1
    }

    valid_claims = possible_claims.difference(invalid_claims)

    return list(valid_claims)[0]

