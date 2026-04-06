class Lab5:
    @staticmethod
    def flood_fill(matrix, y, x, target_color, replacement_color):
        if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
            return
        
        if matrix[y][x] != target_color:
            return
        
        matrix[y][x] = replacement_color
        
        Lab5.flood_fill(matrix, y - 1, x, target_color, replacement_color)
        Lab5.flood_fill(matrix, y + 1, x, target_color, replacement_color)
        Lab5.flood_fill(matrix, y, x - 1, target_color, replacement_color)
        Lab5.flood_fill(matrix, y, x + 1, target_color, replacement_color)

class Program:
    @staticmethod
    def main():
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        height, width = map(int, lines[0].strip().split(','))
        start_y, start_x = map(int, lines[1].strip().split(','))
        
        replacement_color = lines[2].strip().replace("'", "").replace("‘", "").replace("’", "")

        matrix = []
        for line in lines[3:]:
            row = [char for char in line if char.isalpha()]
            if row:
                matrix.append(row)

        target_color = matrix[start_y][start_x]

        if target_color != replacement_color:
            Lab5.flood_fill(matrix, start_y, start_x, target_color, replacement_color)

        with open('output.txt', 'w', encoding='utf-8') as f:
            for i in range(len(matrix)):
                row_str = "['" + "', '".join(matrix[i]) + "']"
                if i < len(matrix) - 1:
                    f.write(row_str + ",\n")
                else:
                    f.write(row_str + "\n")

Program.main()
