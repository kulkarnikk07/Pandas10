# Pandas10

# 1 Problem 1 : Group Sold Products by the Date	(https://leetcode.com/problems/group-sold-products-by-the-date/)

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups = activities.groupby(['sell_date'])
    result = groups.agg(
        num_sold = ('product', 'nunique'),
        products = ('product', lambda x:','.join(sorted(set(x))))
    ).reset_index()
    result.sort_values(by =['sell_date'], inplace = True)
    return result

# 2 Problem 2 : Daily Leads and Partners	(	https://leetcode.com/problems/daily-leads-and-partners/ )

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df = daily_sales.groupby(['date_id','make_name']).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id','nunique')
    ).reset_index()
    return df

# 3 Problem 3 : Actors and Directors who Cooperated At Least Three Times	(https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id']).size().reset_index(name = 'cnt')
    df = df[df['cnt']>=3]
    return df[['actor_id','director_id']]