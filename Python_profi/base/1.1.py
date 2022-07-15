
def hide_card(card_number):
    card_number = card_number.replace(' ', '')
    res = ''
    for i, item in enumerate(card_number):
        if item.isdigit():
            res += '*'
            if len(res) == 12 and len(card_number) > 12:
                res += ''.join(list(card_number)[i+1:])
                break
    return res


# just beauty
# def hide_card(card_number):
#     return '*' * 12 + card_number.replace(' ', '')[12:]