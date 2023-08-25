class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        result = ''
        list = []
        for i in range(num_rows):
            list.append('')

        row_num = 0
        flag = True
        for ch in s:
            list[row_num] += ch
            if row_num == num_rows - 1:
                flag = False
            if row_num == 0:
                flag = True
            if flag:
                row_num += 1
            else: 
                row_num -= 1

        for i in range(num_rows):
            result += list[i]
        
        return result