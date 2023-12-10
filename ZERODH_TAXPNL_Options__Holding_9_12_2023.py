import streamlit as st   # pip install streamlit
import pandas as pd
import plotly.express as px       #                             pip install plotly
import copy
from streamlit_extras.metric_cards import style_metric_cards   #    pip install streamlit-extras
# import time
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

st.set_page_config(page_title="JANRAL ZERODHA",page_icon="🌍",layout="wide")
theme_plotly = None # None or streamlit

# # Style
# with open('style.css')as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Set the background color to blackpip freeze > requirements.txt
background_color = "#000000"
text_color = "#FFFFFF"  # Optional: Set text color to white for better visibility

# Apply custom styles using HTML and CSS
custom_styles = f"""
    <style>
        body {{color: {text_color};}}
        .stApp {{background-color: {background_color};}}
           .plot-container>div {{box-shadow: 0 0 4px "#000000";
    padding: 10px;}}
    </style>
"""
# Display the custom styles using markdown
custom_styles2 = f"""
       <style>
       div[data-testid="metric-container"] {{background-color: rgba(28, 131, 225, 0.1);}}
       {{border: 1px solid rgba(28, 131, 225, 0.1);}}
       {{padding: 5% 5% 5% 10%;}}
       {{border-radius: 5px;}}
       {{color: rgb(30, 103, 119);}}
       {{overflow-wrap: break-word;}}

        /* breakline for metric text         */
        div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {{
        overflow-wrap: break-word;}}
        {{white-space: break-spaces;}}
        {{color: red;}}
    </style>
     """
st.markdown(custom_styles2, unsafe_allow_html=True)
st.sidebar.markdown(custom_styles, unsafe_allow_html=True)
def header_selet_Equity(tradebook,file_extension):
    red_padas = file_extension(tradebook)
    entry_buy = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00,"Holding_day":None, "cumsum": None}
    entry_list = []
    entry_buy_df = red_padas.fillna(value=0.00)

    index_lis = red_padas.index.tolist()
    count = 1
    for index in index_lis:
        cadican = entry_buy_df.iloc[index, 1]
        if cadican == "Equity" and count:
          for index_2 in index_lis[index:]:
             cadican = entry_buy_df.iloc[index_2, 1]
             # print(index_2,cadican,'Quantity=',entry_buy_df.iloc[index_2, 5], count )
             if cadican == "Symbol" and entry_buy_df.iloc[index_2, 5] and count:
                # print(index_2, cadican, 'Quantity=', entry_buy_df.iloc[index_2, 5], count)
                for index_3 in index_lis[index_2:]:
                    if not entry_buy_df.iloc[index_3, 5] == 'Quantity'  and entry_buy_df.iloc[index_3, 9] > 0 :
                       entry_buy["symbol"] = entry_buy_df.iloc[index_3, 1]
                       entry_buy["Entry_Date"] = entry_buy_df.iloc[index_3, 3]
                       entry_buy["Exit_Date"] = entry_buy_df.iloc[index_3, 4]
                       entry_buy["Qtt"] = entry_buy_df.iloc[index_3, 5]
                       entry_buy["Buy_Value"] = entry_buy_df.iloc[index_3, 6]
                       entry_buy["Sell_Value"] = entry_buy_df.iloc[index_3, 7]
                       entry_buy["Profit"] = entry_buy_df.iloc[index_3, 8]
                       entry_buy["Holding_day"] = entry_buy_df.iloc[index_3, 9]
                       # print(entry_buy)
                       if entry_buy["Qtt"]:
                          entry_list.append(copy.deepcopy((entry_buy)))
                       if not entry_buy["Qtt"]:
                          count = 0
                          break
    # print(pd.DataFrame(entry_list).head(10))
    return entry_list

