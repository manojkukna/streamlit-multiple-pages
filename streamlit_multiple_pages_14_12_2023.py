# import streamlit as st                                         # pip install streamlit
import pandas as pd
import plotly.express as px                                    #  pip install plotly
import copy
# import time

# import streamlit_multiple_home_13_12_2023 as home
# import streamlit as st  # streamlit pip install
# import pandas as pd
# import plotly.express as px       #                             pip install plotly
import copy
from streamlit_option_menu import option_menu     # pip install streamlit-option-menu
# import streamlit_multiple_pages_13_12_2023 as z
from streamlit_extras.metric_cards import style_metric_cards
#
# st.set_page_config(page_title="KUKAN MANOJ22",page_icon="📊",layout="wide",initial_sidebar_state="expanded",)  # "auto" or "expanded" or "collapsed"
# # Set dark theme using custom CSS
# st.markdown(
#     """
#     <style>
#         body {
#             color: #FFFFFF;  /* Text color */
#             background-color: 'black';  /* Background color */
#         }
#         /* Add more custom styles as needed */
#     </style>
#     """,
#     unsafe_allow_html=True)

def header_selet_Holding(tradebook,file_extension):
    red_padas = file_extension(tradebook)
    entry_dict_Holding = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00,"Holding_day": None, "cumsum": None}
    entry_list_Holding = []
    entry_buy_df = red_padas.fillna(value=0.00)
    entry_list_Holding.append(copy.deepcopy((entry_dict_Holding)))
    index_lis_Holding = red_padas.index.tolist()
    count = 1
    for index in index_lis_Holding:
        cadican = entry_buy_df.iloc[index, 1]
        if cadican == "Equity" and count:
          for index_2 in index_lis_Holding[index:]:
             cadican = entry_buy_df.iloc[index_2, 1]
             # print(index_2,cadican,'Quantity=',entry_buy_df.iloc[index_2, 5], count )
             if cadican == "Symbol" and entry_buy_df.iloc[index_2, 5] and count:
                # print(index_2, cadican, 'Quantity=', entry_buy_df.iloc[index_2, 5], count)
                for index_3 in index_lis_Holding[index_2:]:
                  if not entry_buy_df.iloc[index_3, 5] == 'Quantity' and entry_buy_df.iloc[index_3, 9] > 0:
                     if not entry_buy_df.iloc[index_3, 4] == 'Quantity':
                       entry_dict_Holding["symbol"] = entry_buy_df.iloc[index_3, 1]
                       entry_dict_Holding["Entry_Date"] = entry_buy_df.iloc[index_3, 3]
                       entry_dict_Holding["Exit_Date"] = entry_buy_df.iloc[index_3, 4]
                       entry_dict_Holding["Qtt"] = entry_buy_df.iloc[index_3, 5]
                       entry_dict_Holding["Buy_Value"] = entry_buy_df.iloc[index_3, 6]
                       entry_dict_Holding["Sell_Value"] = entry_buy_df.iloc[index_3, 7]
                       entry_dict_Holding["Profit"] = entry_buy_df.iloc[index_3, 8]
                       entry_dict_Holding["Holding_day"] = entry_buy_df.iloc[index_3, 9]
                       # print(entry_buy)
                       if entry_dict_Holding["Qtt"]:
                          entry_list_Holding.append(copy.deepcopy((entry_dict_Holding)))
                       if not entry_dict_Holding["Qtt"]:
                          count = 0
                          break
    # print(pd.DataFrame(entry_list_Holding).head(10))

    return entry_list_Holding #if entry_list_Holding != [] else [entry_buy_Holding]

