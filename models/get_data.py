import pandas as pd
import psycopg2


def get_conexion_db():
    conexion = psycopg2.connect(
        host="mikldb.c4q77ebplhtf.us-east-2.rds.amazonaws.com", 
        database="postgres", 
        user="postgres", 
        password="*Mexico2022*"
    )
    return conexion

def get_cursor(conexion):
    return conexion.cursor()

def get_lactation_summary(cursor, string_ids):
    cursor.execute(f"""select * from milk_lactation_summary where id_cow in ({string_ids});""")
    alive_cows_raw = cursor.fetchall()
    alive_cows_raw = pd.DataFrame(alive_cows_raw, columns=['id_cow', 'lactation', 'days_milk', 'daily_production', 'id_lac'])
    alive_cows_raw = alive_cows_raw[['id_cow', 'lactation', 'days_milk', 'daily_production']]
    return alive_cows_raw

def get_total_production(df, list_of_single_column):
    for i in range(1,10):
        df['total_production_' + str(i)] = 0
    for id in list_of_single_column:
        filter_df = df.query(f'id_cow == {id}')
        if filter_df.lactation.unique().any():
            for lact in list(filter_df.lactation.unique()):
                index_ = df.query(f'id_cow == {id}').index[0]
                index_t = df.query(f'id_cow == {id}').index[lact - 1]
                df.iloc[index_]['total_production_' + str(lact)] = df.iloc[index_t]['daily_production']

def get_days_milk(df, list_of_single_column):
    for i in range(1,10):
        df['days_milk' + str(i)] = 0
    for id in list_of_single_column:
        filter_df = df.query(f'id_cow == {id}')
        if filter_df.lactation.unique().any():
            for lact in list(filter_df.lactation.unique()):
                index_ = df.query(f'id_cow == {id}').index[0]
                index_t = df.query(f'id_cow == {id}').index[lact - 1]
                df.iloc[index_]['days_milk' + str(lact)] = df.iloc[index_t]['days_milk']

def get_lactation(df, list_of_single_column):
    for i in range(1,10):
        df['lactation_' + str(i)] = 0
    for id in list_of_single_column:
        filter_df = df.query(f'id_cow == {id}')
        if filter_df.lactation.unique().any():
            for lact in list(filter_df.lactation.unique()):
                index_ = df.query(f'id_cow == {id}').index[0]
                df.iloc[index_]['lactation_' + str(lact)] = 1

def get_aborts(group_df, cur, string_ids):
    group_df = group_df.drop(['lactation', 'daily_production', 'days_milk'], axis=1)
    cur.execute(f"""select * from milk_abortion_details where id_cow in ({string_ids});""")
    abort_cows = cur.fetchall()
    abort_cows = pd.DataFrame(abort_cows, columns=['id_cow', 'date', 'ab_1', 'ab_2', 'ab_3', 'ab_4', 'ab_5', 'ab_6', 'ab_7', 'ab_8', 'ab_9'])
    return abort_cows[['id_cow', 'ab_1', 'ab_2', 'ab_3', 'ab_4', 'ab_5', 'ab_6', 'ab_7', 'ab_8', 'ab_9']]

def get_inse(cur, string_ids):
    cur.execute(f"""select * from milk_insemination_details where id_cow in ({string_ids});""")
    inse_cows = cur.fetchall()
    inse_cows = pd.DataFrame(inse_cows, columns=['id_cow', 'date', 'inse_1', 'inse_2', 'inse_3', 'inse_4', 'inse_5', 'inse_6', 'inse_7', 'inse_8', 'inse_9'])
    return inse_cows[['id_cow','inse_1', 'inse_2', 'inse_3', 'inse_4', 'inse_5', 'inse_6', 'inse_7', 'inse_8', 'inse_9']]

def get_mas(cur, string_ids):
    cur.execute(f"""select * from milk_mastitis_details where id_cow in ({string_ids});""")
    mast_cows = cur.fetchall()
    mast_cows = pd.DataFrame(mast_cows, columns=['id_cow','date','mast_1', 'mast_2', 'mast_3', 'mast_4', 'mast_5', 'mast_6', 'mast_7', 'mast_8', 'mast_9'])
    return mast_cows[['id_cow','mast_1', 'mast_2', 'mast_3', 'mast_4', 'mast_5', 'mast_6', 'mast_7', 'mast_8', 'mast_9']]

def get_target_columns(total_dt):
    total_dt.fillna(0)
    total_dt['production_ok'] = 0
    total_dt.loc[total_dt['total_production_3'] > 10000, 'production_ok'] = 1
    # obtener solo las vacas que tienen dos lactancias
    total_dt = total_dt.query('lactation_2 != 0')
    return total_dt

def get_data():
    conexion = get_conexion_db()
    cur = conexion.cursor(conexion)
    
    alive_cows = pd.read_csv('../Resources/alive_cows_to_predict.csv')
    ids_cows = alive_cows[['id']]
    list_of_single_column = ids_cows['id'].tolist()
    string_ids = ids_cows['id'].astype(str).tolist()
    string_ids = ','.join(string_ids)

    df = get_lactation_summary(cur, string_ids)
    get_total_production(df, list_of_single_column)
    get_days_milk()
    get_lactation()

    group = df.groupby('id_cow').first()
    group_df = group.reset_index()


    abort_cows = get_aborts(group_df, cur, string_ids)
    inse_cows = get_inse(cur, string_ids)
    mast_cows = get_mas(cur)
    
    total_dt = pd.merge(group_df, abort_cows, how='left', on='id_cow').fillna(False, downcast='infer')
    total_dt = pd.merge(total_dt, inse_cows, how='left', on='id_cow').fillna(False, downcast='infer')
    total_dt = pd.merge(total_dt, mast_cows, how='left', on='id_cow').fillna(False, downcast='infer')

    total_dt = get_target_columns(total_dt)
    return total_dt