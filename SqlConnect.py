import pandas.io.sql as psql
from sqlalchemy import create_engine


# Skynet production db
# Query the SQL Server database and put the results into a Pandas dataframe. This will
# allow easier manipulation and graphics displays.
def getData():
    ServerName = 'rnop-ctpa02'
    Database = 'FTA'
    Driver = "driver=SQL Server Native Client 11.0"

    engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)
    # sql = "SELECT GameName AS 'Games Tested', " \
    #       "COUNT(GameName) AS 'Games Tested Amount' " \
    #       "FROM GameLogs WHERE GameName <> '' " \
    #       "GROUP BY GameName " \
    #       "ORDER BY '# of Games Tested' " \
    #       "DESC"
    sql = "SELECT COUNT(GameName) AS 'Game Name Count', GameName AS 'Game Name', Denom AS 'Denom', Bet AS 'Bet', AI AS 'AI', Win AS 'Win', G2S as 'G2S', SAS AS 'SAS' " \
          "FROM GameLogs " \
          "WHERE GameName != '' " \
          "GROUP BY Bet, GameName, AI, Denom, Win, G2S, SAS " \
          "ORDER BY GameName " \
          "ASC"

    df = psql.read_sql(sql, engine)

    # test: read one row at a time
    # for ix in df.index:
    #         ser: object = df.loc[ix:ix]
    #         print(ser)

    return df
#
# df2 = getData()
# print(df2[['AI','Game Name']].nunique())
# print(df2.info())
# print(df2.describe())
