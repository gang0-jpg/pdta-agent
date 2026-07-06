from database.db import get_connection


class MemoryAgent:
    def latest(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, run_at, version, market, portfolio,
                           recommendation, decision, policy, investor_note
                    FROM pdta_memory
                    ORDER BY id DESC
                    LIMIT 1
                """)
                row = cur.fetchone()

        if row is None:
            return None

        return self._row_to_dict(row)

    def history(self, limit=5):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, run_at, version, market, portfolio,
                           recommendation, decision, policy, investor_note
                    FROM pdta_memory
                    ORDER BY id DESC
                    LIMIT %s
                """, (limit,))
                rows = cur.fetchall()

        return [self._row_to_dict(row) for row in rows]

    def compare_last_two(self):
        memories = self.history(limit=2)

        if len(memories) < 2:
            return {"message": "Not enough memory records to compare."}

        latest = memories[0]
        previous = memories[1]

        latest_actions = self._extract_actions(latest["policy"])
        previous_actions = self._extract_actions(previous["policy"])

        return {
            "latest_id": latest["id"],
            "previous_id": previous["id"],
            "added_actions": sorted(list(latest_actions - previous_actions)),
            "removed_actions": sorted(list(previous_actions - latest_actions)),
            "unchanged_actions": sorted(list(latest_actions & previous_actions)),
        }

    def _extract_actions(self, policy):
        actions = set()

        if not policy:
            return actions

        if isinstance(policy, list):
            for item in policy:
                asset = item.get("Asset")
                action = item.get("AdjustedAction") or item.get("Action")
                if asset and action:
                    actions.add(f"{action} {asset}")

        return actions

    def _row_to_dict(self, row):
        return {
            "id": row[0],
            "run_at": row[1],
            "version": row[2],
            "market": row[3],
            "portfolio": row[4],
            "recommendation": row[5],
            "decision": row[6],
            "policy": row[7],
            "investor_note": row[8],
        }