def header_selet_Intraday(tradebook,file_extension):
    red_padas = file_extension(tradebook)
    entry_buy = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00,"Holding_day":None, "cumsum": None}
    entry_list = []
    entry_buy_df = red_padas.fillna(value=0.00)

    index_lis = red_padas.index.tolist()
    count = 1
    for index in index_lis:
        cadican = entry_buy_df.iloc[index, 1]
        if cadican == "Equity" and count:
          for index_2 in index_lis[index:]:
             cadican = entry_buy_df.iloc[index_2, 1]
             # print(index_2,cadican,'Quantity=',entry_buy_df.iloc[index_2, 5], count )
             if cadican == "Symbol" and entry_buy_df.iloc[index_2, 5] and count:
                # print(index_2, cadican, 'Quantity=', entry_buy_df.iloc[index_2, 5], count)
                for index_3 in index_lis[index_2:]:
                    if not entry_buy_df.iloc[index_3, 5] == 'Quantity' and entry_buy_df.iloc[index_3, 9] == 0:
                       entry_buy["symbol"] = entry_buy_df.iloc[index_3, 1]
                       entry_buy["Entry_Date"] = entry_buy_df.iloc[index_3, 3]
                       entry_buy["Exit_Date"] = entry_buy_df.iloc[index_3, 4]
                       entry_buy["Qtt"] = entry_buy_df.iloc[index_3, 5]
                       entry_buy["Buy_Value"] = entry_buy_df.iloc[index_3, 6]
                       entry_buy["Sell_Value"] = entry_buy_df.iloc[index_3, 7]
                       entry_buy["Profit"] = entry_buy_df.iloc[index_3, 8]
                       entry_buy["Holding_day"] = entry_buy_df.iloc[index_3, 9]
                       # print(entry_buy)
                       if entry_buy["Qtt"]:
                          entry_list.append(copy.deepcopy((entry_buy)))
                       if not entry_buy["Qtt"]:
                          count = 0
                          break
    # print(pd.DataFrame(entry_list).head(10))
    return entry_list
def header_selet_Options(tradebook,file_extension):
    red_padas = file_extension(tradebook)
    entry_buy = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00, "cumsum": None}
    entry_Options_list = [entry_buy]
    entry_buy_Options_df = red_padas.fillna(value=0.00)
    index_Options_lis = red_padas.index.tolist()
    count = 1
    for index in index_Options_lis:
        cadican_Options = entry_buy_Options_df.iloc[index, 1]
        if cadican_Options == "F&O" and count:
           for index_2 in index_Options_lis[index:]:
             cadican = entry_buy_Options_df.iloc[index_2, 1]
             # print(index_2,cadican,'Quantity=',entry_buy_Options_df.iloc[index_2, 4], count )
             if cadican == "Symbol" and entry_buy_Options_df.iloc[index_2, 4] and count:
                # print(index_2, cadican, 'Quantity=', entry_buy_df.iloc[index_2, 5], count)
                for index_3 in index_Options_lis[index_2:]:
                    if not entry_buy_Options_df.iloc[index_3, 4] == 'Quantity':
                       entry_buy["symbol"] = entry_buy_Options_df.iloc[index_3, 1]
                       entry_buy["Entry_Date"] = entry_buy_Options_df.iloc[index_3, 2]
                       entry_buy["Exit_Date"] = entry_buy_Options_df.iloc[index_3, 3]
                       entry_buy["Qtt"] = entry_buy_Options_df.iloc[index_3, 4]
                       entry_buy["Buy_Value"] = entry_buy_Options_df.iloc[index_3, 5]
                       entry_buy["Sell_Value"] = entry_buy_Options_df.iloc[index_3, 6]
                       entry_buy["Profit"] = entry_buy_Options_df.iloc[index_3, 7]
                       # print(entry_buy)
                       if entry_buy["Qtt"]:
                           entry_Options_list.append(copy.deepcopy((entry_buy)))
                       if not entry_buy["Qtt"]:
                          count = 0
                          break
    return entry_Options_list

def header_selet_Charges(tradebook,file_extension,sheet_name):
    red_padas = file_extension(tradebook,sheet_name=sheet_name)
    entry_Charges = {"Account_Head": None, "Amount": None,}
    entry_Charges_list = []
    entry_Charges_df1 = red_padas.fillna(value=0.00)
    entry_Charges_df = pd.DataFrame(entry_Charges_df1)
    index_Charges_lis = red_padas.index.tolist()
    count = 1
    for index1 in index_Charges_lis:
        cadican_Charges = entry_Charges_df.iloc[index1, 1]
        if cadican_Charges == "Charges" and count:
           for index2 in index_Charges_lis[index1:]:
             cadican = entry_Charges_df.iloc[index2, 1]
             # print(index2,cadican,'Amount=',entry_Charges_df.iloc[index2, 2], count )
             if cadican == "Account Head" and entry_Charges_df.iloc[index2, 1] and count:
                # print(index2, cadican, 'Amount==',  entry_Charges_df.iloc[index2, 2], count)
                for index3 in index_Charges_lis[index2:]:
                    if not entry_Charges_df.iloc[index3, 2] == 'Amount':
                       entry_Charges["Account_Head"] = entry_Charges_df.iloc[index3, 1]
                       entry_Charges["Amount"] = entry_Charges_df.iloc[index3, 2]
                       if entry_Charges["Amount"]:
                           entry_Charges_list.append(copy.deepcopy((entry_Charges)))
                       if entry_Charges["Account_Head"] == "Other Charges":
                          count = 0
                          break
    return entry_Charges_list

