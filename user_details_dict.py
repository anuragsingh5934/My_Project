def usr_info_dict(owner_name,car_name,buy_year,cc,color,known_prob="None",modification=None):
    '''This function buid user profile in dictionary'''
    user_data_report = {
            'Owner name': owner_name, 'car name': car_name,
            'year of purchase': buy_year,'engine size': cc,
            'car color': color, 'known problem': known_prob,
            'modification': modification 
            }
    if modification:
        return user_data_report
    else:
        del user_data_report['modification']
        return user_data_report