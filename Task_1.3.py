# Zadanie: poszerzony raport

name_cheese1 = 'raquefort'
name_cheese2 = 'stilton'
name_cheese3 = 'brie'
name_cheese4 = 'gouda'
name_cheese5 = 'edam'
name_cheese6 = 'parmezan'
name_cheese7 = 'mozzarella'
name_cheese8 = 'czechosłowacki ser z owczego mleka'

price_cheese1 = 12.50
price_cheese2 = 11.24
price_cheese3 = 9.30
price_cheese4 = 8.55
price_cheese5 = 11.00
price_cheese6 = 16.50
price_cheese7 = 14.00
price_cheese8 = 122.32

weight_cheese1 = 2
weight_cheese2 = 1
weight_cheese3 = 1
weight_cheese4 = 1
weight_cheese5 = 1
weight_cheese6 = 3.5
weight_cheese7 = 0.13
weight_cheese8 = 0.22

price_summary = weight_cheese1 * price_cheese1 + weight_cheese2 * price_cheese2 +\
    weight_cheese3 * price_cheese3 + weight_cheese4 * price_cheese4 +\
    weight_cheese5 * price_cheese5 + weight_cheese6 * price_cheese6 +\
    weight_cheese7 * price_cheese7 + weight_cheese8 * price_cheese8

main_report = f"Raport z zakupów\n\
- {name_cheese1}, {weight_cheese1}kg, {price_cheese1} zł\n\
- {name_cheese2}, {weight_cheese2}kg, {price_cheese2} zł\n\
- {name_cheese3}, {weight_cheese3}kg, {price_cheese3} zł\n\
- {name_cheese4}, {weight_cheese4}kg, {price_cheese4} zł\n\
- {name_cheese5}, {weight_cheese5}kg, {price_cheese5} zł\n\
- {name_cheese6}, {weight_cheese6}kg, {price_cheese6} zł\n\
- {name_cheese7}, {weight_cheese7}kg, {price_cheese7} zł\n\
- {name_cheese8}, {weight_cheese8}kg, {price_cheese8} zł\n\
...\n\
Suma {price_summary}"

print(main_report)