def header_selet_Intraday(tradebook,file_extension):
    red_padas_Intraday1 = file_extension(tradebook)
    red_padas_Intraday = pd.DataFrame(red_padas_Intraday1)

    entry_dict_Intraday = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00,"Holding_day":None, "cumsum": None}
    entry_list_Intraday = []
    entry_list_Intraday.append(copy.deepcopy((entry_dict_Intraday)))
    entry_buy_df_Intraday = red_padas_Intraday.fillna(value=0.00)

    index_lis = red_padas_Intraday.index.tolist()
    count = 1
    for index in index_lis:
        cadican = entry_buy_df_Intraday.iloc[index, 1]
        if cadican == "Equity" and count:
          for index_2 in index_lis[index:]:
             cadican = entry_buy_df_Intraday.iloc[index_2, 1]

             # print(index_2,cadican,'Quantity=', entry_buy_df_Intraday.iloc[index_2, 5], count)

             if cadican == "Symbol" and entry_buy_df_Intraday.iloc[index_2, 5] and count:
                # print(index_2, cadican, 'Quantity=', entry_buy_df_Intraday.iloc[index_2, 5], count)
                for index_3 in index_lis[index_2:]:
                   if not entry_buy_df_Intraday.iloc[index_3, 5] == 'Quantity' and entry_buy_df_Intraday.iloc[index_3, 9] == 0:
                       if not entry_buy_df_Intraday.iloc[index_3, 4] == 'Quantity' :
                        entry_dict_Intraday["symbol"] = entry_buy_df_Intraday.iloc[index_3, 1]
                        entry_dict_Intraday["Entry_Date"] = entry_buy_df_Intraday.iloc[index_3, 3]
                        entry_dict_Intraday["Exit_Date"] = entry_buy_df_Intraday.iloc[index_3, 4]
                        entry_dict_Intraday["Qtt"] = entry_buy_df_Intraday.iloc[index_3, 5]
                        entry_dict_Intraday["Buy_Value"] = entry_buy_df_Intraday.iloc[index_3, 6]
                        entry_dict_Intraday["Sell_Value"] = entry_buy_df_Intraday.iloc[index_3, 7]
                        entry_dict_Intraday["Profit"] = entry_buy_df_Intraday.iloc[index_3, 8]
                        entry_dict_Intraday["Holding_day"] = entry_buy_df_Intraday.iloc[index_3, 9]

                        if not entry_dict_Intraday["Qtt"] == 0.0:
                            # print(not entry_dict_Intraday["Qtt"] == 0.0, entry_dict_Intraday)
                            entry_list_Intraday.append(copy.deepcopy((entry_dict_Intraday)))
                            # print(entry_list_Intraday)
                   if entry_buy_df_Intraday.iloc[index_3, 1] == "Equity - Buyback":
                                count = 0
                                break

    # if entry_list_Intraday:
    #     entry_list_Intraday = [entry_dict_Intraday]
    # print(pd.DataFrame(entry_list_Intraday))
    return entry_list_Intraday   # if entry_list_Intraday != [] else  entry_dict_Intraday
def header_selet_Options(tradebook,file_extension):
    red_padas_Options = file_extension(tradebook)
    entry_dict_Options = {'symbol': None, "Entry_Date": None, 'Exit_Date': None, 'Qtt': None, "Buy_Value": 0,
                 "Sell_Value": 0.00, "Profit": 0.00, "cumsum": None}
    entry_Options_list = []
    entry_Options_list.append(copy.deepcopy((entry_dict_Options)))
    entry_buy_Options_df = red_padas_Options.fillna(value=0.00)
    index_Options_lis = red_padas_Options.index.tolist()
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
                     if not entry_buy_Options_df.iloc[index_3, 4] == 'Quantity':
                       entry_dict_Options["symbol"] = entry_buy_Options_df.iloc[index_3, 1]
                       entry_dict_Options["Entry_Date"] = entry_buy_Options_df.iloc[index_3, 2]
                       entry_dict_Options["Exit_Date"] = entry_buy_Options_df.iloc[index_3, 3]
                       entry_dict_Options["Qtt"] = entry_buy_Options_df.iloc[index_3, 4]
                       entry_dict_Options["Buy_Value"] = entry_buy_Options_df.iloc[index_3, 5]
                       entry_dict_Options["Sell_Value"] = entry_buy_Options_df.iloc[index_3, 6]
                       entry_dict_Options["Profit"] = entry_buy_Options_df.iloc[index_3, 7]
                       # print(entry_buy)
                       if entry_dict_Options["Qtt"]:
                           entry_Options_list.append(copy.deepcopy((entry_dict_Options)))
                  if entry_buy_Options_df.iloc[index_3, 1] == "Currency":
                          count = 0
                          break

    return entry_Options_list

