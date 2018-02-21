#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import timedelta, date
import pandas as pd
import numpy as np
import warnings
import requests
import sqlalchemy 
import airports


def configure_engine():
    DB_TYPE = 'mysql'
    DB_DRIV = 'pymysql'
    DB_USER = 'DBUSER'
    DB_PASS = 'PASSWORD'
    DB_HOST = 'IP'
    DB_NAME = 'DBNAME'
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s/%s' % (DB_TYPE, DB_DRIV, DB_USER, DB_PASS, DB_HOST, DB_NAME)

    return SQLALCHEMY_DATABASE_URI

def create_table():
    POOL_SIZE = 50

    metadata = sqlalchemy.MetaData()

    TABLENAME = 'weather'

    ENGINE = sqlalchemy.create_engine(
        configure_engine(), pool_size=POOL_SIZE, max_overflow=0)

    t = sqlalchemy.Table(TABLENAME, metadata, 
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
        sqlalchemy.Column('DateTime', sqlalchemy.DATETIME),
        sqlalchemy.Column('Airport-code', sqlalchemy.VARCHAR(10)),
        sqlalchemy.Column('Temperature', sqlalchemy.DECIMAL(3,1)),
        sqlalchemy.Column('Dew-Point', sqlalchemy.DECIMAL(3,1)),
        sqlalchemy.Column('Humidity', sqlalchemy.VARCHAR(10)),
        sqlalchemy.Column('Pressure-hPa', sqlalchemy.INTEGER),
        sqlalchemy.Column('Visibility-km', sqlalchemy.DECIMAL(3,1)),
        sqlalchemy.Column('Wind-Dir', sqlalchemy.VARCHAR(10)),
        sqlalchemy.Column('Conditions', sqlalchemy.TEXT),
        sqlalchemy.Column('Wind-Speed-kmh', sqlalchemy.DECIMAL(3,1)),
        sqlalchemy.Column('Wind-Speed-ms', sqlalchemy.DECIMAL(3,1))
        )
    t.create(ENGINE)


def read_text(link):
    page = requests.get(link)
    return page.text

def get_data_between_texts(raw_text, text1, text2, include_texts=True):
    index1 = raw_text.find(text1)
    index2 = raw_text.find(text2)
    if(include_texts):
        filtered = raw_text[index1:index2+len(text2)]
    else:
        filtered = raw_text[index1+len(text1):index2]
    return filtered

def get_weather_table(url):
    full_html = read_text(url)
    table_header = '<table cellspacing="0" cellpadding="0" id="obsTable" class="obs-table responsive">'
    table_footer = '<div class="obs-table-footer">'
    table = get_data_between_texts(full_html, table_header, table_footer)
    return pd.read_html(table, header=0)[0]

def generate_weather_information(airport_code, year, month, day):
    LINK = 'https://www.wunderground.com/history/airport/%s/%s/%s/%s/DailyHistory.html' % (airport_code, year, month, day)
    try:
        df = get_weather_table(LINK)
    except:
        return pd.DataFrame()

    #Drop columns that not appair for all airports.
    if unicode('Heat Index',"utf-8") in df.columns:
        df = df.drop('Heat Index', 1)

    if unicode('Windchill',"utf-8") in df.columns:
        df = df.drop('Windchill', 1)
    
    df = df.drop('Gust Speed', 1)
    df = df.drop('Events', 1)
    df = df.replace(np.nan, 'NA', regex=True)
    df = df[df['Precip'] == 'NA']
    df = df[df['Humidity'] != 'N/A%']
    df = df.drop('Precip', 1)
    df['Temp.'] = df['Temp.'].map(lambda x: x.rstrip(unicode(' °C',"utf-8")).replace('- ','0.0').replace(u'\xa0', u''))
    df['Dew Point'] = df['Dew Point'].map(lambda x: x.rstrip(unicode(' °C',"utf-8")).replace('- ','0.0').replace(u'\xa0', u''))
    df['Wind Speed'] = df['Wind Speed'].map(lambda x: x.replace('Calm','0.0 km/h  / 0.0 m/s').replace('-','0.0 km/h  / 0.0 m/s').replace(u'\xa0', u''))
    df['Wind-Speed-kmh'] = df['Wind Speed'].map(lambda x: x.split('  / ')[0].rstrip(unicode(' km/h',"utf-8")).replace(u'\xa0', u''))
    df['Wind-Speed-ms'] = df['Wind Speed'].map(lambda x: x.split('  / ')[1].rstrip(unicode(' m/s',"utf-8")).replace(u'\xa0', u''))
    df = df.drop('Wind Speed', 1)
    df['Pressure'] = df['Pressure'].map(lambda x: x.rstrip(unicode(' hPa',"utf-8")).replace('-','0.0').replace(u'\xa0', u''))
    df['Visibility'] = df['Visibility'].map(lambda x: x.rstrip(unicode(' km',"utf-8")).replace('-','0.0').replace(u'\xa0', u''))
    #Adjust the first column name to just Time
    df.rename(columns={ df.columns[0]: 'Time' }, inplace=True)
    measure_date = '%s-%s-%s ' % (year, month, day)
    df['Time'] = pd.to_datetime(measure_date + df['Time'])
    df['Airport-code'] = airport_code
    cols = {}
    cols['Temp.'] = 'Temperature'
    cols['Time'] = 'DateTime'
    cols['Dew Point'] = 'Dew-Point'
    cols['Wind Dir'] = 'Wind-Dir'
    cols['Pressure'] = 'Pressure-hPa'
    cols['Visibility'] = 'Visibility-km'
    df.rename(columns=cols, inplace=True)
    return df

def send_to_sql(df):
    TABLENAME = 'weather'
    POOL_SIZE = 50

    ENGINE = sqlalchemy.create_engine(
        configure_engine(), pool_size=POOL_SIZE, max_overflow=0)

    df.to_sql(TABLENAME, ENGINE, if_exists='append', index=False)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def run(start_date, end_date):
    notLoaded = {}
    airport_list = airports.get_airport_list()
    for airport in airport_list:
        notLoaded[airport['sigla']] = 0
    
    for single_date in daterange(start_date, end_date):#The last day is not included, so the daterange is start_date to end_date-1
        year = single_date.year
        month = single_date.month
        day = single_date.day
        print("Reading data for %s-%s-%s"%(year,month,day))
        for airport in airport_list:
            df = generate_weather_information(airport['sigla'],year,month,day)
            if df.empty == True:
                notLoaded[airport['sigla']] = notLoaded[airport['sigla']] + 1
            else:
                send_to_sql(df)
    print(notLoaded)

def test(airport_code,year,month,day):
    df = generate_weather_information(airport_code,year,month,day)
    print(df)

if __name__ == "__main__":
    warnings.simplefilter(action='ignore', category=FutureWarning)
    #test('SBCG',2017,10,2)
    #create_table()
    start_date = date(2018, 1, 1)
    end_date = date(2018, 2, 1) 
    run(start_date, end_date)
