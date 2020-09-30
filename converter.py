from _pydecimal import Decimal, Context, ROUND_HALF_UP

def area_proportion(convert_target, full_size):
    new_convert_target = convert_target*100
    result = Context(prec=3, rounding=ROUND_HALF_UP).create_decimal((new_convert_target*100)/full_size)
    return result

# print(type(area_proportion(40, 15200)))
