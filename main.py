#!/usr/bin/python3.8
import os
import datetime
from re import T
from dateutil.relativedelta import relativedelta
from pymongo import collection
from mongo_connection import clientmongo

today = datetime.datetime.today()
print("***** today is:",today," *****")

date_today = today.strftime("%Y%m%d")
print("***** date is:",date_today," *****")

date_year = today.year
# print("year is:",date_year)

# date_month = today.month
# print("month is:",date_month)

# date_day = '{:02d}'.format(today.day)
# print("day is:", date_day)

myyear= str(date_year)
# print("my year is :", myyear)


# print("date is today:",date_today)

one_month = today - relativedelta(months=1)
# print("two_month normal is:",two_month)


two_month = today - relativedelta(months=2)
# print("two_month normal is:",two_month)

# two_month_convert= two_month.strftime("%Y%m%d")
# print("two month ago:",two_month_convert)


# three_month = today - relativedelta(months=3)
# print("three_month normal is:",three_month)

# three_month_convert= three_month.strftime("%Y%m%d")
# print("three month ago:",three_month_convert)

# base = datetime.datetime.today()
base = one_month

# print("base is :",base)
numdays = 100
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
# print(date_list)
# print(date_list[0].strftime("%Y%m%d"))

list_dates=[]
for i in date_list:
    list_dates.append(i.strftime("%Y%m%d"))

# print(list_dates)



# Drop Collection time now

# mydb = clientmongo[myyear]
# mycollection = mydb[date_today]
# result= mycollection.drop()

# print(result)

# Drop Collection time specification

# for day in two_month:

    mydb = clientmongo["archive_error_log"]
    # mycollection = mydb[day]
    collection_lists = (mydb.list_collection_names())


def remove_coll(day):
    mydb = clientmongo["archive_error_log"]
    mycollection = mydb[day]
    # collection_lists = (mydb.list_collection_names())
    result = mycollection.drop()
    print("****","collection", day ,"removed","****")
    
    # print(collection_lists)


    # if day in collection_lists:
    #     print("collection does exists ")
    # else:
    #     print("collection dosn't exists ")

    # print(result)



for day in list_dates:
    # print ("collection name is :" ,day)
    if day in collection_lists:
        print("collection name is :", day ," does exists ")
        remove_coll(day)
    else:
        print("collection name is :", day ," doesn't exists ")
    
