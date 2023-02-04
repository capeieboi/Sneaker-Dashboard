from main import SnkrsBot
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import streamlit as st 
import pandas as pd 
from datetime import datetime
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
# datetime object containing current date and time
def current_time():
    now = datetime.now()
    #print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    return(dt_string)
def main():
    url = 'https://www.nike.com/launch/t/air-force-1-low-x-undefeated-mens-shoes'
    bot = SnkrsBot(url)

    last_price = 0
    data = [[current_time(), last_price]]
    df = pd.DataFrame(data,columns=['Time','Price'])
    st.title("Air force 1 low undefeated-mes-shoes")

    # layout = go.Layout(
    # title= "<b>Price Time monitor</b>",
    # paper_bgcolor = 'rgb(248, 248, 255)',
    # plot_bgcolor = 'rgb(248, 248, 255)',
    # barmode = "stack",
    # xaxis = dict(domain=[0, 0.5], title="Time", linecolor="#BCCCDC",
    # showspikes=True,spikethickness=2,spikedash="dot",spikecolor= "yellowgreen",spikemode="across",),
    # yaxis= dict(title="Revenue",linecolor="#021C1E"),
    # )

    placeholder = st.empty()
    while 1:
        price = bot.get_price()
        data = [[current_time(),price]]
        df_temp = pd.DataFrame(data,columns=['Time','Price'])
        df = pd.concat([df, df_temp], 
                  ignore_index = True)
        print(df.head())
        # line_chart= go.Scatter(x=df['Time'], y=df['Price'])
        # temp_data = []
        # temp_data.append(line_chart)
        # fig= go.Figure(data=temp_data, layout=layout)
        # st.plotly_chart(fig)

        #st.line_chart(df)
        #bot.get_sizes_available()
        with placeholder.container():
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
            #placeholder.line_chart(df,x='Time',y='Price')
                fig = px.line(df, x='Time', y='Price')
                placeholder.write(fig)
            
        if last_price:
            if price < last_price:
                print(f"Price dropped: {last_price - price}")
            elif price > last_price:
                print(f"Price rose: {price - last_price}")
            else:
                print(f"Price stayed: {price}")
        last_price = price
        time.sleep(5)
        #placeholder.empty()

if __name__ == "__main__":
    main()