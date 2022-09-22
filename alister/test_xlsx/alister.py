person = {}
data_string = 'Sotinov Moscow 84957850000 +79890002112'


def create_dict(data_string):
    data_string = data_string.split()
    person['family'] = data_string[0]
    person['city'] = data_string[1]
    person['tel_num'] = []
    for i in data_string[2:]:
        person['tel_num'].append(i)
    print(person)


data_base = {'family': ['Ivanov', 'Petrov', 'Sidorov', 'Galeichenko', 'family', 'family'],
             'city': ['Moscow', 'Orel', 'Tula', 'Kyrsk', 'Bolgograd', 'Rostov'],
             'tel_number': ['89012023432',
                            '+79014568880',
                            '79994140000',
                            '9342009191',
                            '88632450919',
                            '2567895']}


class Build:
    def load_string_xlsx(self):
        pass

    def save_dictionary(self):
        pass

    def len_number(self):
        pass

    def city(self):
        pass


def city_code(city):
    city_code_number = ''
    tel_dict = {'Rostov': '863', 'Moscow': '495'}
    for key in tel_dict:
        if key == city:
            return tel_dict[city]
    # except KeyError:
    #     print('Uncon')


def result(data_base):
    tel = data_base['tel_number']
    new_tel_list = []
    for tn in tel:
        if [tn][0][0] == '+':
            new_tel_list.append(tn)
        elif [tn][0][0] == '8':
            new_tel_list.append('+7' + tn[1:])
        elif [tn][0][0] == '7':
            new_tel_list.append('+7' + tn[1:])
        elif len([tn][0]) == 10:
            new_tel_list.append('+7' + tn[0:])
        elif len([tn][0]) == 7:
            new_tel_list.append('+7' + city_code(city='Rostov') + tn[0:])
    print('new_tel_list', new_tel_list)


if __name__ == '__main__':
    # pass
    result(data_base=data_base)
    # create_dict(data_string=data_string)
    # city_code('Rostov')
