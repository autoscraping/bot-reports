# -*- coding: utf-8 -*-

import mysql.connector


class ASMysql:
    
    def __init__(self, host, db_name, user, password, port):
        self.__host = host
        self.__db_name = db_name
        self.__user = user
        self.__password = password
        self.__port = port

    def get_connection(self):
        try:
            connection = mysql.connector.connect(host=self.__host,
                                           database=self.__db_name,
                                           password=self.__password,
                                           user=self.__user,
                                           port=self.__port)
            return connection
        except Exception as e:
            raise Exception (f"get_connection(): {e}")

    def read(self, sentence ,connection):
        with connection.cursor() as cursor:
            try:
                cursor.execute(sentence)
                result = cursor.fetchall()
                return result
            except Exception as e:
                raise Exception (f"ASMysql read(): {e}")

    def insert(self, table_name, data_dict, connection):
        with connection.cursor() as cursor:
            try:
                keys = []
                values = []
                places = ",".join(['%s' for val in values])

                for key, value in data_dict.items():
                    keys.append(key)
                    values.append(value)
                
                # Sentence to insert
                sentence = f"INSERT INTO {table_name} (" 
                sentence += ",".join(keys) + ") VALUES ("
                sentence += f"{places} );"

                cursor.execute(sentence, tuple(values))
                connection.commit()
            except Exception as e:
                raise Exception (f"ASMysql insert(): {e}")
    
    def update(self, table_name, data_dict, condition ,connection):
        with connection.cursor() as cursor:
            try:
               
               
                key_value = []
                for key, value in data_dict.items():
                    key_value.append(f"{key}={value}")
                
                key_value = ",".join(key_value)
                
                # Sentence to insert
                sentence = f"UPDATE {table_name} SET {key_value} WHERE {condition}"

                cursor.execute(sentence)
                connection.commit()
            except Exception as e:
                raise Exception (f"ASMysql update(): {e}")

    def sp(self, sp_name, data_list):

            try:
                connection = self.get_connection()
                cursor = connection.cursor()

                sentence = f"call {sp_name}"

                for elem in data_list:
                    # print(len(elem))
                    for count, i in enumerate(elem):
                        if count == 0:
                            # is the first
                            sentence+="(%s,"
                        elif (count+1) == len(elem):
                            # is the last
                            sentence+=" %s)"
                        else:
                            # is in the middle
                            sentence+=" %s,"
                    break

                cursor.executemany(sentence, data_list)
                connection.commit()
                connection.close()
            except Exception as e:
                raise Exception(f"ASMysql sp(): {e}")