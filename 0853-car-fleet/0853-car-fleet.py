class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        # Pair each car's position with its arrival time and sort in descending order of position
        cars = sorted([(position[i], (target - position[i]) / speed[i]) for i in range(n)], reverse=True)

        fleet_count = 0
        latest_arrival_time = 0  # Initialize to a value that will always be less than any car's arrival time

        for position, arrival_time in cars:
            # If this car's arrival time is greater than the latest, it forms a new fleet
            if arrival_time > latest_arrival_time:
                fleet_count += 1
                latest_arrival_time = arrival_time

        return fleet_count