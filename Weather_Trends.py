import pandas as pd
import matplotlib.pyplot as plt
import os
# Set working directory
os.chdir('/Users/dayanesallet/Documents/_Educação/Data Analyst Nanodegree/Weather Project/Data')

# Import data
PortoAlegre_temp = pd.read_csv('./PortoAlegre_Temperature_Data.csv')
World_temp = pd.read_csv('./World_Temperature_Data.csv')
Perth_temp = pd.read_csv('./Perth_Temperature_Data.csv')
NY_temp = pd.read_csv('./NovaYORK_Temperature_Data.csv')
Paris_temp = pd.read_csv('./Paris_Temperature_Data.csv')

# Compute moving avarage
PortoAlegre_temp_ma = PortoAlegre_temp['avg_temp'].rolling(window=7).mean()
World_temp_ma = World_temp['avg_temp'].rolling(window=7).mean()
Perth_temp_ma = Perth_temp['avg_temp'].rolling(window=7).mean()
NY_temp_ma = NY_temp['avg_temp'].rolling(window=7).mean()
Paris_temp_ma = Paris_temp['avg_temp'].rolling(window=7).mean()

# Insert new column in the dataframe with the computed moving avareges
PortoAlegre_temp.insert(4,'7-year Moving Avarage', PortoAlegre_temp_ma)
World_temp.insert(2,'7-year Moving Avarage', World_temp_ma)
Perth_temp.insert(2,'7-year Moving Avarage', Perth_temp_ma)
NY_temp.insert(2,'7-year Moving Avarage', NY_temp_ma)
Paris_temp.insert(2,'7-year Moving Avarage', Paris_temp_ma)

# Verify NaN values
PortoAlegre_temp['7-year Moving Avarage'].isnull().any()
PortoAlegre_temp['7-year Moving Avarage'].isnull().sum()
World_temp['7-year Moving Avarage'].isnull().any()
World_temp['7-year Moving Avarage'].isnull().sum()

# Plot the data
# Moving Avarage Comparisson
plt.plot(World_temp['year'],World_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'World')
plt.plot(PortoAlegre_temp['year'],PortoAlegre_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'Porto Alegre')
plt.xlabel('Year')
plt.ylabel('Moving Avarege Temperature (ºC) \n 7-year window')
plt.title("Comparison of Porto Alegre and the world's \n temperature (ºC) over the years", fontweight = 'bold')
plt.axis([1838,2013,7,19.5])
plt.legend()
plt.grid(True)
plt.savefig('Moving Avarage Comparisson',dpi = 300,bbox_inches='tight')
plt.show()

# Porto Alegre mean temperature variation
plt.plot(PortoAlegre_temp['year'],PortoAlegre_temp['avg_temp'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.xlabel('Year')
plt.ylabel('Mean Temperature (ºC)')
plt.title("Mean temperature (ºC) variation in\n Porto Alegre  over the years", fontweight = 'bold')
plt.axis([1832,2013,16.5,20])
plt.grid(True)
plt.savefig('Porto Alegre mean temperature variation',dpi = 300,bbox_inches='tight')
plt.show()

# Porto Alegre moving avarage temperature variation
plt.plot(PortoAlegre_temp['year'],PortoAlegre_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.xlabel('Year')
plt.ylabel('Moving Avarege Temperature (ºC) \n 7-year window')
plt.title("Moving avarage temperature (ºC) variation in\n Porto Alegre over the years", fontweight = 'bold')
plt.axis([1832,2013,16.5,20])
plt.grid(True)
plt.savefig('Porto Alegre moving avarage temperature variation',dpi = 300,bbox_inches='tight')
plt.show()

# World mean temperature variation
plt.plot(World_temp['year'],World_temp['avg_temp'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.xlabel('Year')
plt.ylabel('Mean Temperature (ºC)')
plt.title("Mean temperature (ºC) variation in\n the world over the years", fontweight = 'bold')
plt.axis([1750,2013,5.5,10])
plt.grid(True)
plt.savefig('World mean temperature variation',dpi = 300,bbox_inches='tight')
plt.show()


# World moving avarage temperature variation
plt.plot(World_temp['year'],World_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.xlabel('Year')
plt.ylabel('Moving Avarege Temperature (ºC) \n 7-year window')
plt.title("Moving avarage temperature (ºC) variation in\n the world over the years", fontweight = 'bold')
plt.axis([1750,2013,6.5,10])
plt.grid(True)
plt.savefig('World moving avarage temperature variation',dpi = 300,bbox_inches='tight')
plt.show()


# Subplot
plt.figure(figsize=(6, 4))
plt.subplot(2, 1, 1)
plt.plot(PortoAlegre_temp['year'],PortoAlegre_temp['avg_temp'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.title("Porto Alegre mean temperature variation", fontweight = 'bold')
plt.xlabel('Year')
plt.ylabel('Avarege \n Temperature (ºC)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(World_temp['year'],World_temp['avg_temp'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.title("World mean temperature variation", fontweight = 'bold')
plt.xlabel('Year')
plt.ylabel('Avarege \n Temperature (ºC)')
plt.grid(True)

plt.tight_layout()
plt.savefig('Mean_Temp_POA_W',dpi = 300,bbox_inches='tight')
plt.show()



plt.figure(figsize=(6, 4))
plt.subplot(2, 1, 1)
plt.plot(PortoAlegre_temp['year'],PortoAlegre_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.title("Porto Alegre moving average temperature variation", fontweight = 'bold')
plt.xlabel('Year')
plt.ylabel('Moving Avarege \n Temperature (ºC)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(World_temp['year'],World_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1)
plt.title("World moving average temperature variation", fontweight = 'bold')
plt.xlabel('Year')
plt.ylabel('Moving Avarege \n Temperature (ºC)')
plt.grid(True)

plt.tight_layout()
plt.savefig('Moving_Temp_POA_W',dpi = 300,bbox_inches='tight')
plt.show()



# Additional computations for comparisson
#
avg_temp_POA = PortoAlegre_temp['avg_temp'].mean()
avg_temp_World = World_temp['avg_temp'][-len(PortoAlegre_temp['year'])-2:-2].mean()
diff_avg_temp = avg_temp_POA - avg_temp_World

PortoAlegre_temp.corrwith(World_temp[-len(PortoAlegre_temp['year'])-2:-2])








plt.plot(PortoAlegre_temp['year'],PortoAlegre_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'Porto Alegre')
plt.plot(Perth_temp['year'],Perth_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'Perth')
plt.plot(Paris_temp['year'],Paris_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'Paris')
plt.plot(NY_temp['year'],NY_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'New York')
plt.plot(World_temp['year'],World_temp['7-year Moving Avarage'],
         linestyle='-', marker='o',linewidth=2, markersize=1, label = 'World')
plt.xlabel('Year')
plt.ylabel('Moving Avarege Temperature (ºC) \n 7-year window')
plt.title("Comparison of different cities and the world's \n temperature (ºC) over the years", fontweight = 'bold')
plt.axis([1838,2013,7,19.5])
plt.legend()
plt.grid(True)
plt.savefig('Multiple Cities Moving Avarage Comparisson',dpi = 300,bbox_inches='tight')
plt.show()































