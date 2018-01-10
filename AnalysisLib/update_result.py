def update_result(_location, _table, _type):
    year_list = ['17']
    month_list = ['01', '02','03','04','05','06','07','08','09','10','11','12']
    for _year in year_list:
        if _year in _table:
            for _month in month_list:
                if _month in _table[_year]:
                    #if _table[_year][_month] != {}:
                        with open(_location + '/leader/' + '20' + _year + '_' + _month + '_' + _type + '_leader.csv', 'w') as outFile:
                            if _month is "02":
                                if((int(_year)%4)==0):
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29")
                                    for key, value in _table[_year][_month]['leader'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]))        
                                else:
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28")
                                    for key, value in _table[_year][_month]['leader'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]))        
                                   

                            elif ((int(_month)%2)!= 0) or _month is "08":
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31")
                                    for key, value in _table[_year][_month]['leader'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]) + ','+ str(value['30'][i]) + ','+ str(value['31'][i]))                                    
                            else:
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30")
                                    for key, value in _table[_year][_month]['leader'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]) + ','+ str(value['30'][i]))                               

                        with open(_location + '/party/' + '20' + _year + '_' + _month + '_' + _type + '_party.csv', 'w') as outFile:
                            if _month is "02":
                                if((int(_year)%4)==0):
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29")
                                    for key, value in _table[_year][_month]['party'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]))        
                                else:
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28")
                                    for key, value in _table[_year][_month]['party'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]))        
                                   

                            elif ((int(_month)%2)!= 0) or _month is "08":
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31")
                                    for key, value in _table[_year][_month]['party'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]) + ','+ str(value['30'][i]) + ','+ str(value['31'][i]))                                    
                            else:
                                    outFile.write("name,scale,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30")
                                    for key, value in _table[_year][_month]['party'].items():
                                        for i, x in enumerate(value['01'], 0):
                                            outFile.write('\n')
                                            outFile.write(key + ',' + str(i+1) + ',' + str(value['01'][i]) + ',' + str(value['02'][i]) + ','+ str(value['03'][i]) + ','+ str(value['04'][i]) + ','+ str(value['05'][i]) + ','+ str(value['06'][i]) + ','+ str(value['07'][i]) + ','+ str(value['08'][i]) + ','+ str(value['09'][i]) + ','+ str(value['10'][i]) + ','+ str(value['11'][i]) + ','+ str(value['12'][i]) + ','+ str(value['13'][i]) + ','+ str(value['14'][i]) + ','+ str(value['15'][i]) + ','+ str(value['16'][i]) + ','+ str(value['17'][i]) + ','+ str(value['18'][i]) + ','+ str(value['19'][i]) + ','+ str(value['20'][i]) + ','+ str(value['21'][i]) + ','+ str(value['22'][i]) + ','+ str(value['23'][i]) + ','+ str(value['24'][i]) + ','+ str(value['25'][i]) + ','+ str(value['26'][i]) + ','+ str(value['27'][i]) + ','+ str(value['28'][i]) + ','+ str(value['29'][i]) + ','+ str(value['30'][i]))                               
