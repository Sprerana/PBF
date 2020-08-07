import pandas as pd
from chart_studio.plotly import iplot
data = pd.read_csv('C:/Users/Hp/Documents/Django/projects/pbf/AirPassengers.csv',index_col=0)
data.head()

data.index = pd.to_datetime(data.index)

data.columns = ['Energy Production']

import plotly.plotly as ply
import cufflinks as cf
data.iplot(title="Energy Production Jan 1985--Jan 2018")

from plotly.plotly import plot_mpl
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(data, model='multiplicative')
fig = result.plot()
plot_mpl(fig)

from pyramid.arima import auto_arima
stepwise_model = auto_arima(data, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())

train = data.loc['1985-01-01':'2016-12-01']
test = data.loc['2017-01-01':]

stepwise_model.fit(train)

future_forecast = stepwise_model.predict(n_periods=37)
# This returns an array of predictions:
print(future_forecast)
array([ 114.35302037,  105.67472349,   91.62172016,   93.11965624,
        103.13943782,  112.0750119 ,  110.28775882,  100.3846244 ,
         92.76377402,   96.56146867,  110.15807481,  122.16905229,
        111.76255057,  102.1074658 ,   90.72177437,   92.21641046,
        103.29671997,  112.53381746,  111.79663986,  101.28342664,
         92.21562554,   95.42427613,  109.83787975,  118.78803148,
        108.06504426,  101.03926634,   89.8586184 ,   91.90975603,
        102.9426644 ,  112.42626585,  111.2655725 ,  100.67041402,
         92.32953027,   95.54048842,  110.86398308,  120.63508802,
        108.74454694])

future_forecast = pd.DataFrame(future_forecast,index = test.index,columns=['Prediction'])
pd.concat([test,future_forecast],axis=1).iplot()

pd.concat([data,future_forecast],axis=1).iplot()