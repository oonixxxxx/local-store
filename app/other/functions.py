def return_anketa(name, adress):
    return f'Имя: {name} \nАдрес: {adress} \nОформил заказ на товар с артикулем "артикуль" "нейм товара" по стоимости "стоимость товара" \nЧек приложен:'

def get_finally_summ(lst_articules):
    result = 0
    for i in lst_articules:
        result += int(i)

    return int(result)