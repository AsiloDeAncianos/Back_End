from django.urls import path, include
from rest_framework import routers
from caambu import views

#api versioning
router = routers.DefaultRouter()

router.register(r'benefactor', views.BenefactorView, 'benefactor')
router.register(r'institucionasilo', views.InstitucionAsiloView, 'institucionasilo')    
router.register(r'campania', views.CampaniaView, 'campania')    
router.register(r'donacion', views.DonacionView, 'donacion')    
router.register(r'gestor', views.GestorView, 'gestor')  
router.register(r'recojosprogramados', views.RecojosProgramadosView, 'recojosprogramados')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]