def header_selet_Charges_credits_debits(tradebook,file_extension,sheet_name):
    red_padas = file_extension(tradebook,sheet_name=sheet_name)
    entry_debits = {"Particulars": None, "Posting_Date": None,"Debit": None}
    entry_debits_list = []
    entry_debits_df1 = red_padas.fillna(value=0.00)
    entry_debits_df = pd.DataFrame(entry_debits_df1)
    index_debits_lis = red_padas.index.tolist()
    count = 1
    for index1 in index_debits_lis:
        cadican_Charges = entry_debits_df.iloc[index1, 1]
        if cadican_Charges == "Equity" and count:
           for index2 in index_debits_lis[index1:]:
             cadican = entry_debits_df.iloc[index2, 1]
             # print(index2,cadican,'Amount=',entry_Charges_df.iloc[index2, 2], count )
             if cadican == "Particulars" and entry_debits_df.iloc[index2, 3] and count:
                # print(index2, cadican, 'Amount==',  entry_Charges_df.iloc[index2, 2], count)
                for index3 in index_debits_lis[index2:]:
                    if not entry_debits_df.iloc[index3, 3] == "Debit" :
                       entry_debits["Particulars"] = entry_debits_df.iloc[index3, 1]
                       entry_debits["Posting_Date"] = entry_debits_df.iloc[index3, 2]
                       entry_debits["Debit"] = entry_debits_df.iloc[index3, 3]

                       if entry_debits["Debit"]:
                           entry_debits_list.append(copy.deepcopy((entry_debits)))
                       if entry_debits["Particulars"] == "Mutual Funds":
                          count = 0
                          break

    # print(pd.DataFrame(entry_debits_list))
    return entry_debits_list
def risk_management(risk_df,symbol):
    if symbol:
        risk_df = risk_df.loc[(risk_df['symbol'] == symbol)]
    else:
        risk_df = risk_df
    risk_list = []
    risk_dict = {"Invested": None, "Wins": None, "Losser": None, "Nb_of_trade": None, "Profit": None, "Loss": None,
                 "Fees": 0.00, "RR": 0.00, "Avg_Winner": 0.00, "Avg_Loser": 0.00, "Bigges_Winner": 0.00,
                "Bigges_Loser": 0.00, "Buy_avg": 0.00, "Qtt_Buy": 0, 'sell_value': 0.00, 'Sell_quantity': 0,
                "Sell_avg": 0.00, "PNL_Total": 0.00, "PNL_Total_parsent": 0.00, "Avg_Return": 0.00}
    risk_dict["Invested"] = risk_df['Buy_Value'].sum()
    risk_dict["Wins"] = len(risk_df.loc[(risk_df['Profit'] > 0)])
    risk_dict["Losser"] = len(risk_df.loc[(risk_df['Profit'] <= 0)])
    risk_dict["Nb_of_trade"] = risk_dict["Wins"] + risk_dict["Losser"]
    risk_dict["Profit"] = risk_df.loc[risk_df['Profit'] >= 0, 'Profit'].sum() if (risk_dict['Profit']) != 0 else 0
    risk_dict["Loss"] = risk_df.loc[risk_df['Profit'] < 0, 'Profit'].sum()
    risk_dict["Fees"] = risk_dict["Nb_of_trade"] * 15.96
    risk_dict["RR"] = round(risk_dict["Profit"] / abs(risk_dict["Loss"]), 2) if abs(risk_dict["Loss"]) != 0 else 0
    risk_dict["Avg_Winner"] = risk_dict["Profit"] / risk_dict["Nb_of_trade"]
    risk_dict["Avg_Loser"] = risk_dict["Loss"] / risk_dict["Nb_of_trade"]
    risk_dict["Bigges_Winner"] = risk_df['Profit'].max()
    risk_dict["Bigges_Loser"] = risk_df['Profit'].min()
    risk_dict["Buy_avg"] = risk_dict["Invested"] / float(risk_df["Qtt"].sum()) if (risk_dict["Invested"]) != 0 else 0
    risk_dict["sell_value"] = float(risk_df["Sell_Value"].sum())
    risk_dict["Sell_Qtt"] = float(risk_df["Qtt"].sum())
    risk_dict["Sell_avg"] = risk_dict["sell_value"] / float(risk_df["Qtt"].sum()) if (risk_df["Qtt"].sum()) != 0 else 0
    risk_dict["PNL_Total_parsent"] = round(risk_dict["PNL_Total"] / risk_dict["Invested"] * 100, 2) if (risk_dict["Invested"]) != 0 else 0
    risk_dict["PNL_Total"] = (risk_dict["Profit"] + risk_dict["Loss"]) #-risk_dict["Fees"]
    risk_dict["Avg_Return"] = risk_dict["PNL_Total"] / risk_dict["Nb_of_trade"] if (risk_dict["Nb_of_trade"]) != 0 else 0
    risk_list.append(copy.deepcopy((risk_dict)))
    risk_list_pd = pd.DataFrame(risk_list)
    return risk_dict
