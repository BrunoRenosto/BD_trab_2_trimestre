#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

con = pymysql.connect(host='192.168.56.101',
                      user='admin',
                      password='admin123',
                      db='Tarefas',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)

with con:
    reiniciar = 0
    while reiniciar == 0:
        cur = con.cursor()

        #______________________________________________________________________________________________________________________________________________#

        print("Adicionar Tarefa ?")
        x = input()

        if x == "sim" or x == "Sim" or x == "S" or x=="s":
            nome = input()
            data = input()
            prioridade = input()
            cur.execute("INSERT INTO Tarefas.Lista(`Nome`, `data`, `Prioridade`, `Concluida`) VALUES('", nome ,"' ,'", data, "' , '" ,prioridade, "' ,'0')")
            cur.execute("SELECT * FROM Tarefas")

        #______________________________________________________________________________________________________________________________________________#

        print("Concluir tarefa?")


        m = input()
        if m == "sim" or m == "Sim" or m == "S" or m == "s":
            print("qual tarefa(id)?")
            q = int(input())
            cur.execute("UPDATE `Lista` SET `Concluida` = '1' WHERE =",id,";")

        #______________________________________________________________________________________________________________________________________________#

        print("Excluir tarefa ?")
        y = input()
        if y == "sim" or y == "Sim" or y == "S" or y == "s":
            print("Qual(selecione o id)?")
            n = input()
            cur.execute("DELETE FROM `Lista` WHERE `id` = ", n ,";")

        #______________________________________________________________________________________________________________________________________________#

        rows = cur.fetchall()


        for row in rows:
            print(row["Nome"], row["data"], row["Prioridade"], row["Concluida"], row["id"])

        #______________________________________________________________________________________________________________________________________________#

        print("Fechar programa?")
        z = input()
        if z == "sim" or z == "Sim" or z == "S" or z == "s":
            reiniciar = 1
