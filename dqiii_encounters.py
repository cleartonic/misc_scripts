# -*- coding: utf-8 -*-
"""
@author: cleartonic
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
from IPython.display import Image, Markdown, display
pd.options.display.max_rows = 999
pd.options.display.max_columns= 999
pd.options.mode.chained_assignment = None

df_master = pd.read_csv('data/dq3-encounter_analytic.csv', dtype={"index": int, "Map Type": str, "Area Code": int, "Zone": str, "Time": str, "Formation": str, "Formation_j": str})
df_walks = pd.read_csv('enka_level/dq3_encounter_walks_master.csv')





## TEMP FOR TESTING OVERWORLD
df = df_master.copy()
#df = df_master.loc[(df_master['Map Type'] == "Dungeon") & (df_master['Zone'] == "Garuna Tower F3")]
##

#
# Fix for weird stoneman/goopi 
#
df.loc[367287] = df.loc[368788]
#



df['Zone'].loc[(df['Zone'] == "To Melkido")] = 'To Domdora'

#maptypes_list = df['Map Type'].unique().tolist()
maptypes_list = ['Overworld','Dungeon','Sea']

daynightlist = ['Samanosa (2)','Baharata (3)','Silver Orb Shrine','Kazave','Lamia Shrine','Samanosa (1)','Romaly','Samanosa (4)','Desert','Dhama (1)','Reeve','To Kandar 2','Edinbear','Isis','Tedanki','Baharata (1)','Dhama (2)','Merchant Town','Aliahan','Necrogond','Portoga','Baharata (2)','Ultimate Key Tile','To Samanosa Shrine','To Magic Ball','Samanosa (3)','To Assalam']
zone_hex_dict =  {'Aliahan': '0x04', 'Reeve': '0x06', 'To Magic Ball': '0x07', 'Romaly': '0x08', 'Kazave': '0x09', 'Portoga': '0x0F', 'To Assalam': '0x0C', 'Desert': '0x0D', 'Isis': '0x0E', 'Baharata (1)': '0x10', 'Baharata (2)': '0x11', 'Baharata (3)': '0x12', 'To Kandar 2': '0x13', 'Dhama (1)': '0x15', 'Dhama (2)': '0x16', 'Samanosa (1)': '0x27', 'Samanosa (2)': '0x2A', 'Samanosa (3)': '0x27', 'Samanosa (4)': '0x2B', 'Edinbear': '0x1F', 'Tedanki': '0x1B', 'Necrogond': '0x30', 'Silver Orb Shrine': '0x31', 'Merchant Town': '0x20', 'Lamia Shrine': '0x1E', 'To Ludatorm': '0x10', 'To Mountain Cave': '0x11', 'To Domdora': '0x12', 'Outside Garin Tomb': '0x8', 'To Kol (1)': '0x18', 'To Kol (2)': '0x24', 'Southwest Domdora': '0x30', 'Outside RainStaff Shrine': '0x6', 'Eastern Darkworld Continent': '0x1C', 'To Zoma (1)': '0x20', 'To Zoma (2)': '0x17', 'To Zoma (3)': '0x16', 'To Zoma (4)': '0x15', 'To Zoma (5)': '0x14', 'Ultimate Key Tile': '0x23', 'To Samanosa Shrine': '0x24', 'To Sioux (1)':'0x00', 'To Sioux (2)':'0x00', 'To Necrogond':'0x02','To Lamia Shrine':'0x03','Dark World (1)':'0x00','Dark World (2)':'0x00'}
metals_list = ["Garuna Tower F3", "Garuna Tower F4", "Garuna Tower F5", "Gaia's Navel B1", "Gaia's Navel F1", "Gaia’s Navel B1", "Zipangu Cave F1", "Baharata (1)", "Dhama (1)", "Samanosa (2)", "Necrogond F1", "Necrogond B1", "Necrogond B2", "Baramos Castle Outer", "Baramos Castle F1", "Baramos Castle B1", "Rubiss Tower F1", "Rubiss Tower F2", "Rubiss Tower F6", "Zoma’s Castle F1", "To Zoma (1)", "To Zoma (2)", "To Zoma (3)", "To Zoma (5)","Ultimate Key Tile" ,"To Samanosa Shrine"]


def fetch_img(maptype, areacode):
    try:
        return Image(filename='images/'+maptype.lower()+'/'+str(areacode)+'.png')
    except:
        return Image(filename='images/jester-m.png')
        
#plot.set_xticklabels(plot.get_xticklabels(), rotation=-45, ha='left')
def plot_thresholds(df_walks):
    sns.set(style = 'whitegrid')
    fig, ax = plt.subplots(ncols=1)
    fig.set_size_inches(16, 6)
    fig.suptitle("Encounter threshold range (full data)")
    sns.countplot(x = "count", data = df_walks, palette="Blues")
    plt.show()
    
def plot_thresholds_2(df_walks):
    fig, ax = plt.subplots(ncols=1)
    fig.set_size_inches(16, 6)
    fig.suptitle("Encounter threshold range (full data, area detail)")
    sns.countplot(x = 'count', hue = 'area',data = df_walks, palette="Greens")
    plt.show()    
def plot_two(df_day, df_night, maptype, zone, language):
    sns.set_style('ticks')
    sns.set_context(font_scale=1.4)
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    fig.set_size_inches(16, 6)
    if language == 'en':
        mpl.rcParams['font.sans-serif'] = ['Roboto']
        mpl.rcParams['font.serif'] = ['Roboto']
        sns.set(style = 'whitegrid')
        sns.set_style("whitegrid",{"font.sans-serif":['Roboto', 'Arial']})
        sns.barplot(x=df_day['Formation'],y=df_day['%'],ax=ax1, palette="Blues_r").set_title('Day')
        sns.barplot(x=df_night['Formation'],y=df_night['%'],ax=ax2, palette="Greens_r").set_title('Night')
    elif language == 'jp':
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['font.serif'] = ['SimHei']
        sns.set(style = 'whitegrid')
        sns.set_style("whitegrid",{"font.sans-serif":['simhei', 'Arial']})
        sns.barplot(x=df_day['Formation_j'],y=df_day['%'],ax=ax1, palette="Blues_r").set_title('日')
        sns.barplot(x=df_night['Formation_j'],y=df_night['%'],ax=ax2, palette="Greens_r").set_title('夜')
    else:
        print("Language error - check argument.")
    for ax in fig.axes:
        mpl.pyplot.sca(ax)
        plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(top=.8)
    #fig.suptitle(maptype+" - "+zone)
    plt.show()
    
def plot_one(df_query, maptype, zone, language):
    sns.set_style('ticks')
    sns.set_context(font_scale=1.4)
    fig, ax = plt.subplots(ncols=1)
    fig.set_size_inches(16, 6)
    if language == 'en':
        mpl.rcParams['font.sans-serif'] = ['Roboto']
        mpl.rcParams['font.serif'] = ['Roboto']
        sns.set(style = 'whitegrid')
        sns.set_style("whitegrid",{"font.sans-serif":['Roboto', 'Arial']})
        sns.barplot(x=df_query['Formation'],y=df_query['%'], palette="Blues_r")
    elif language == 'jp':
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['font.serif'] = ['SimHei']
        sns.set(style = 'whitegrid')
        sns.set_style("whitegrid",{"font.sans-serif":['simhei', 'Arial']})
        sns.barplot(x=df_query['Formation_j'],y=df_query['%'], palette="Blues_r")
    else:
        print("Language error - check argument.")
    for ax in fig.axes:
        mpl.pyplot.sca(ax)
        plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(top=.8)
    #fig.suptitle(maptype+" - "+zone)
    plt.show()
    
def return_daynight(df_first, maptype, zone):
    df_list = []
    for daynight in ['Day','Night']:
        df_temp = df_first.loc[(df['Map Type'] == maptype) & (df_first['Zone'] == zone) & (df_first['Time'] == daynight)]
        df_query = pd.DataFrame(df_temp['Formation'].value_counts())
        df_query_j = pd.DataFrame(df_temp['Formation_j'].value_counts())
        df_query = df_query.reset_index()
        df_query_j = df_query_j.reset_index()
        df_query_both = pd.concat([df_query, df_query_j], axis=1)
        df_query_both.columns = ['Formation', 'Count', 'Formation_j', 'Count 2']
        df_query_both = df_query_both[['Formation','Formation_j','Count']]
        df_query_both['%'] = df_query_both['Count']/(df_query_both['Count'].sum() / 100)
        df_query_both = df_query_both[0:10]
        df_list.append(df_query_both)
    return df_list
  
def return_df(df_temp, maptype, zone):
    df_temp = df_temp.loc[(df_temp['Map Type'] == maptype) & (df_temp['Zone'] == zone)]
    df_query = pd.DataFrame(df_temp['Formation'].value_counts())
    df_query_j = pd.DataFrame(df_temp['Formation_j'].value_counts())
    df_query = df_query.reset_index()
    df_query_j = df_query_j.reset_index()
    df_query_both = pd.concat([df_query, df_query_j], axis=1)
    df_query_both.columns = ['Formation', 'Count', 'Formation_j', 'Count 2']
    df_query_both = df_query_both[['Formation','Formation_j','Count']]
    df_query_both['%'] = df_query_both['Count']/(df_query_both['Count'].sum() / 100)
    df_query_both = df_query_both[0:10]
    return df_query_both

def call_fullchart_dn(df2, zone, maptype, language):
    df_day = df2.loc[(df2['Map Type'] == maptype) & (df2['Zone'] == zone) & (df2['Time'] == 'Day')]
    df_night = df2.loc[(df2['Map Type'] == maptype) & (df2['Zone'] == zone) & (df2['Time'] == 'Night')]
    if language == 'en':
        print("Day:")
        df_day2 = pd.DataFrame(df_day['Formation'].value_counts())
        df_day2['%'] = df_day2['Formation']/(df_day2['Formation'].sum() / 100)
        print(df_day2)
        print("-----")
        print("Night:")
        df_night2 = pd.DataFrame(df_night['Formation'].value_counts())
        df_night2['%'] = df_night2['Formation']/(df_night2['Formation'].sum() / 100)
        print(df_night2)

    elif language == 'jp':
        print("日:")
        df_day2 = pd.DataFrame(df_day['Formation_j'].value_counts())
        df_day2['%'] = df_day2['Formation_j']/(df_day2['Formation_j'].sum() / 100)
        print(df_day2)
        print("-----")
        print("夜:")
        df_night2 = pd.DataFrame(df_night['Formation_j'].value_counts())
        df_night2['%'] = df_night2['Formation_j']/(df_night2['Formation_j'].sum() / 100)
        print(df_night2)
    else:
        print("Language error - check argument.")
            
def call_fullchart(df_temp, language):
        if language == 'en':
            df_temp2 = pd.DataFrame(df_temp['Formation'].value_counts())
            df_temp2['%'] = df_temp2['Formation']/(df_temp2['Formation'].sum() / 100)
            print(df_temp2)
        elif language == 'jp':
            df_temp2 = pd.DataFrame(df_temp['Formation_j'].value_counts())
            df_temp2['%'] = df_temp2['Formation_j']/(df_temp2['Formation_j'].sum() / 100)
            print(df_temp2)
        else:
            print("Language error - check argument.")
            
def call_areas(df):
    display(Markdown(("""### All Areas""")))
    for i in maptypes_list:
        for i2 in df.loc[(df['Map Type'] == i)]['Zone'].unique().tolist():
            print(i+" : "+i2)
            
