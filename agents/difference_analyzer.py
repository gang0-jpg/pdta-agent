class DifferenceAnalyzer:
    def compare_policy_targets(self, latest_policy, previous_policy):
        latest_map = self._policy_to_map(latest_policy)
        previous_map = self._policy_to_map(previous_policy)

        assets = sorted(set(latest_map.keys()) | set(previous_map.keys()))
        results = []

        for asset in assets:
            latest = latest_map.get(asset, {})
            previous = previous_map.get(asset, {})

            latest_target = latest.get("Target")
            previous_target = previous.get("Target")

            if latest_target is not None and previous_target is not None:
                target_change = latest_target - previous_target
            else:
                target_change = None

            latest_action = latest.get("AdjustedAction") or latest.get("Action")
            previous_action = previous.get("AdjustedAction") or previous.get("Action")

            results.append({
                "Asset": asset,
                "PreviousTarget": previous_target,
                "LatestTarget": latest_target,
                "TargetChange": target_change,
                "PreviousAction": previous_action,
                "LatestAction": latest_action,
                "ActionChanged": previous_action != latest_action,
            })

        return results

    def _policy_to_map(self, policy):
        result = {}

        if not policy:
            return result

        for item in policy:
            asset = item.get("Asset")
            if asset:
                result[asset] = item

        return result
