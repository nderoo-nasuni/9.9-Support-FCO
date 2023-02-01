# 9.9 CVM FCO Automation

This directory contains the following files
Support_Account_Tool.py - The python tool that automates comparing the 9.9 customers to the affected customers list.


## How to run
1. Put the list of latest 9.9 customers from the NOC by copying the following request into your browser, you will need to authenticate to the NOC.
   2. https://account.nasuni.com/dashboard/accounts/?tab=everyone&searchtype=Filer&query=build%3E9.9%20build%3C9.10&columns=accountid%2Ccompanyname%2Cfilerid%2Csignup%2Clastactivity%2Cchurned%2Cbuild%2Cguid%2Ccloudcapacity%2Cfiles%2Csubscription&sort=company&sortdir=asc&aggregates=&agghead=false&csv=1 
2. Copy the "accounts.csv" into the folder you have the support tool in or ensure the variable "customers" in Support_Account_Tool.py points to the previously created file and they are either in the same directory or the full path is included.
3. run the script python3 Support_Account_Tool.py 
4. Review the filers in the affected customer list in the output file: CVM_Affected_Customers_upgraded_to_99.csv