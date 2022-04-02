#importing the required libraries 
import pandas as pd
import bar_chart_race as bcr

#loading the dataset
data = pd.read_csv(r"..............\WHO-COVID-19-global-data.csv", encoding="latin")           # insert the path
print(data.head(5))
#print(data.columns)
#print(data.describe)
#selecting specific columns and creating a new dataframe
df=pd.DataFrame(data,columns=["Date_reported","Country","Cumulative_cases"])
print(df)
Date_reported = df["Date_reported"].unique()
Country_name = df["Country"].unique()
print(Date_reported,Country_name)

data_dict = dict()
            
for i in Country_name:
    n = df["Cumulative_cases"][ df.Country == i]                                                # n is a list here
    data_dict[i]= n.tolist()                                                                    # list to dictionary conversion

#converting the "data_dict" dictionary into a dataset
df_final= pd.DataFrame(data_dict)
print(df_final.tail(5))

#insert new column "Date" on 0th position in the dataset
df_final.insert(0,"Date",Date_reported,True)
print(df_final.tail(5))
#saving the dataset to the specific location
#t.to_csv(r"...........................\covid cases.csv",index = False)                         # insert the path

#setting "Date" as an index
df_final.set_index("Date",inplace=True)
#sorted dataframe
df_sorted = df_final.sort_values(by= '16-03-2022',axis=1,ascending= False)                      # insert the last date till which you have the dataset &insert the path
#saving the dataset to the specific location
df_sorted.to_csv(r".........................................\total cases.csv", index = True)

# lets have some animation now , save the output in "filename"
bcr.bar_chart_race(df=df_sorted,
                   filename = r"..................\video01.mp4",                                # insert the path
                   figsize=(9,4),
                   period_length=800,     
                   n_bars=12,
                   bar_size=.80,
                   dpi=144,
                   steps_per_period=50,
                   filter_column_colors=True,
                   period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center','size':16},
                   period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total cases: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 10, 'family': 'Courier New','color': 'red'},
                   title="Covid-19 cases around the World")