def header_selet_Charges(tradebook,file_extension,sheet_name):
    red_padas = file_extension(tradebook,sheet_name=sheet_name)
    entry_Charges_dict = {"Account_Head": None, "Amount": None,}
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
                       entry_Charges_dict["Account_Head"] = entry_Charges_df.iloc[index3, 1]
                       entry_Charges_dict["Amount"] = entry_Charges_df.iloc[index3, 2]
                       if entry_Charges_dict["Amount"]:
                           entry_Charges_list.append(copy.deepcopy((entry_Charges_dict)))
                       if entry_Charges_dict["Account_Head"] == "Other Charges":
                          count = 0
                          break
    return entry_Charges_list if entry_Charges_list != [] else  entry_Charges_dict

def header_selet_Charges_credits_debits(tradebook,file_extension,sheet_name):
    red_padas = file_extension(tradebook,sheet_name=sheet_name)
    entry_debits_dict = {"Particulars": None, "Posting_Date": None,"Debit": None}
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
                       entry_debits_dict["Particulars"] = entry_debits_df.iloc[index3, 1]
                       entry_debits_dict["Posting_Date"] = entry_debits_df.iloc[index3, 2]
                       entry_debits_dict["Debit"] = entry_debits_df.iloc[index3, 3]

                       if entry_debits_dict["Debit"]:
                           entry_debits_list.append(copy.deepcopy((entry_debits_dict)))
                       if entry_debits_dict["Particulars"] == "Mutual Funds":
                          count = 0
                          break

    # print(pd.DataFrame(entry_debits_list))
    return entry_debits_list if entry_debits_list != [] else entry_debits_dict


def header_selet_Dividends(tradebook,file_extension,sheet_name):
    red_padas = file_extension(tradebook,sheet_name=sheet_name)
    entry_Dividends_dict = {"Symbol": None, "Date": None,"Quantity": None,"Dividend Per Share":None,"Net Dividend Amount":None}
    entry_Dividends_list = []
    entry_Dividends_list.append(copy.deepcopy((entry_Dividends_dict)))
    entry_Dividends_df1 = red_padas.fillna(value=0.00)
    entry_Dividends_df = pd.DataFrame(entry_Dividends_df1)
    index_Dividends_lis = red_padas.index.tolist()
    count = 1
    for index1 in index_Dividends_lis:
        cadican_Dividends = entry_Dividends_df.iloc[index1, 1]
        if cadican_Dividends == "Symbol" and count:
           for index2 in index_Dividends_lis[index1:]:
             cadican = entry_Dividends_df.iloc[index2, 1]
             # print(index2,cadican,'Net Dividend Amount=',entry_Dividends_df.iloc[index2, 6], count )
             if cadican == "Symbol" and entry_Dividends_df.iloc[index2, 3] and count:
                # print(index2, cadican, 'Net Dividend Amount==',  entry_Dividends_df.iloc[index2, 2], count)
                for index3 in index_Dividends_lis[index2:]:
                    if not entry_Dividends_df.iloc[index3, 6] == "Net Dividend Amount":
                       entry_Dividends_dict["Symbol"] = entry_Dividends_df.iloc[index3, 1]
                       entry_Dividends_dict["Date"] = entry_Dividends_df.iloc[index3, 3]
                       entry_Dividends_dict["Quantity"] = entry_Dividends_df.iloc[index3, 4]
                       entry_Dividends_dict["Dividend Per Share"] = entry_Dividends_df.iloc[index3, 5]
                       entry_Dividends_dict["Net Dividend Amount"] = entry_Dividends_df.iloc[index3, 6]
                       # print(entry_Dividends_dict)
                       if entry_Dividends_dict["Quantity"]:
                           # print( entry_Dividends_dict)
                           entry_Dividends_list.append(copy.deepcopy((entry_Dividends_dict)))
                       if entry_Dividends_dict["Symbol"] == "Total Dividend Amount":
                          count = 0
                          break

    # print(pd.DataFrame(entry_Dividends_list))
    # breakpoint()
    return entry_Dividends_list


