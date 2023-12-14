import streamlit as st  # streamlit pip install
import pandas as pd
import plotly.express as px       #                             pip install plotly
import copy
from streamlit_option_menu import option_menu     # pip install streamlit-option-menu
import streamlit_multiple_pages_14_12_2023 as z
from streamlit_extras.metric_cards import style_metric_cards
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

st.set_page_config(page_title="KUKAN MANOJ",page_icon="📊",layout="wide",initial_sidebar_state="expanded",)  # "auto" or "expanded" or "collapsed"
# Set dark theme using custom CSS
st.markdown(
    """
    <style>
        body {
            color: #FFFFFF;  /* Text color */
            background-color: 'black';  /* Background color */
        }
        /* Add more custom styles as needed */
    </style>
    """,
    unsafe_allow_html=True)



import datetime, time

def time_():
    time_ = time.strftime("%H:%M:%S", time.localtime())
    return (time_)





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

    # print("metric_labe 75",time_())
    style_metric_cards(background_color="#121270", border_left_color="#f20045" ,box_shadow="3px") #color="white"


def line_chart(data, title):
    st.line_chart(data)
    st.title(title)
    # print("line_chart 82",time_())

def convert_df(df, file_name):
    csv1 = df.to_csv().encode("utf-8")
    st.download_button(
        label="Download data as CSV",
        data=csv1,
        file_name=file_name,
        mime="text/csv", key=f"{csv1}")
    return


def Charges_pie(pie_df,width,height):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = -abs(pie_df_data['Amount'].sum())
    fig = px.pie(pie_df_data, values='Amount',names='Account_Head',title=f"Charges piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Charges value', legend_y=0.9, paper_bgcolor= '#202228',width=width,height=height )
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=14, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=None)
    pie_df_data['cumsum'] = -abs(pie_df_data['Amount'].cumsum())
    st.dataframe(pie_df_data, use_container_width=False,width=1200,height=300)
    convert_df(df=pie_df_data, file_name="MANOJ KUKNA.csv")
    return fig



def Charges_Debits_and_Credits_pie(pie_df,width,height):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = -abs(pie_df_data['Debit'].sum())
    fig = px.pie(pie_df_data.head(20), values='Debit',names='Particulars',title=f"Charges_Debits_and_Credits piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Charges_Debits_and_Credits value', legend_y=0.9, paper_bgcolor= '#202228',width=width,height=height)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=20, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=None)
    pie_df_data['cumsum'] = -abs(pie_df_data['Debit'].cumsum())
    st.dataframe(pie_df_data.round(2), use_container_width=False,width=1200,height=300)
    convert_df(df=pie_df_data, file_name="MANOJ KUKNA.csv")
    st.line_chart(pie_df_data, x='Posting_Date', y='cumsum', width=1200, height=300)
    return fig


def Dividends_pie(pie_df,width,height):
    pie_df_data = pd.DataFrame(pie_df)
    Profit = (pie_df_data['Net Dividend Amount'].sum())
    fig = px.pie(pie_df_data.head(20), values='Net Dividend Amount',names='Symbol',title=f"Dividend piy chaty = Rs. {round(Profit,2)}")
    fig.update_layout(legend_title='Dividend value', legend_y=0.9, paper_bgcolor= '#202228',width=width,height=height)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont=dict(size=20, color="white", family="Arial Black"))
    st.plotly_chart(fig, use_container_width=True, theme=None)
    pie_df_data['cumsum'] = pie_df_data['Net Dividend Amount'].cumsum()
    st.dataframe(pie_df_data.round(2), use_container_width=False,width=1200,height=300)
    convert_df(df=pie_df_data, file_name="MANOJ KUKNA.csv")
    st.line_chart(pie_df_data, x='Date', y='cumsum', width=1200, height=300)
    return fig




# print(" 138",time_())

width = 2000
height = 625

all_qttar_dict = 0

def uploaded_file2(all_qttar_dict,key):
    uploaded_file = st.file_uploader("your uploaded_file DOWNLOAD TAX P&L REPORT FOR ALL SEGMENTS",
                                     key=f"{key}",
                                     type=['xlsx', 'xls', 'xlsm', 'csv'])
    if uploaded_file is not None :
       all_qttar_dict_list = z.uploaded_file(uploaded_file)
       all_qttar_dict = all_qttar_dict + 1
       return all_qttar_dict_list

    else:
        if all_qttar_dict == 0 :
            all_qttar_dict_list = z.uploaded_file(uploaded_file)
            all_qttar_dict = all_qttar_dict + 1
            return all_qttar_dict_list
    return all_qttar_dict
import webbrowser

