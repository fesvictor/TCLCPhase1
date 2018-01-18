def get_year_table(year, party_list, leader_list):
    year_table = {}
    for year in year:
        year_table[year] = get_month_list();
        for key, value in year_table[year].items():
            year_table[year][key]['party'] = {}
            for party in party_list:
                year_table[year][key]['party'][party.get_name()[0]] = get_day_list()
            year_table[year][key]['leader'] = {}
            for leader in leader_list:
                year_table[year][key]['leader'][leader.get_name()[0]] = get_day_list()
    return year_table


def get_month_list():
    # Note: range(1,3) = [1,2]
    month_list = dict.fromkeys(map(pad2digit, range(1, 13)), {})
    return month_list

def get_day_list():
    day_list = dict.fromkeys(map(pad2digit, range(1, 32)), [0, 0])
    return day_list

def pad2digit(x):
    return str(x).zfill(2)