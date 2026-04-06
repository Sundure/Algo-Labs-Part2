class Lab1():
    @staticmethod
    def zig_zag_sort(matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
            
        current_cycle = 0
        current_column = 0
        reverse = True
        final_list = []
        
        while True:
            if len(final_list) >= len(matrix) * len(matrix[0]):
                return final_list

            if reverse:
                current_column = min(current_cycle, len(matrix) - 1)
            else:
                current_column = max(0, current_cycle - len(matrix[0]) + 1)

            while current_column in range(len(matrix)):
                if current_column > current_cycle or current_cycle - current_column >= len(matrix[0]):
                    break
                final_list.append(matrix[current_column][current_cycle - current_column])
                if reverse:
                    current_column -= 1
                else:
                    current_column += 1

            reverse = not reverse
            current_cycle += 1
