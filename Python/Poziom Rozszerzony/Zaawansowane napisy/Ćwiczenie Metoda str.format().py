def fill_in_data(data):
    form = "Nr. Zam�wienia: {}\nNr. Klienta: {}\nImi�: {}\nNazwisko: {}"

    return form.format(data['order_id'], data['client_id'], data['name'], data['family_name'])
