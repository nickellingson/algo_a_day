class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # create list of lists
        cars = [[p, s]for p, s in zip(position, speed)]

        fleet_stack = []

        for p, s in reversed(sorted(cars)):

            # calculate how long it takes to reach target
            time = (target - p) / s

            # place time on top of stack
            fleet_stack.append(time)

            # check whether stack is greater than 2
            # check top element less than element below
            if len(fleet_stack) >= 2 and fleet_stack[-1] <= fleet_stack[-2]:
                fleet_stack.pop()

        return len(fleet_stack)