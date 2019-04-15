import csv, re

def get_data():
    reg_prod = 'Изготовитель системы'
    reg_name = 'Название ОС'
    reg_code = 'Код продукта'
    reg_type = 'Тип системы'
    reg_val = ':+[\s]*(\w*)'
    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    f = []
    for i in list_files:
        with open(i, 'r') as file:
            for line in file:
                if line.count(reg_prod):
                    l = line
                    r = re.search(reg_val, line)
                    os_prod_list.append(r.group(1))
                elif line.count(reg_name):
                    l = line
                    r = re.search(reg_val, line)
                    os_name_list.append(r.group(1))
                elif line.count(reg_code):
                    l = line
                    r = re.search(reg_val, line)
                    os_code_list.append(r.group(1))
                elif line.count(reg_type):
                    l = line
                    r = re.search(reg_val, line)
                    os_type_list.append(r.group(1))
    for i in range(len(main_data)):
        f.append(os_prod_list[i - 1])
        f.append(os_name_list[i - 1])
        f.append(os_code_list[i - 1])
        f.append(os_type_list[i - 1])
        main_list.append(f)
        f = []


def write_to_csv():
    get_data()
    with open('write.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(main_data)
        for line in main_list:
            writer.writerow(line)


main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
main_list = []
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
a = write_to_csv()