def open_url():
    url = "https://console.zerodha.com/reports/taxpnl/eq"
    webbrowser.open_new_tab(url)



def run(all_qttar_dict):

        all_qttar_dict_list = uploaded_file2(all_qttar_dict=all_qttar_dict,key="key2")
        st.sidebar.image("IMG_20190423_172859.png",
                 caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
        # print("all_qttar_dict_list lin 173 ", time_())
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Home','DOWNLOAD', 'your uploaded_file', 'Holding', 'Intraday', 'Options','Charges','Charges Debits and Credits','Dividends', 'about'],
                #           https: // icons.getbootstrap.com /  # icons     'person-circle'

                icons=['house-fill', 'person-bounding-box','journal-arrow-up', 'trophy-fill', 'apple', 'play-btn-fill','caret-right-square-fill','caret-right-square-fill','caret-right-square-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={"container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "30px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                       "nav-link-selected": {"background-color": "#02ab21"}, })

            # print("option_menu lin 189 ", time_())
        if app == "Home":


            # print(pd.DataFrame(z.all_qttar_dict_Holding_Intraday_Options(all_qttar_dict=all_qttar_dict_list)))
            #
            #


            Holding_Options_BOKREJ_df = z.Holding_Options_BOKREJ(Holding_df=pd.DataFrame(all_qttar_dict_list["Holding"]),
                                                                Intraday=pd.DataFrame(all_qttar_dict_list["Intraday"]),
                                                                Options=pd.DataFrame(all_qttar_dict_list["Options"]),
                                                                Charges=pd.DataFrame(all_qttar_dict_list["Charges"]),
                                                                Charges_credits_debits=pd.DataFrame(all_qttar_dict_list["Charges_credits_debits"]),
                                                                Dividends=pd.DataFrame(all_qttar_dict_list["Dividends"]))

            all_qttar_dict_Holding_Intraday_Options_pd = pd.DataFrame(z.all_qttar_dict_Holding_Intraday_Options(all_qttar_dict=all_qttar_dict_list))


            fig = z.Equity_Options_BOKREJ_pie(pie_df=Holding_Options_BOKREJ_df, symbol=None, width=width, height=height)
            st.plotly_chart(fig, use_container_width=True, theme=None, width=width, height=height)

            metric_label(risk_dict=z.risk_management(risk_df=all_qttar_dict_Holding_Intraday_Options_pd, symbol=None))

            dataframe_df = z.dataframe(dataframe_df=Holding_Options_BOKREJ_df, symbol=None, width=width, height=height)
            showData = st.multiselect('Filter: ', dataframe_df.columns, key=f'filter_{dataframe_df}', default=z.dataframe_columns(list=dataframe_df))
            st.dataframe(dataframe_df[showData], use_container_width=False, width=1200, height=300)
            convert_df(df=dataframe_df, file_name="MANOJ KUKNA.csv")


            all_qttar_dict_Holding_Intraday_Options_pd =  all_qttar_dict_Holding_Intraday_Options_pd.loc[(all_qttar_dict_Holding_Intraday_Options_pd["Qtt"] > 0)]

            st.dataframe(all_qttar_dict_Holding_Intraday_Options_pd, use_container_width=False, width=1200, height=300)
            convert_df(df=all_qttar_dict_Holding_Intraday_Options_pd, file_name="MANOJ KUKNA.csv")

        # print("Home lin 215 ", time_())
        if app == "DOWNLOAD":
            app = option_menu(
                menu_title='DOWNLOAD TAX P&L REPORT FOR ALL SEGMENTS ',
                options=['DOWNLOAD zhorodh',""],icons=['trophy-fill','house-fill',],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={"container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "30px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"}, })





            if app == 'DOWNLOAD zhorodh':
                # Write some JavaScript code to capture mouse clicks
                # js_code = f"""
                # js_code = f"""
                # <script>
                # var selectbox = document.querySelector('.stSelectbox');
                # selectbox.addEventListener("dblclick", function() {{
                # console.log("Double-clicked on: {app}");
                # }});
                # </script>
                # """
                #
                # # Display the JavaScript code using the `st.write` function
                # st.write(js_code, unsafe_allow_html=True)
                open_url()
                # time.sleep(2)


            st.image("zhrodh.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("tax_pnl1.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("reports.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("download.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")


            # print("DOWNLOAD lin 240 ", time_())
        if app == 'your uploaded_file':
            st.image("zhrodh.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("tax_pnl1.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("reports.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("download.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("uploaded.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            #
            # print("your uploaded_fi lin 253 ", time_())
        if app == 'Holding':
            # print(all_qttar_dict["Holding"])

            fig2 = z.Profit_pie(pie_df=all_qttar_dict_list["Holding"], symbol=None,width=width,height=height)
            st.plotly_chart(fig2, use_container_width=True, theme=None)










            fig3 = z.Loss_pie(all_qttar_dict_list['Holding'], symbol=None,width=width,height=height)
            st.plotly_chart(fig3, use_container_width=True, theme=None)

            metric_label(risk_dict=z.risk_management(risk_df=all_qttar_dict_list['Holding'], symbol=None))

            dataframe_df2 = z.dataframe(dataframe_df=all_qttar_dict_list["Holding"], symbol=None, width=width, height=height)
            showData = st.multiselect('Filter: ', dataframe_df2.columns, key=f'filter_{dataframe_df2}',
                                      default=z.dataframe_columns(list=dataframe_df2))
            st.dataframe(dataframe_df2[showData], use_container_width=False, width=1200, height=300)
            convert_df(df=dataframe_df2, file_name="MANOJ KUKNA.csv")
            st.line_chart(dataframe_df2, x='Entry_Date', y='cumsum', width=1200, height=300)

            # print("Holding lin 281 ", time_())
        if app == 'Intraday':
            fig4 = z.Profit_pie(pie_df=all_qttar_dict_list["Intraday"], symbol=None, width=width, height=height)
            st.plotly_chart(fig4, use_container_width=True, theme=None)

            fig5 = z.Loss_pie(pie_df=all_qttar_dict_list["Intraday"], symbol=None, width=width, height=height)
            st.plotly_chart(fig5, use_container_width=True, theme=None)
            metric_label(risk_dict=z.risk_management(risk_df=all_qttar_dict_list["Intraday"], symbol=None))

            dataframe_df3 = z.dataframe(dataframe_df=all_qttar_dict_list["Intraday"], symbol=None, width=width, height=height)
            showData = st.multiselect('Filter: ', dataframe_df3.columns, key=f'filter_{dataframe_df3}',
                                      default=z.dataframe_columns(list=dataframe_df3))
            st.dataframe(dataframe_df3[showData].round(2), use_container_width=False, width=1200, height=300)
            convert_df(df=dataframe_df3, file_name="MANOJ KUKNA.csv")
            st.line_chart(dataframe_df3, x='Entry_Date', y='cumsum', width=1200, height=300)

            # print("Intraday lin 297 ", time_())
        if app == 'Options':
            fig6 = z.Profit_pie(pie_df=all_qttar_dict_list["Options"], symbol=None, width=width, height=height)
            st.plotly_chart(fig6, use_container_width=True, theme=None)
            fig6 = z.Loss_pie(pie_df=all_qttar_dict_list["Options"], symbol=None, width=width, height=height)
            st.plotly_chart(fig6, use_container_width=True, theme=None)
            metric_label(risk_dict=z.risk_management(risk_df=all_qttar_dict_list["Options"], symbol=None))

            dataframe_df4 = z.dataframe(dataframe_df=all_qttar_dict_list["Options"], symbol=None, width=width, height=height)
            showData = st.multiselect('Filter: ', dataframe_df4.columns, key=f'filter_{dataframe_df4}',
                                      default=z.dataframe_columns(list=dataframe_df4))
            st.dataframe(dataframe_df4[showData].round(2), use_container_width=False, width=1200, height=300)
            convert_df(df=dataframe_df4, file_name="MANOJ KUKNA.csv")
            st.line_chart(dataframe_df4.round(2), x='Entry_Date', y='cumsum', width=1200, height=300)
            # print("Options lin 311 ", time_())
        if app == 'Charges':
            Charges_pie(pie_df=all_qttar_dict_list["Charges"], width=width, height=height)

            # print("Charges lin 315 ", time_())
        if app == 'Charges Debits and Credits':
            Charges_Debits_and_Credits_pie(pie_df=all_qttar_dict_list["Charges_credits_debits"], width=width, height=height)

        if app == 'Dividends':
            Dividends_pie(pie_df=all_qttar_dict_list["Dividends"], width=width, height=height)

            # print("Dividends lin 322 ", time_())

run(all_qttar_dict=all_qttar_dict)

#
# print("lin 327 ", time_())
#





#  stock market journal  STOCK MARET JOURNAL        Z AI TECHNOLOGY     manojkukna/JANRAL_ZERODHA
#   STOCK MARKET JANRAL
# streamlit run streamlit_multiple_home_14_12_2023.py




    # icons  download      https: // icons.getbootstrap.com /  # icons     'person-circle'
#      pip install streamlit
#      pip install plotly
#      pip install streamlit-extras
#      pip install openpyxl

# python varjan 3.8   up
# Generate the requirements.txt File
# pip freeze > requirements.txt