def call_all_plots(df, maptypes_list, language):
    for maptype in maptypes_list:
        display(Markdown(('**Map Type: '+maptype+'**')))

        df1 = df.loc[(df['Map Type'] == maptype)]

        zones_list = df1['Zone'].unique().tolist()
        areacode_list = df1['Area Code'].unique().tolist()
        zonedict = dict(zip(areacode_list,zones_list))
        for areacode in sorted(areacode_list):
            zone = zonedict[areacode]
            df2 = df1.loc[(df1['Map Type'] == maptype) & (df1['Zone'] == zone)]
            print('-----')
            display(Markdown(('**'+zone+'**')))
            if (maptype == 'Overworld' or maptype == 'Sea'):
                display(Markdown(("**Overworld zone hex: "+zone_hex_dict[zone]+"**")))
            print('-----')
            display(fetch_img(maptype,areacode))
            if zone in daynightlist:
                if zone in metals_list:
                    df3 = df2.loc[(df2['Map Type'] == maptype) & (df2['Zone'] == zone) & (df2['Time'] == "Day")]
                    y = df3[df3['Formation'].str.contains("Metaly|Metabble")==True]
                    display(Markdown(('**Day chance to see metal: '+str((len(y)/100)))+'%**'))
                    df3 = df2.loc[(df2['Map Type'] == maptype) & (df2['Zone'] == zone) & (df2['Time'] == "Night")]
                    y = df3[df3['Formation'].str.contains("Metaly|Metabble")==True]
                    display(Markdown(('**Night chance to see metal: '+str((len(y)/100)))+'%**'))
                df_day, df_night = return_daynight(df2,maptype,zone)
                plot_two(df_day,df_night,maptype,zone, language)
                call_fullchart_dn(df2,zone,maptype,language)
            else:
                if zone in metals_list:
                    y = df2[df2['Formation'].str.contains("Metaly|Metabble")==True]
                    display(Markdown(('**Chance to see metal: '+str((len(y)/100)))+'%**'))
                df_query = return_df(df2, maptype,zone)
                plot_one(df_query, maptype, zone, language)
                call_fullchart(df2,language)
            print()
#            except:
#                print("Error on "+maptype+" : "+zone+"!")

