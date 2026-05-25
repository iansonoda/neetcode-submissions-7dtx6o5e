class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArray = []

        for i in range(len(position)):
            carArray.append((position[i], speed[i]))

        carArray.sort(reverse=True)

        fleetStack = []

        for car in carArray:
            time = (target - car[0]) / car[1]

            if fleetStack and time <= fleetStack[-1]:
                continue

            elif fleetStack and time >= fleetStack[-1]:
                fleetStack.append(time)

            else:
                fleetStack.append(time)

        return len(fleetStack)
