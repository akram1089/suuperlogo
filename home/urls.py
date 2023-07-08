from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
urlpatterns = [
    path('', views.home, name="home"),
    path('features', views.features, name="features"),
    path('use_cases_strategy', views.use_cases_strategy, name="use_cases_strategy"),
    path('use_cases_invester', views.use_cases_invester, name="use_cases_invester"),
    path('Open_interest_analysis', views.Open_interest_analysis,
         name='Open_interest_analysis'),
    path('Strategy_builder_straddle', views.Strategy_builder_straddle,
         name='Strategy_builder_straddle'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('help_support', views.help_support, name='help_support'),
    path('learning_center', views.learning_center, name='learning_center'),
    path('blog', views.blog, name='blog'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('signUp', views.signUp, name='signUp'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_pass/<token>/', views.change_pass, name='change_pass'),
    path('get_option_chain/', views.get_option_chain, name='get_option_chain'),
    path('Algo_market_place', views.Algo_market_place, name='Algo_market_place'),
    path('my_strategies', views.my_strategies, name='my_strategies'),
    path('my_portfolio', views.my_portfolio, name='my_portfolio'),
    path('broking_details', views.broking_details, name='broking_details'),
    path('chart_topgainer', views.chart_topgainer, name='chart_topgainer'),
    path('Futures_Buildup', views.Futures_Buildup, name='Futures_Buildup'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('base', views.base, name='base'),
    path('option_strategies', views.option_strategies, name='option_strategies'),
    path('strategy_builder', views.strategy_builder, name='strategy_builder'),
    path('market_glance', views.market_glance, name='market_glance'),
    path('financial_result', views.financial_result, name='financial_result'),
    path('reports', views.reports, name='reports'),
    path('stock_scanner', views.stock_scanner, name='stock_scanner'),
    path('rocket_call', views.rocket_call, name='rocket_call'),
    path('holiday', views.holiday, name='holiday'),
    path('lot_size', views.lot_size, name='lot_size'),
    path('market_heavy', views.market_heavy, name='market_heavy'),
    path('bulk_deal_data', views.bulk_deal_data, name='bulk_deal_data'),
    path('bulk_deal_data_page', views.bulk_deal_data_page,
         name='bulk_deal_data_page'),
    path('dashboard1', views.dashboard1, name='dashboard1'),
    path('base_dashboard1', views.base_dashboard1, name='base_dashboard1'),
    path('global_market', views.global_market, name='global_market'),
    path('market_actions', views.market_actions, name='market_actions'),
    path('ban_list_dashboard', views.ban_list_dashboard, name='ban_list_dashboard'),
    # path('stock-listing/', views.stock_listing, name='stock_listing'),
    path('delete_user/<str:id>', views.delete_user, name='delete_user'),
    path('manage_user', views.manage_user, name='manage_user'),
    path('admin_reset', views.admin_reset, name='admin_reset'),
    path('admin_signup', views.admin_signup, name='admin_signup'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('courses_details', views.courses_details, name='courses_details'),
    path('market_wide_position', views.market_wide_position,
         name='market_wide_position'),
    path('dii_fii', views.dii_fii, name='dii_fii'),
    path('stock_analysis', views.stock_analysis, name='stock_analysis'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

    path('put_call_ratio_chart', views.put_call_ratio_chart,
         name='put_call_ratio_chart'),

    path('filtered_oi_data', views.filtered_oi_data, name='filtered_oi_data'),
    path('filtered_oi_change_data', views.filtered_oi_change_data,
         name='filtered_oi_change_data'),
    path('scale_stacking_chart', views.scale_stacking_chart,
         name='scale_stacking_chart'),
    path('pcr_volume', views.pcr_volume, name='pcr_volume'),

    path('Edit_user_data/<str:id>', views.Edit_user_data, name='Edit_user_data'),

    path('volume-shocker/', views.volume_shocker, name='volume_shocker'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('put_call_ratio', views.put_call_ratio, name='put_call_ratio'),
    path('feedback_management', views.feedback_management,
         name='feedback_management'),
    path('payments_details', views.payments_details, name='payments_details'),


    path('oi_gainers', views.oi_gainers, name='oi_gainers'),
    path('oi_losers', views.oi_losers, name='oi_losers'),
    path('dii_fii', views.dii_fii, name='dii_fii'),

    path('performance_data', views.performance_chart, name='performance_chart'),
    path('nifty_tracker', views.nifty_tracker, name='nifty_tracker'),
    path('get_52_week_data', views.get_52_week_data, name='get_52_week_data'),
    path('get_52_week_low_data', views.get_52_week_low_data,
         name='get_52_week_low_data'),
    path('only_buyers', views.only_buyers, name='only_buyers'),
    path('get_data_buildup/', views.get_data_buildup, name='get_data_buildup'),
    path('watch_list', views.watch_list, name='watch_list'),
    path('port_folio_management', views.port_folio_management,
         name='port_folio_management'),
    path('options_simulator', views.options_simulator, name='options_simulator'),
    path('new_options_data', views.new_options_data, name='new_options_data'),
    path('admin_report', views.admin_report, name='admin_report'),
    path('feedback', views.feedback, name='feedback'),
    path('stock_list', views.stock_list, name='stock_list'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