def metric_label(risk_dict):

    total1, total3, total4, total5, total6, = st.columns(5, gap="small")    #"small"  'large'
    with total1:
     st.metric(label="Nb_of_trade", value=f'{risk_dict["Nb_of_trade"]:,.0f}')
    with total3:
        st.metric(label="Fees", value=f'{risk_dict["Fees"]:,.0f}')
    with total4:
        st.metric(label="RETURN ALL", value=f'{risk_dict["PNL_Total"]:,.0f}')
    with total5:
        st.metric(label="%RETURN ALL%", value=risk_dict["PNL_Total_parsent"])
    with total6:
        st.metric(label="R!R", value=f'1:{risk_dict["RR"]:,.0f}')
    total8, total9, total10,  = st.columns(3, gap='large')
    with total8:
         st.metric(label="Wins", value=f'{risk_dict["Wins"]:,.0f}')
    with total9:
       st.metric(label="%Win", value=f'{risk_dict["Wins"] / risk_dict["Nb_of_trade"] * 100:,.0f}%')
    with total10:
         st.metric(label="Profit", value=f'{risk_dict["Profit"]:,.0f}')
    total11, total12, total13 = st.columns(3, gap='large')
    with total11:
        st.metric(label="Losser", value=f'{risk_dict["Losser"]:,.0f}')
    with total12:
         st.metric(label="%Losser", value=f'{risk_dict["Losser"] / risk_dict["Nb_of_trade"] * 100:,.0f}%')
    with total13:
        st.metric(label="Loss", value=f'{risk_dict["Loss"]:,.0f}')
    total16, total17, total18, total19, total20 = st.columns(5, gap='large')
    with total16:
        st.metric(label="Avg_Return", value=f'{risk_dict["Avg_Return"]:,.0f}')
    with total17:
        st.metric(label="Avg_Winner", value=f'{ risk_dict["Avg_Winner"]:,.0f}')
    with total18:
        st.metric(label="Avg_Loser", value=f'{ risk_dict["Avg_Loser"]:,.0f}')
    with total19:
        st.metric(label="Bigges_Winner", value=f'{risk_dict["Bigges_Winner"]}')
    with total20:
        st.metric(label="Bigges_Loser", value=f'{ risk_dict["Bigges_Loser"]:,.0f}')
    style_metric_cards(background_color="#121270", border_left_color="#f20045" ,box_shadow="3px") #color="white"


