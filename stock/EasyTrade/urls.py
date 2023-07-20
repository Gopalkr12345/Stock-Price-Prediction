from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('prices/', views.prices, name="prices"),
    # path('prediction/', views.prediction, name="prediction"),
    path('desc/', views.desc, name="desc"),
    path('desc2/', views.desc2, name="desc2"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('add_stock.html', views.delete_stock, name="delete_stock"),

    path('index_learn/', views.index_learn, name="index_learn"),
    path('news/', views.news, name="news"),
    path('intro_stock_market/', views.intro_stock_market,
         name="intro_stock_market"),
    path('fundamental_analysis/', views.fundamental_analysis,
         name="fundamental_analysi"),
    path('technical_analysis/', views.technical_analysis,
         name="technical_analysis"),
    path('the_need_to_invest/', views.the_need_to_invest,
         name="the_need_to_invest"),
    path('regulators/', views.regulators, name="regulators"),
    path('ipo_market/', views.ipo_market, name="ipo_market"),
    path('the_stock_markets/', views.the_stock_markets, name="the_stock_markets"),
    path('jargons/', views.jargons, name="jargons"),
    path('clearing_and_settlement/', views.clearing_and_settlement,
         name="clearing_and_settlement"),
    path('corporate_actions/', views.corporate_actions, name="corporate_actions"),
    path('intro_fund_analy/', views.intro_fund_analy, name="intro_fund_analy"),
    path('mindset_investor/', views.mindset_investor, name="mindset_investor"),
    path('read_annual_report/', views.read_annual_report,
         name="read_annual_report"),
    path('understanding_p_l_1/', views.understanding_p_l_1,
         name="understanding_p_l_1"),
    path('understanding_p_l_2/', views.understanding_p_l_2,
         name="understanding_p_l_2"),
    path('understanding_bal_sheet_1/', views.understanding_bal_sheet_1,
         name="understanding_bal_sheet_1"),
    path('understanding_bal_sheet_2/', views.understanding_bal_sheet_2,
         name="understanding_bal_sheet_2"),
    path('cashflow_statement/', views.cashflow_statement,
         name="cashflow_statement"),
    path('background/', views.background, name="background"),
    path('introducing_tech_analysis/', views.introducing_tech_analysis,
         name="introducing_tech_analysis"),
    path('chart_types/', views.chart_types, name="chart_types"),
    path('getting_started_candlesticks/', views.getting_started_candlesticks,
         name="getting_started_candlesticks"),
    path('single_cad_patterns_part1/', views.single_cad_patterns_part1,
         name="single_cad_patterns_part1"),
    path('single_cad_patterns_part2/', views.single_cad_patterns_part2,
         name="single_cad_patterns_part2"),
    path('single_cad_patterns_part3/', views.single_cad_patterns_part3,
         name="single_cad_patterns_part3"),
    path('support_resistance/', views.support_resistance,
         name="support_resistance"),
    path('volumes/', views.volumes, name="volumes"),
    path('moving_averages/', views.moving_averages, name="moving_averages"),
    path('indicators/', views.indicators, name="indicators"),
    path('dow_theory_1/', views.dow_theory_1, name="dow_theory_1"),
    path('dow_theory2/', views.dow_theory2, name="dow_theory2"),
    path('signup', views.handelSignup, name="handelSignup"),
    path('login', views.handelLogin, name="handelLogin"),
    path('logout', views.handelLogout, name="handelLogout"),
]
