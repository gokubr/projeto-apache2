#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
usuario=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]

print("content-type: text/html")
print("")

if usuario == "heitor" and senha == "senai132":
    f = open("site/menu.html","r")
    menu = f.read()
    f.close()
   print(menu)
 16 else:
        print("<h1>Usuário ou senha incorreto. Retorne e tente novamente!</h1>")
