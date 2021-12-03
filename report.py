from aslibs import mysql_methods, log
from constants import DB_Credentials
import csv




class report:
    def __init__(self):
        self.__logger = log.Log().get_logger(name='report')
        self.__mysql_obj = mysql_methods.ASMysql(DB_Credentials['dan-black']['host'],
                                         DB_Credentials['dan-black']['db_name'],
                                         DB_Credentials['dan-black']['user'],
                                         DB_Credentials['dan-black']['password'],
                                         DB_Credentials['dan-black']['port'])

    def query(self, query, csv_name):
        

        try:
            dict_list = []
            self.__logger.info(f"Generating report: {csv_name}")
            result = self.__mysql_obj.read(query ,self.__mysql_obj.get_connection())
            if result:
                for row in result:
                    row_dict = {
                        'source_name':str(row[0]),
                        'Dispensary':str(row[1]),
                        'Address':str(row[2]),
                        'City':str(row[3]),   
                        'Latitude':str(row[4]),
                        'Longitude':str(row[5]),
                        'source_id':str(row[6]),
                        'Item':str(row[7]),
                        'Brand':str(row[8]),
                        'Category':str(row[9]),
                        'Price':str(row[10]),
                        'Size':str(row[11]),
                        'scraped_date':str(row[12])
                    }
                    dict_list.append(row_dict)
                with open(csv_name, 'w', encoding="utf-8") as f:  
                    writer = csv.DictWriter(f,delimiter =",", fieldnames=row_dict.keys())
                    writer.writeheader()
                    for elem in dict_list:
                        writer.writerow(elem)
                self.__logger.info(f"Report: {csv_name} finished")
            else:
                self.__logger.info(f"There is not data match for input parameters")
        except Exception as e:
            self.__logger.error(f"error: {e}")