def risk_management(risk_df,symbol):
    risk_df1 = pd.DataFrame(risk_df)
    risk_df = risk_df1.loc[(risk_df1["Qtt"] > 0)]
    # print(risk_df)

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
    risk_dict["Fees"] = 0    #risk_dict["Nb_of_trade"] * 15.96
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



def Profit_pie(pie_df,symbol,width,height):
    pie_df = pd.DataFrame(pie_df)
    # print("Profit_pie 348",pie_df)
    if symbol:
        pie_df = pie_df.loc[(pie_df["symbol"] == symbol)]
        names = 'Profit'
    else:
        pie_df = pie_df
        names = "symbol"
    Profit = pie_df.loc[pie_df['Profit'] >= 0, 'Profit'].sum()
    Profit_pie = pie_df.loc[pie_df['Profit'] >= 0]
    fig = px.pie(Profit_pie, values='Profit',names=names, title=f"Pofit_piy_chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Profit value', legend_y=0.9,paper_bgcolor= '#202228',width=width,height=height)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    # st.plotly_chart(fig, use_container_width=True, theme=None)
    return fig


def Loss_pie(pie_df, symbol,width,height):
    pie_df = pd.DataFrame(pie_df)
    # print("Profit_pie 348", pie_df)
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
    fig.update_layout(legend_title='Loss value', legend_y=0.9,paper_bgcolor= '#202228', width=width, height=height)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    # st.plotly_chart(fig, use_container_width=True, theme=None)
    return fig


def Equity_Options_BOKREJ_pie(pie_df,symbol,width,height):
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
                     'Options': colors_(df=pie_df_data['Profit'][2]),  'Charges': 'red',
                     'Charges debit': colors_(df=pie_df_data['Profit'][4]), "Dividends" : 'green'}

    fig = px.pie(Profit_pie, values='Profit',names='symbol', color='symbol', color_discrete_map=custom_colors,
                 title=f"ALL DATA piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Profit value', legend_y=0.9, paper_bgcolor= '#202228',width=width,height=height)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))

    return fig



def dataframe_columns(list):
    dataframe_columns_list = list.columns.values.tolist()
    return dataframe_columns_list

def dataframe(dataframe_df, symbol,width,height):
    global df_selec
    if symbol:
        dataframe_df = dataframe_df.loc[(dataframe_df['symbol'] == symbol)]
    else:
        dataframe_df = dataframe_df
    dataframe_df = pd.DataFrame(dataframe_df)
    dataframe_df['cumsum'] = dataframe_df['Profit'].cumsum()
    PNL_Total = dataframe_df['Profit'].sum()

    dataframe_df.reset_index(inplace=True, drop=True)

    return dataframe_df



def Holding_Options_BOKREJ(Holding_df , Intraday, Options, Charges, Charges_credits_debits, Dividends):
    # print(pd.DataFrame(Holding_df))
    # print(pd.DataFrame(Intraday))
    # print(pd.DataFrame(Options))
    # print(pd.DataFrame(Charges))
    # print(pd.DataFrame(Charges_credits_debits))
    # print(pd.DataFrame(Dividends))
    Holding = pd.DataFrame(Holding_df)
    Intraday = pd.DataFrame(Intraday)
    Options = pd.DataFrame(Options)
    Charges = pd.DataFrame(Charges)
    Charges_credits_debits = pd.DataFrame(Charges_credits_debits)
    Dividends = pd.DataFrame(Dividends)
    Holding_Options_BOKREJ = pd.DataFrame(
        ['Holding', "Intraday", 'Options', 'Charges', 'Charges debit', 'Dividends'], columns=["symbol"])
    Holding_Options_BOKREJ['Entry_Date'] = " "

    Holding_Options_BOKREJ['Profit'] = Holding['Profit'].sum(),\
                                      Intraday['Profit'].sum(),\
                                      Options['Profit'].sum(), \
                             -abs(int(Charges['Amount'].sum())), -abs(
                                 int(Charges_credits_debits['Debit'].sum())),\
                                    Dividends['Net Dividend Amount'].sum()

    Holding_Options_BOKREJ['cumsum'] = Holding_Options_BOKREJ['Profit'].cumsum()

    # print(Holding_Options_BOKREJ)
    return Holding_Options_BOKREJ


all_qttar_dict = {"Holding": None, "Intraday": None, "Options": None, "Charges": None,"Charges_credits_debits":None,"Dividends": None}


def all_qttar_dict_Holding_Intraday_Options(all_qttar_dict):
    all_qttar_Holding_Intraday_Options_list = []
    df = [ all_qttar_dict["Holding"], all_qttar_dict["Intraday"], all_qttar_dict["Options"]]
    for df in df:
       for i in range(len(df)):
           all_qttar_Holding_Intraday_Options_list.append(copy.deepcopy(df[i]))
    # print(pd.DataFrame(all_qttar_Holding_Intraday_Options_list))
    return all_qttar_Holding_Intraday_Options_list

def all_qttar_dict_data(all_qttar_dict,addresh,file_extension):
    all_qttar_dict["Holding"] = header_selet_Holding(tradebook=addresh, file_extension=file_extension)
    all_qttar_dict["Intraday"] = header_selet_Intraday(tradebook=addresh, file_extension=file_extension)
    all_qttar_dict["Options"] = header_selet_Options(tradebook=addresh, file_extension=file_extension)
    all_qttar_dict["Charges"] = header_selet_Charges(tradebook=addresh,file_extension=file_extension,sheet_name="Equity")
    all_qttar_dict["Charges_credits_debits"] = header_selet_Charges_credits_debits(tradebook=addresh,file_extension=file_extension, sheet_name="Other Debits and Credits")
    all_qttar_dict["Dividends"] = header_selet_Dividends(tradebook=addresh, file_extension=file_extension,sheet_name="Equity Dividends")
    all_qttar_dict_Holding_Intraday_Options(all_qttar_dict=all_qttar_dict)
    return all_qttar_dict


all_qttar_dict_data(all_qttar_dict=all_qttar_dict,addresh="taxpnl-JD0585-2022_2023-Q1-Q4.xlsx",file_extension=pd.read_excel)

def uploaded_file(uploaded_file):

    if uploaded_file is not None:
       # Check the file type and read accordingly
       if uploaded_file.name.endswith(('.xlsx', '.xls', '.xlsm')):
          all_qttar_dict_data(all_qttar_dict=all_qttar_dict,addresh=uploaded_file, file_extension=pd.read_excel)
          return all_qttar_dict
       elif uploaded_file.name.endswith('.csv'):
           all_qttar_dict_data(all_qttar_dict=all_qttar_dict,addresh=uploaded_file, file_extension=pd.read_csv)
           return all_qttar_dict
    return all_qttar_dict_data(all_qttar_dict=all_qttar_dict,addresh="taxpnl-JD0585-2022_2023-Q1-Q4.xlsx",file_extension=pd.read_excel)


#  stock market journal  STOCK MARET JOURNAL   Z AI TECHNOLOGY     manojkukna/JANRAL_ZERODHA
#   STOCK MARKET JANRAL
# streamlit run streamlit_multiple_pages_12_12_2023.py




    # icons  download      https: // icons.getbootstrap.com /  # icons     'person-circle'
#      pip install streamlit
#      pip install plotly
#      pip install streamlit-extras
#      pip install openpyxl

# python varjan 3.8   up
# Generate the requirements.txt File
# pip freeze > requirements.txt