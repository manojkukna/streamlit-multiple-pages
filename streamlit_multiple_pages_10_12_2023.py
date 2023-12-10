import streamlit as st  # streamlit pip install
import pandas as pd
import plotly.express as px       #                             pip install plotly
import copy
from streamlit_option_menu import option_menu     # pip install streamlit-option-menu
import ZERODH_TAXPNL_Options__Holding_9_12_2023 as z

Holding = pd.DataFrame(z.all_qttar_dict["Holding"])
Options = pd.DataFrame(z.all_qttar_dict["Options"])
Charges = pd.DataFrame(z.all_qttar_dict["Charges"])
Intraday = pd.DataFrame(z.all_qttar_dict["Intraday"])
Charges_credits_debits = pd.DataFrame(z.all_qttar_dict["Charges_credits_debits"])

def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Home','your uploaded_file', 'Holding', 'Intraday', 'Options','Charges','Charges Debits and Credits', 'about'],
                #           https: // icons.getbootstrap.com /  # icons     'person-circle'

                icons=['house-fill','person-bounding-box','journal-arrow-up' , 'trophy-fill', 'apple', 'play-btn-fill','caret-right-square-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={"container": {"padding": "5!important", "background-color": 'black'},
                        "icon": {"color": "white", "font-size": "23px"},
                        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                     "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#02ab21"}, })
        if app == "Home":
            z.uploaded_file()
            df = z.Equity_Options_BOKREJ_pie(pie_df=z.Equity_Options_BOKREJ(Holding=Holding, Intraday=Intraday,
                                    Options=Options, Charges=Charges,Charges_credits_debits=Charges_credits_debits), symbol=None)
            z.dataframe(dataframe_df= df, default=z.dataframe_columns(list= df), symbol=None)
        if app == 'your uploaded_file':
            st.image("image\\zhrodh.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("image\\tax_pnl1.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("image\\reports.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("image\\download.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")
            st.image("image\\uploaded.png",
                     caption="Developed and Maintaned by: KUKAN MANOJ                          :      MO ->8000594016")

            z.uploaded_file()
        if app == 'Holding':
            z.metric_label(risk_dict=z.risk_management(risk_df=Holding, symbol=None))
            z.Profit_pie(pie_df=Holding.round(2), symbol=None)
            z.Loss_pie(pie_df=Holding.round(2), symbol=None)
            z.dataframe(dataframe_df=Holding, default=z.dataframe_columns(list=Holding), symbol=None)
        if app == 'Intraday':
            z.metric_label(risk_dict=z.risk_management(risk_df=Intraday, symbol=None))
            z.Profit_pie(pie_df=Intraday.round(2), symbol=None)
            z.Loss_pie(pie_df=Intraday.round(2), symbol=None)
            z.dataframe(dataframe_df=Intraday, default=z.dataframe_columns(list=Intraday), symbol=None)
        if app == 'Options':
            z.metric_label(risk_dict=z.risk_management(risk_df=Options, symbol=None))
            z.Profit_pie(pie_df=Options.round(2), symbol=None)
            z.Loss_pie(pie_df=Options.round(2), symbol=None)
            z.dataframe(dataframe_df=Options, default=z.dataframe_columns(list=Options), symbol=None)
        if app == 'Charges':
            z.Charges_pie(pie_df=Charges)
        if app == 'Charges Debits and Credits':
            z.Charges_Debits_and_Credits_pie(pie_df=Charges_credits_debits)


run()

# janral zorhodh
#  JANRAL ZERODHA
#                streamlit run streamlit_multiple_pages_10_12_2023.py