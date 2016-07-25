#This function was originally created to filter a database used
#online that was filtered to only 4 columns

import read
import pandas as pd

from dateutil.parser import parse
import datetime



df = read.load_data()


datetimes = df['submission_time']



def ret_hour(dt):

    ret_dt = parse(dt)

    return ret_dt.hour



df['submission_hours'] = datetimes.apply(ret_hour)



print(df['submission_hours'].value_counts(ascending=False).head(10))