# -*- coding: utf-8 -*-
import sqlite3
import requests
import datetime


def eva_score(list):
    
    #抽出した平均を評価
    if 0<=list1[0] and list1[0]<=0.016:
        evalution="S"

    elif 0.017<=list1[0] and list1[0]<=0.099:
        evalution="A"

    elif 0.1<=list1[0] and list1[0]<=0.999:
        evalution="B"

    elif 1.0<=list1[0] and list1[0]<=9.999:
        evalution="C"

    elif 10.0<=list1[0]:
        evalution="D"
    return evalution

print("=====================")
print("                    ")
print("  計測・評価を開始")
print("                    ")
print("=====================")

#--------------------------
#     
#       192.168.1.81
#
#--------------------------

#応答速度計測
url = 'http://192.168.1.81'
res = requests.get(url)
time_elapsed = res.elapsed.total_seconds()

#現在時刻取得
dt_now = datetime.datetime.now()


#データベースＳＱＬＩＴＥに接続
dbname = 'response'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()


#応答速度テーブルへ計測結果を挿入
setdb1 = (None, time_elapsed,dt_now)
cur.execute("insert into response81 (id,speed,datetime) values (?,?,?)", setdb1)



#抽出した現在応答速度を評価
if 0<=time_elapsed and time_elapsed<=0.016:
    evaluation_now="S"

elif 0.017<=time_elapsed and time_elapsed<=0.099:
    evaluation_now="A"

elif 0.1<=time_elapsed and time_elapsed<=0.999:
    evaluation_now="B"

elif 1.0<=time_elapsed and time_elapsed<=9.999:
    evaluation_now="C"

elif 10.0<=time_elapsed:
    evaluation_now="D"



#応答速度テーブルから過去24時間の平均を取り出す
cur.execute("select avg(speed) from response81 where datetime > datetime(datetime(), '-1 days', '+0 hours');")
list1 = cur.fetchone()

evaluation_ave=eva_score(list1)


print("----192.168.1.81----")
print("now_speed:",time_elapsed)
print("now_eva:",evaluation_now)
print("ave_speed:",list1)
print("sve_eva:",evaluation_ave)



#評価テーブルへ挿入
#ID　現在の速度　現在の評価　平均の速度　平均の評価　日時
setdb2 = (None,time_elapsed,evaluation_now,list1[0],evaluation_ave,dt_now)
cur.execute("insert into monitoring81 (id,now_speed,now_speed_score,ave_speed,ave_speed_score,datetime) values (?,?,?,?,?,?)", setdb2)

#--------------------------
#     
#       192.168.1.82
#
#--------------------------


#応答速度計測
url = 'http://192.168.1.82'
res = requests.get(url)
time_elapsed = res.elapsed.total_seconds()

#現在時刻取得
dt_now = datetime.datetime.now()


#応答速度テーブルへ計測結果を挿入
setdb1 = (None,time_elapsed,dt_now)
cur.execute("insert into response82 (id,speed,datetime) values (?,?,?)", setdb1)



#抽出した現在応答速度を評価
if 0<=time_elapsed and time_elapsed<=0.016:
    evaluation_now="S"

elif 0.017<=time_elapsed and time_elapsed<=0.099:
    evaluation_now="A"

elif 0.1<=time_elapsed and time_elapsed<=0.999:
    evaluation_now="B"

elif 1.0<=time_elapsed and time_elapsed<=9.999:
    evaluation_now="C"

elif 10.0<=time_elapsed:
    evaluation_now="D"



#応答速度テーブルから過去24時間の平均を取り出す
cur.execute("select avg(speed) from response82 where datetime > datetime(datetime(), '-1 days', '+0 hours');")
list1 = cur.fetchone()

evaluation_ave=eva_score(list1)


print("----192.168.1.82----")
print("now_speed:",time_elapsed)
print("now_eva:",evaluation_now)
print("ave_speed:",list1)
print("sve_eva:",evaluation_ave)

#評価テーブルへ挿入
#ID　現在の速度　現在の評価　平均の速度　平均の評価　日時
setdb2 = (None,time_elapsed,evaluation_now,list1[0],evaluation_ave,dt_now)
cur.execute("insert into monitoring82 (id,now_speed,now_speed_score,ave_speed,ave_speed_score,datetime) values (?,?,?,?,?,?)", setdb2)


#--------------------------
#     
#       192.168.1.83
#
#--------------------------


#応答速度計測
url = 'http://192.168.1.83'
res = requests.get(url)
time_elapsed = res.elapsed.total_seconds()

#現在時刻取得
dt_now = datetime.datetime.now()


#応答速度テーブルへ計測結果を挿入
setdb1 = (None,time_elapsed,dt_now)
cur.execute("insert into response83 (id,speed,datetime) values (?,?,?)", setdb1)



#抽出した現在応答速度を評価
if 0<=time_elapsed and time_elapsed<=0.016:
    evaluation_now="S"

elif 0.017<=time_elapsed and time_elapsed<=0.099:
    evaluation_now="A"

elif 0.1<=time_elapsed and time_elapsed<=0.999:
    evaluation_now="B"

elif 1.0<=time_elapsed and time_elapsed<=9.999:
    evaluation_now="C"

elif 10.0<=time_elapsed:
    evaluation_now="D"



#応答速度テーブルから過去24時間の平均を取り出す
cur.execute("select avg(speed) from response83 where datetime > datetime(datetime(), '-1 days', '+0 hours');")
list1 = cur.fetchone()

evaluation_ave=eva_score(list1)


print("----192.168.1.83----")
print("now_speed:",time_elapsed)
print("now_eva:",evaluation_now)
print("ave_speed:",list1)
print("sve_eva:",evaluation_ave)


#評価テーブルへ挿入
#ID　現在の速度　現在の評価　平均の速度　平均の評価　日時
setdb2 = (None,time_elapsed,evaluation_now,list1[0],evaluation_ave,dt_now)
cur.execute("insert into monitoring83 (id,now_speed,now_speed_score,ave_speed,ave_speed_score,datetime) values (?,?,?,?,?,?)", setdb2)


# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()

print("上記結果をデータベースへ保存しました。")
