from collections import deque


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None
        total_litter = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = total_litter
                    total_litter += 1

        if total_litter == 0:
            return 0

        target = (1 << total_litter) - 1

        queue = deque()
        queue.append((start[0], start[1], 0, energy, 0))

        visited = set()
        visited.add((start[0], start[1], 0, energy))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, current_energy, moves = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if current_energy == 0:
                    continue

                new_energy = current_energy - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    bit = 1 << litter[(nr, nc)]
                    new_mask |= bit

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                if new_mask == target:
                    return moves + 1

                state = (nr, nc, new_mask, new_energy)

                if state not in visited:
                    visited.add(state)
                    queue.append(
                        (nr, nc, new_mask, new_energy, moves + 1)
                    )

        return -1