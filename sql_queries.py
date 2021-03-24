# -*- coding: utf-8 -*-
import sqlite3
from google.colab import drive
import pandas as pd
drive.mount('/content/drive')

#Connect to the database file in your Google Drive. Adjust the path if necessary.
conn = sqlite3.connect('/content/drive/My Drive/31-M29/Chinook_Sqlite.sqlite') #from https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite

"""### 0. Find all information on the employees (i.e., show the table "Employee")."""

pd.read_sql_query("SELECT * FROM Employee", conn)

"""### 1. Find the first name and the last name of all customers."""

pd.read_sql_query("SELECT FirstName, LastName FROM Customer", conn)

"""### 2. Find all invoices with a total (amount) below 5 (i.e, the entry in the column Total is < 5)."""

pd.read_sql_query("SELECT * FROM Invoice WHERE Total <5", conn)

"""### 3. Find all customers from Germany. Tip: This might be helpful: https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks"""

pd.read_sql_query("SELECT * FROM Customer WHERE Country = 'Germany'", conn)

"""### 4. Find all customers that are not from Canada."""

pd.read_sql_query("SELECT * FROM Customer WHERE Country != 'Canada'", conn)

"""### 5. List the last nam of all employees  in alphabetical order without duplicates"""

pd.read_sql_query("SELECT DISTINCT LastName FROM Employee ORDER BY LastName", conn)

"""### 6. Find all employees that work in IT (IT Manger and IT Staff) and list their first name and their last name."""

pd.read_sql_query("SELECT FirstName,LastName,Title FROM Employee WHERE Title LIKE 'IT%'", conn)

"""### 7. Show the invoice date and the first name and the last name of the customor for each invoice. Tip: You have to join two tables."""

pd.read_sql_query("SELECT InvoiceDate,FirstName,LastName FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId" , conn)

"""8. Show the invoice date and the first name and the last name of the customor for invoices where the customer is from Germany."""

pd.read_sql_query("SELECT InvoiceDate,FirstName,LastName FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId WHERE c.Country = 'Germany'" , conn)

"""### 9. For each BillingCountry, find the number of invoices with that BillingCountry.  Show only the columns "BillingCountry" and "count(*)". Tip: You have to use GROUP BY."""

pd.read_sql_query("SELECT BillingCountry, COUNT(*) FROM Invoice GROUP BY BillingCountry", conn)

"""### 10. For each BillingCountry, find the average invoice amount for invoices with that BillingCountry. Show only the columns "BillingCountry" and "AVG(total)"."""

pd.read_sql_query("SELECT BillingCountry,AVG(total) FROM Invoice GROUP BY BillingCountry", conn)

"""### 11. For each customer, find the total amount  that the customer spend in the shop (). Tip: You have to join two tables and use GROUP BY."""

pd.read_sql_query("SELECT c.CustomerId,c.FirstName,c.LastName,c.Country,SUM(i.Total) as spend_total FROM INVOICE i INNER JOIN CUSTOMER c ON c.CustomerId = i.CustomerId GROUP BY c.CustomerID ORDER BY spend_total DESC",conn)

"""### 12. For each customer from Germany, find the average amount  that the customer spend in the shop (). Tip: You have to join two tables and use GROUP BY."""

pd.read_sql_query("SELECT c.CustomerId,c.FirstName,c.LastName,c.Country,ROUND(AVG(i.Total),2) as spend_average FROM Invoice i INNER JOIN  Customer c ON c.CustomerId = i.CustomerId WHERE c.Country = 'Germany' GROUP BY c.CustomerID ORDER BY spend_average DESC",conn)

conn.close()
