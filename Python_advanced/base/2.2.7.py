def winner(fig_t, fig_r):
    if fig_t == fig_r:
        return 'ничья'
    elif (fig_t == 'камень' and fig_r == 'ножницы') or (fig_t == 'ножницы' and fig_r == 'бумага') or (fig_t == 'бумага' and fig_r == 'камень'):
        return 'Тимур'
    else:
        return 'Руслан'

print(winner(input(), input()))