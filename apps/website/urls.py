from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('aero-space-services/', views.AeroSpaceServicesView.as_view(), name='aero_space_services'),
    path('automative-system/', views.AutomativeSystemView.as_view(), name='automative_system'),
    path('blog-large-image/', views.BlogLargeImageView.as_view(), name='blog_large_image'),
    path('blog-single/', views.BlogSingleView.as_view(), name='blog_single'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('contact-2/', views.Contact2View.as_view(), name='contact_2'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faqs/', views.FaqsView.as_view(), name='faqs'),
    path('', views.IndexView.as_view(), name='index'),
    path('index2/', views.Index2View.as_view(), name='index2'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('market-sector-single/', views.MarketSectorSingleView.as_view(), name='market_sector_single'),
    path('market-sector/', views.MarketSectorView.as_view(), name='market_sector'),
    path('power-and-energy/', views.PowerAndEnergyView.as_view(), name='power_and_energy'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('projects-modern/', views.ProjectsModernView.as_view(), name='projects_modern'),
    path('projects-single/', views.ProjectsSingleView.as_view(), name='projects_single'),
    path('projects-with-filter/', views.ProjectsWithFilterView.as_view(), name='projects_with_filter'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('railway-infrastructure/', views.RailwayInfrastructureView.as_view(), name='railway_infrastructure'),
    path('ship-building-industry/', views.ShipBuildingIndustryView.as_view(), name='ship_building_industry'),
    path('shop-single/', views.ShopSingleView.as_view(), name='shop_single'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shoping-cart/', views.ShopingCartView.as_view(), name='shoping_cart'),
    path('testimonial/', views.TestimonialView.as_view(), name='testimonial'),
]
