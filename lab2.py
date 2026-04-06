class Hamster():
    def __init__(self, hungry: int, greed: int) -> None:
        self.h: int = hungry
        self.g: int = greed

class Lab2():
    max_hamsters: int = 105
    min_hamsters: int = 1

    max_food_count: int = 109
    min_food_count: int = 0

    @staticmethod
    def calculate_hamsters_value(hamsters: list[Hamster], potential_hamster_count: int) -> list[int]:
        hamsters_value: list[int] = list()
        for i in range(len(hamsters)):
            hamster_value: int = hamsters[i].h + hamsters[i].g * (potential_hamster_count - 1)
            hamsters_value.append(hamster_value)
        return hamsters_value

    @staticmethod
    def quick_sort(unsorted_list: list[int]) -> list[int]:
        if len(unsorted_list) <= 1:
            return unsorted_list

        privot = unsorted_list[len(unsorted_list) // 2]

        left = [element for element in unsorted_list if element < privot]
        middle = [element for element in unsorted_list if element == privot]
        right = [element for element in unsorted_list if element > privot]

        return Lab2.quick_sort(left) + middle + Lab2.quick_sort(right)


    @staticmethod
    def calculate_hamsters(hamsters: list[Hamster], food: int = 0) -> int:
        potential_hamster_count: int = int(len(hamsters) / 2)
        unsorted_hamsters_requied_food: list[int] = list()

        if len(hamsters) > Lab2.max_hamsters:
            while len(hamsters) > Lab2.max_hamsters:
                hamsters.pop()
        elif len(hamsters) < Lab2.min_hamsters:
            raise ValueError("Hamsters Count Cannon Be Less That 1")

        if food > Lab2.max_food_count:
            food = Lab2.max_food_count
        elif food < Lab2.min_food_count:
            food = Lab2.min_food_count

        can_go_up = True
        can_go_down = True
        aproved_hamster_count = 0

        while(True):
            unsorted_hamsters_requied_food: list[int] = Lab2.calculate_hamsters_value(hamsters, potential_hamster_count)
            sorted_hamsters_requied_food: list[int] = Lab2.quick_sort(unsorted_hamsters_requied_food)
            needed_food: int = 0

            i: int = 0

            while i < potential_hamster_count:
                needed_food += sorted_hamsters_requied_food[i]
                i += 1

            print(f"\nUnsorted Hamseters Food Requiments: {unsorted_hamsters_requied_food}")
            print(f"Sorted Hamseters Food Requiments: {sorted_hamsters_requied_food}")
            print(f"Potential Hamseters Count: {potential_hamster_count}")
            print(f"Needed Food: {needed_food}")

            if food >= needed_food:
                aproved_hamster_count  = potential_hamster_count
                if potential_hamster_count >= len(hamsters):
                    return len(hamsters)

            if needed_food <= food and can_go_up:
                potential_hamster_count += 1
                can_go_down = False
            elif needed_food > food and can_go_down:
                potential_hamster_count -= 1
                can_go_up = False
                if potential_hamster_count <= 0:
                    return 0
            else:
                return aproved_hamster_count

hamsters = [Hamster(1,2), Hamster(3,4), Hamster(5,6)]
print(f"\nFinal Hamster Count {Lab2.calculate_hamsters(hamsters,32)}")
