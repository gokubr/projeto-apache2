#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()

import os
menu=var.split("=")[0]
print("content-type: text/html")
print("")

if menu == "d_i":
        os.system("sudo /etc/firewall/script.sh bind9 start")
        print "O serviço Bind9 foi iniciado com sucesso!"
elif menu == "d_p":
        os.system("sudo /etc/firewall/script.sh bind9 stop")
        print "O serviço Bind9 foi pausado com sucesso!"
elif menu == "d_r":
        os.system("sudo /etc/firewall/script.sh bind9 restart")
        print "O serviço Bind9 foi reiniciado com sucesso!"
elif menu == "f_i":
        os.system("sudo /etc/firewall/script.sh firewall start")
        print "O serviço Firewall foi iniciado com sucesso!"
elif menu == "f_p":
        os.system("sudo /etc/firewall/script.sh firewall stop")
        print "O serviço Firewall foi pausado com sucesso!"
elif menu == "f_r":
        os.system("sudo /etc/firewall/script.sh firewall restart")
        print "O serviço Firewall foi reiniciado com sucesso!"
elif menu == "n_i":
        os.system("sudo /etc/firewall/script.sh nagios start")
        print "O serviço Nagios3 foi iniciado com sucesso!"
elif menu == "n_p":
        os.system("sudo /etc/firewall/script.sh nagios stop")
        print "O serviço Nagios3 foi pausado com sucesso!"
elif menu == "n_r":
        os.system("sudo /etc/firewall/script.sh nagios restart")
        print "O serviço Nagios3 foi reiniciado com sucesso!"
