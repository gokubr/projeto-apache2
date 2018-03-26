#!/bin/bash

#### ESSE SCRIPT SERVE PARA PARAR E INICIAR OS SERVIÇOS BIND9, NAGIOS3 E FIREWALL######

case $1 in
        bind9) $(systemctl $2 $1) ;;
        nagios) $(systemctl $2 $1) ;;
        firewall) $(bash -c firewall $2) ;;
        *) exit 1 ;;
esac
