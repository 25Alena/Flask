import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM comands'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ошибка чтения из БД')
            return False
        return []

    def addCommand(self, name_of_comand, achivements, sostav, identif):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO comands VALUES (NULL, ?,?,?,?,?)', (name_of_comand, achivements, sostav, identif, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления команды в БД ' + str(e))
        return True


    def getCommand(self):
        try:
            self.__cur.execute(f"SELECT id, name_of_comand, achivements, sostav, identif FROM comands")
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ошибка получения списка комманд из БД', )
            return False
        return []


    def delCommand(self, id):
        try:
            self.__cur.execute(f"DELETE FROM comands WHERE id = ?", (id,))
            res = self.__cur.fetchall()
            self.__db.commit()
            if res: return res
        except:
            print('Ошибка получения списка комманд из БД', )
            return False
        return []


    def getUser(self):
        try:
            self.__cur.execute(f"SELECT id, login, psw FROM users")
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ошибка получения списка комманд из БД', )
            return False
        return []


    def addUser(self, login, psw):
        try:
            self.__cur.execute('INSERT INTO users VALUES (NULL, ?,?)', (login, psw))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления пользователя в БД ' + str(e))
        return True

    # def delCommand(self, id):
    #     sql = 'DELETE FROM comands WHERE id = ?'
    #     try:
    #         self.cursor.execute(sql, (id,))
    #         res = self.cursor.fetchall()
    #         if res: return res;
    #     except:
    #         print('Ошибка чтения бд')