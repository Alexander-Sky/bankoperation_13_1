amount = 197533806
amount_rouble = amount // 100
amount_kop = amount % 100
total_amount = f'{amount_rouble} руб. {amount_kop} коп.'
print(total_amount)