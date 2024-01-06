#!/bin/bash

echo -e "\e[32m
"

figlet "WELCOME"
sleep 0.1
figlet "TO"
sleep 0.1
figlet "WHATSAPP"
sleep 0.1
figlet "AUTO"
sleep 0.1
figlet "MESSAGE"
sleep 0.1
figlet " SENDER"
sleep 0.1

echo -e "\e[31m
"
echo Send whatsapp messages directly through terminal

echo -e "\n"

echo  -e "\033[0;95m
"

echo Author : Sourabh Dey


echo -e "\e[31m
"


echo -e "\n"


read -p "Enter Your countrycode : + " Cc

read -p "Enter Sender's whatsapp number : " Num

read -p "Enter message to be send : " mess



echo -e "\e[34m
"
figlet " Opening "

figlet "and"

figlet "and"

figlet "sending"

figlet "message"



xdg-open https://wa.me/$Cc$Num/?text=$mess