def Profit_pie(pie_df,symbol):
    pie_df = pd.DataFrame(pie_df)
    if symbol:
        pie_df = pie_df.loc[(pie_df["symbol"] == symbol)]
        names = 'Profit'
    else:
        pie_df = pie_df
        names = "symbol"
    Profit = pie_df.loc[pie_df['Profit'] >= 0, 'Profit'].sum()
    Profit_pie = pie_df.loc[pie_df['Profit'] >= 0]
    fig = px.pie(Profit_pie, values='Profit',names=names, title=f"Pofit_piy_chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Profit value', legend_y=0.9,paper_bgcolor= '#202228',width=1200,height=725)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
def Loss_pie(pie_df, symbol):
    pie_df = pd.DataFrame(pie_df)
    if symbol:
        pie_df = pie_df.loc[(pie_df["symbol"] == symbol)]
        names = 'Profit'
    else:
        pie_df = pie_df
        names = "symbol"
    Loss = pie_df.loc[pie_df['Profit'] < 0, 'Profit'].sum()
    Loss_pie = pie_df.loc[pie_df['Profit'] < 0]
    Loss_pie =pd.DataFrame(Loss_pie)
    Loss_pie['Profit'] = Loss_pie['Profit'].abs()
    fig = px.pie(Loss_pie, values='Profit', names=names, title=f"Loss_piy_chaty = Rs. {round(Loss,2)}")
    fig.update_layout(legend_title='Loss value', legend_y=0.9,paper_bgcolor= '#202228',width=1200,height=725)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
def Equity_Options_BOKREJ_pie(pie_df,symbol):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = pie_df_data['Profit'].sum()
    pie_df = pd.DataFrame(pie_df_data)
    pie_df['Profit'] = pie_df['Profit'].abs()
    Profit_pie = pie_df.loc[pie_df['Profit'] >= 0]
    def colors_(df):
        if df > 0 :
            colors_ ='green'             #facecolor  '#333333'
        else:
            colors_ = 'red'
        return colors_
    # print(pie_df_data)

    custom_colors = {'Holding': colors_(df=pie_df_data['Profit'][0]),  'Intraday': colors_(df=pie_df_data['Profit'][1]),
                     'Options': colors_(df=pie_df_data['Profit'][2]),  'Charges': 'red', 'Charges debit': colors_(df=pie_df_data['Profit'][4])}

    fig = px.pie(Profit_pie, values='Profit',names='symbol',color='symbol', color_discrete_map=custom_colors,
                 title=f"ALL DATA piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Profit value', legend_y=0.9, paper_bgcolor= '#202228',width=1200, height=625)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    return pie_df_data

def Charges_pie(pie_df):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = -abs(pie_df_data['Amount'].sum())
    fig = px.pie(pie_df_data, values='Amount',names='Account_Head',title=f"Charges piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Charges value', legend_y=0.9, paper_bgcolor= '#202228',width=1200, height=625)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.dataframe(pie_df_data, use_container_width=False, height=200, width=1200)
    convert_df(df=pie_df_data, file_name="MANOJ KUKNA.csv")
    return pie_df_data

def Charges_Debits_and_Credits_pie(pie_df):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = -abs(pie_df_data['Debit'].sum())
    fig = px.pie(pie_df_data.head(20), values='Debit',names='Particulars',title=f"Charges_Debits_and_Credits piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Charges_Debits_and_Credits value', legend_y=0.9, paper_bgcolor= '#202228',width=1200, height=625)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    st.dataframe(pie_df_data, use_container_width=False, height=200, width=1200)
    convert_df(df=pie_df_data, file_name="MANOJ KUKNA.csv")
    return pie_df_data


def convert_df(df, file_name):
    csv1 = df.to_csv().encode("utf-8")
    st.download_button(
        label="Download data as CSV",
        data=csv1,
        file_name=file_name,
        mime="text/csv",key=f"{csv1}")
    return
def dataframe_columns(list):
    dataframe_columns_list = list.columns.values.tolist()
    return dataframe_columns_list
def line_chart(data, title):
    st.line_chart(data)
    st.title(title)
def dataframe(dataframe_df, default, symbol):
    global df_selec
    if symbol:
        dataframe_df = dataframe_df.loc[(dataframe_df['symbol'] == symbol)]
    else:
        dataframe_df = dataframe_df
    dataframe_df = pd.DataFrame(dataframe_df)
    dataframe_df['cumsum'] = dataframe_df['Profit'].cumsum()
    PNL_Total =dataframe_df['Profit'].sum()
    if PNL_Total > 0:
       st.markdown("<h1 style='color: green;'>ZERODHA Rs</h1>", unsafe_allow_html=True)

    dataframe_df.reset_index(inplace=True, drop=True)
    showData = st.multiselect('Filter: ', dataframe_df.columns,key=f'filter_{dataframe_df}', default=default)
    st.dataframe(dataframe_df[showData], use_container_width=False, height=200, width=1200)
    convert_df(df=dataframe_df, file_name="MANOJ KUKNA.csv")

    st.line_chart(dataframe_df, x='Entry_Date', y='cumsum', height=200, width=1200)
    return dataframe_df
all_qttar_list = []
all_qttar_dict = {"Holding": None, "Intraday": None, "Options": None, "Charges": None,"Charges_credits_debits":None}

def uploaded_file():
    uploaded_file = st.file_uploader("your uploaded_file DOWNLOAD TAX P&L REPORT FOR ALL SEGMENTS", type=['xlsx', 'xls', 'xlsm', 'csv'])
    if uploaded_file is not None:
       # Check the file type and read accordingly
       if uploaded_file.name.endswith(('.xlsx', '.xls', '.xlsm')):
          all_qttar_dict["Holding"] = header_selet_Equity(tradebook=uploaded_file,file_extension=pd.read_excel)
          all_qttar_dict["Intraday"] = header_selet_Intraday(tradebook=uploaded_file, file_extension=pd.read_excel)
          all_qttar_dict["Options"] = header_selet_Options(tradebook=uploaded_file, file_extension=pd.read_excel)
          all_qttar_dict["Charges"] = header_selet_Charges(tradebook=uploaded_file,file_extension=pd.read_excel, sheet_name="Equity")
          all_qttar_dict["Charges_credits_debits"] = header_selet_Charges_credits_debits(tradebook=uploaded_file,
                                                                                         file_extension=pd.read_excel,
                                                                                         sheet_name="Other Debits and Credits")
          return all_qttar_dict
       elif uploaded_file.name.endswith('.csv'):
           all_qttar_dict["Holding"] = header_selet_Equity(tradebook=uploaded_file, file_extension=pd.read_csv)
           all_qttar_dict["Intraday"] = header_selet_Intraday(tradebook=uploaded_file, file_extension=pd.read_csv)
           all_qttar_dict["Options"] = header_selet_Options(tradebook=uploaded_file, file_extension=pd.read_csv)
           all_qttar_dict["Charges"] = header_selet_Charges(tradebook=uploaded_file,file_extension=pd.read_csv, sheet_name="Equity")
           all_qttar_dict["Charges_credits_debits"] = header_selet_Charges_credits_debits(tradebook=pd.read_csv,file_extension=pd.read_excel,sheet_name="Other Debits and Credits")
           return all_qttar_dict
    return all_qttar_dict
uploaded_file()
addresh= "taxpnl-JD0585\\taxpnl-JD0585-2023_2024-Q1-Q3.xlsx"

df = pd.DataFrame(all_qttar_dict["Holding"])
if not len(df):
    all_qttar_dict["Holding"] = header_selet_Equity(tradebook=addresh, file_extension=pd.read_excel)
    all_qttar_dict["Intraday"] = header_selet_Intraday(tradebook=addresh, file_extension=pd.read_excel)
    all_qttar_dict["Options"] = header_selet_Options(tradebook=addresh, file_extension=pd.read_excel)
    all_qttar_dict["Charges"] = header_selet_Charges(tradebook=addresh,file_extension=pd.read_excel, sheet_name="Equity")
    all_qttar_dict["Charges_credits_debits"] = header_selet_Charges_credits_debits(tradebook=addresh, file_extension=pd.read_excel, sheet_name="Other Debits and Credits")
    # print(pd.DataFrame(all_qttar_dict["Charges_credits_debits"]))
def Equity_Options_BOKREJ(Holding,Intraday,Options,Charges,Charges_credits_debits):
      Holding = pd.DataFrame(Holding)
      Intraday = pd.DataFrame(Intraday)
      Options = pd.DataFrame(Options)
      Charges = pd.DataFrame(Charges)
      Charges_credits_debits = pd.DataFrame(Charges_credits_debits)
      Equity_Options_BOKREJ = pd.DataFrame(['Holding',"Intraday",'Options','Charges','Charges debit'],columns=["symbol"])
      Equity_Options_BOKREJ['Entry_Date'] = " "
      Equity_Options_BOKREJ['Profit'] =Holding['Profit'].sum(), Intraday['Profit'].sum(),Options['Profit'].sum() ,-abs(int(Charges['Amount'].sum())),-abs(int(Charges_credits_debits['Debit'].sum()))
      Equity_Options_BOKREJ['cumsum'] = Equity_Options_BOKREJ['Profit'].cumsum()

      # print(Equity_Options_BOKREJ)
      return Equity_Options_BOKREJ






#  stock market journal  STOCK MARET JOURNAL        Z AI TECHNOLOGY     manojkukna/JANRAL_ZERODHA
#   STOCK MARKET JANRAL
# streamlit run ZERODH_TAXPNL_Options__Holding_9_12_2023.py



#      pip install streamlit
#      pip install plotly
#      pip install streamlit-extras

#      pip install openpyxl
