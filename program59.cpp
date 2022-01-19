{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 //name:Britney Huiracocha\
//email:britney.huiracocha44@myhunter.cuny.edu\
//date:November 29, 2020\
//this program writes a C++ program that asks the user\
\
#include <iostream>\
using namespace std;\
\
int main()\
\{\
    float amount, interest , amount2, i;\
    cout<< "please enter the starting amount: ";\
    cin>>amount;\
    interest = amount*0.03;\
    amount2 = amount;\
    i = 0;\
\
    while ((amount2 - amount) < 1000)\
    \{\
        amount2 = amount2 + amount2*0.03;\
        i+=1;\
        cout<<"year"<<i<<" "<<amount2 <<endl;\
    \}\
    return 0;\
\}}