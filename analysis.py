import pandas as pd
import seaborn.objects as so
from matplotlib import style

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
mort_rate = wdi["Mortality rate, infant (per 1,000 live births)"]
GDP_per = wdi["GDP per capita (constant 2010 US$)"]
country_name = wdi["Country Name"]

my_chart = (
    so.Plot(
        wdi,
        x="GDP per capita (constant 2010 US$)",
        y="Mortality rate, under-5 (per 1,000 live births)",
    )
    .add(so.Dot())
    .label(title="Log GDP and Under-5 Mortality")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})
)

my_chart.show()
