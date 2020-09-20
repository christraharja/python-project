import pandas as pd # importing pandas property
import matplotlib.pyplot as plt # importing matplotlib property
# Data source:
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# Practice questions from: w3resource.com/python-exercises/project/covid-19/index.php
dataFile = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv") # read the data using pandas
# Task 1: display the first 5 rows of the data set as well as print the data set information and its missing values.
print(dataFile) # test to print the data set and see if it works
print(dataFile.info()) # print the data set information
print(dataFile.isna().sum()) # print the missing values in data set
# Task 2: get the latest number of confirmed, deaths, recovered and active cases of COVID 19 country wise.
# Since we are trying to calculate the active cases, therefore, we will subtract total confirmed cases with death and recovered.
dataFile["Active"] = dataFile["Confirmed"] - dataFile["Deaths"] - dataFile["Recovered"]
TotalActiveresultpercountry = dataFile.groupby("Country/Region")['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(TotalActiveresultpercountry)
# Task 3: get the latest number of confirmed, deaths, recovered and active cases of COVID 19 province/state wise.
# We will be able to use the same equation listed above and just make a minor modification to the sorting process.
TotalActiveresultperstate = dataFile.groupby(['Country/Region', 'Province/State'])['Confirmed', 'Deaths', 'Recovered'].max()
print(TotalActiveresultperstate)
# Task 4: get the Chinese province wise case of confirmed,deaths and recovered cases of COVID 19.
chineseData = dataFile[dataFile["Country/Region"] == "China"]
chineseData = chineseData[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
finalResult = chineseData.sort_values(by='Confirmed', ascending=False)
finalResult = finalResult.reset_index(drop=True)
print(finalResult)
# Task 5: get the latest country wise death cases of COVID 19.
deathpercountry = dataFile.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
finalresult = deathpercountry[deathpercountry["Deaths"]>0][['Country/Region', 'Deaths']]
print(finalresult)
# Task 6: get the list of country with no cases of COVID 19 recovered.
RecoveredData = dataFile.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
result = dataFile[dataFile["Recovered"]==0][['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
print(result)
# Task 7: get the list of country with all COVID 19 cases died.
alldiedcases = dataFile.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
res = alldiedcases[alldiedcases['Confirmed']==alldiedcases['Deaths']]
res = res[['Country/Region', 'Confirmed', 'Deaths']]
res = res.sort_values('Confirmed', ascending=False)
res = res[res["Confirmed"]>0]
res = res.reset_index(drop = True)
print(res)
# Task 8: get the list of country with all COVID 19 cases recovered.
allreoveredcases = dataFile.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
Res = allreoveredcases[allreoveredcases["Confirmed"]==allreoveredcases["Recovered"]]
Res = Res[['Country/Region', 'Confirmed', 'Recovered']]
Res = Res.sort_values('Confirmed', ascending=False)
Res = Res[Res['Confirmed']>0]
Res = Res.reset_index(drop=True)
print(Res)
# Task 9: Get the top 10 countries data (Last Update, Country/Region, Confirmed, Deaths, Recovered) of COVID 19.
ToptenResult = dataFile.groupby('Country/Region').max().sort_values(by='Confirmed', ascending=False)[:10]
print(ToptenResult)
# Task 10: create a plot of total deaths, confirmed, recovered and active cases Country wise where deaths greater than 150 cases.
plot_data = dataFile.groupby(["Country/Region"])["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
plot_data = plot_data.sort_values(by='Deaths', ascending=False)
plot_data = plot_data[plot_data['Deaths']>50]
plt.figure(figsize=(15,5))
plt.plot(plot_data['Country/Region'], plot_data['Deaths'], color='red')
plt.plot(plot_data['Country/Region'], plot_data['Confirmed'], color='green')
plt.plot(plot_data['Country/Region'], plot_data['Recovered'], color='blue')
plt.plot(plot_data['Country/Region'], plot_data['Active'], color='black')
plt.title('Total Deaths(>150), Confirmed, Recovered and Active Cases by Country')
plt.show()
# Task 11: visualize the state/province wise death cases of COVID 19 in USA.
USA_data = dataFile[dataFile["Country/Region"]=="US"].drop(['Country/Region','Latitude', 'Longitude'], axis=1)
USA_data = USA_data[USA_data.sum(axis = 1) > 0]
USA_data = USA_data.groupby(['Province/State'])['Deaths'].sum().reset_index()
USA_data_death = USA_data[USA_data['Deaths'] > 0]
state_fig = px.bar(USA_data_death, x='Province/State', y='Deaths', title='State wise deaths reported of COVID-19 in USA', text='Deaths')
state_fig.show()
# Task 12: visualize the state/province wise Active cases of COVID 19 in USA.
usa_data = dataFile[dataFile["Country/Region"]=="US"].drop(['Country/Region','Latitude', 'Longitude'], axis=1)
usa_data = usa_data[usa_data.sum(axis=1) > 0]
usa_data = usa_data.groupby(['Province/State'])['Active'].sum().reset_index()
usa_data_death = usa_data[usa_data['Active'] > 0]
state_fig = px.bar(usa_data_death, x='Province/State', y='Active', title='State wise recovery cases of COVID-19 in USA',text='Active')
state_fig.show()
# Task 13:
CombinedData = dataFile[dataFile["Country/Region"]=='US'].drop(['Country/Region','Latitude', 'Longitude'], axis=1)
CombinedData = CombinedData[CombinedData.sum(axis = 1) > 0]
CombinedData = CombinedData.groupby(['Province/State'])['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
CombinedData = pd.melt(CombinedData, id_vars='Province/State', value_vars=['Confirmed', 'Deaths', 'Recovered', 'Active'], value_name='Count', var_name='Case')
fig = px.bar(CombinedData, x='Province/State', y='Count', text='Count', barmode='group', color='Case', title='USA State wise combine number of confirmed, deaths, recovered, active COVID-19 cases')
fig.show()
# Task 14: visualize Worldwide Confirmed COVID 19 cases over time.
Worldwide_data = dataFile.groupby('Last Update')['Last Update', 'Confirmed', 'Deaths'].sum().reset_index()
fig = px.line(worldwide_data, x="Last Update", y="Confirmed",title="Worldwide Confirmed Novel Coronavirus(COVID-19) Cases Over Time")
fig.show()

























