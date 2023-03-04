def get_first_char(s: str) -> str:
    return s[0]

ch = get_first_char("Orlando")
print(ch)
# print(get_first_char(123))  還是會錯

def calculate_area(h: int, w: int) -> int:
    return h * w

area = calculate_area(3, 2)
print(area)