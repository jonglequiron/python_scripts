###
#V1.0 Data transfer Cebu Pacific June 14, 2018
###
import pandas as pd
import glob
import dateutil.parser as parser

#Insert path and csv file
path = "D:/Work2016/WeatherPhilippines/commercial_unit/cebu_pacific/"
path_2 = "D:/Work2016/WeatherPhilippines/commercial_unit/meralco/data/"
csv = "cebu_pacific_stations.csv"

#Insert date format
fmt = "%Y%m%d%H%M"

#Read csv file
csv = pd.read_csv(path+csv)
#Generate the list of csv in path_2
csv_list = glob.glob(path_2+"*.csv")

#Get only the latest run in path_2
data = pd.read_csv(csv_list[-1])

#Get the observation data
obs_date = (parser.parse((csv_list[-1].split("\\")[-1]).split(".csv")[0])).strftime(fmt)

#Filter only the Cebu Pacific Data
data_1 = (pd.merge(csv,data,on = "station_id")).sort_values("station_id", ascending = True)

#Get only the desired parameters
columns = ["station_id","sta_code","lat","lon","RR10m","RH","TL","TD","DIR","FF","G10","GL10","MSLP"]
data_2 = data_1[columns]

#Rename the parameters with units
columns_1 = ["station_id","sta_code","lat","lon","rain_in_mm","relative_humidity_in_percent","temperature_in_degC", 
             "dewpoint_temperature_in_degC","wind_direction_in_deg","wind_speed_in_knots","wind_gust_in_knots",
             "solar_radiation_in_kj_sm","mean_sea_level_pressure_in_hpa"]
data_2.columns = columns_1

#Save as csv 
data_2.to_csv(path+"cebu_pacific_"+obs_date+".csv", header = True, index = None)
print "I am done!"
