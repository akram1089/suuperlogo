from django.contrib import admin
from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve 
urlpatterns = [
    path('',views.home,name="home"),
    path('features',views.features,name="features"),
    path('use_cases_strategy',views.use_cases_strategy,name="use_cases_strategy"),
    path('use_cases_invester',views.use_cases_invester,name="use_cases_invester"),
    path('Open_interest_analysis', views.Open_interest_analysis, name='Open_interest_analysis'),
    path('Strategy_builder_straddle', views.Strategy_builder_straddle, name='Strategy_builder_straddle'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('help_support', views.help_support, name='help_support'),
    path('learning_center', views.learning_center, name='learning_center'),
    path('blog', views.blog, name='blog'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('signUp', views.signUp, name='signUp'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_pass/<token>/',views.change_pass,name='change_pass'),
    path('get_option_chain/',views.get_option_chain,name='get_option_chain'),
    path('Algo_market_place',views.Algo_market_place,name='Algo_market_place'),
    path('my_strategies',views.my_strategies,name='my_strategies'),
    path('my_portfolio',views.my_portfolio,name='my_portfolio'),
    path('broking_details',views.broking_details,name='broking_details'),
    path('chart_topgainer',views.chart_topgainer,name='chart_topgainer'),
    path('Futures_Buildup',views.Futures_Buildup,name='Futures_Buildup'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('base',views.base,name='base'),
    path('option_strategies',views.option_strategies,name='option_strategies'),
    path('strategy_builder',views.strategy_builder,name='strategy_builder'),
    path('market_glance',views.market_glance,name='market_glance'),
    path('financial_result',views.financial_result,name='financial_result'),
    path('reports',views.reports,name='reports'),
    path('stock_scanner',views.stock_scanner,name='stock_scanner'),
    path('rocket_call',views.rocket_call,name='rocket_call'),
    path('holiday',views.holiday,name='holiday'),
    path('lot_size',views.lot_size,name='lot_size'),
    path('market_heavy',views.market_heavy,name='market_heavy'),
    path('bulk_deal_data',views.bulk_deal_data,name='bulk_deal_data'),
    path('bulk_deal_data_page',views.bulk_deal_data_page,name='bulk_deal_data_page'),
    
 
    path('courses_details',views.courses_details,name='courses_details'),
    path('market_wide_position',views.market_wide_position,name='market_wide_position'),
    path('dii_fii',views.dii_fii,name='dii_fii'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)