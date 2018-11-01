import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 10)

df = pd.read_csv('all_prices_filled.csv', sep=',')
writer = pd.ExcelWriter("Отчет.xlsx", engine='xlsxwriter')
df1 = df.head(10)
df1.to_excel(writer, sheet_name='report')

workbook = writer.book
worksheet = writer.sheets['report']


def check_df(df):
    if isinstance(df, pd.DataFrame):
        pass
    else:
        raise ValueError(
            'Параметры не соответствуют объектам pandas. Проверь следующие параметры: датафрейм, страница, книга')


def barcode_to_int(dataframe, worksheet, workbook, header):
    check_df(dataframe)
    if isinstance(header, str):
        counter_barcode = 1
        f3 = workbook.add_format({'num_format': '0'})
        for i in dataframe:
            for value in dataframe[i]:
                if i == header:
                    column_index = dataframe.columns.get_loc(header)
                    worksheet.write(counter_barcode, column_index + 1, value, f3)
                    counter_barcode += 1
    else:
        raise ValueError('Название признака не строка')


def price_to_int(dataframe, worksheet, workbook, header):
    check_df(dataframe)  # проверка на датафрейм
    if isinstance(header, str):
        counter = 1
        f1 = workbook.add_format({'num_format': '0.00'})  # числовые форматы для разных типов цен
        f2 = workbook.add_format({'num_format': '0.0'})
        f3 = workbook.add_format({'num_format': '0'})
        for i in dataframe:
            if i == header:
                for value in dataframe[i]:
                    value = str(value)
                    if value.find('.') and len(value[value.index('.'):]) == 3:  # проверяю кол-во знаков после запятой
                        column_index = dataframe.columns.get_loc(header)
                        value = float(value)
                        worksheet.write_number(counter, column_index + 1, value, f1)
                        counter += 1
                    elif value.find('.') and len(value[value.index('.'):]) == 2 and value[-1] != '0':
                        column_index = dataframe.columns.get_loc(header)
                        value = float(value)
                        worksheet.write_number(counter, column_index + 1, value, f2)
                        counter += 1
                    else:
                        column_index = dataframe.columns.get_loc(header)
                        value = int(float(value))
                        worksheet.write_number(counter, column_index + 1, value, f3)
                        counter += 1
            else:
                print('Признак "{}" не был отформатирован'.format(i))
    else:
        raise ValueError('Название признака не строка')


barcode_to_int(df1, worksheet, workbook, "ШТРИХКОД")
price_to_int(df1, worksheet, workbook, "Цена по карте клиента")
price_to_int(df1, worksheet, workbook, "Цена конкурента (без карты)")
price_to_int(df1, worksheet, workbook, "Цена по акции")

writer.save()
