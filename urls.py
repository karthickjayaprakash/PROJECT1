from django.urls import path
from . import views

urlpatterns=[
path("",views.basic,name="basic"),
path("fo/",views.fo,name="fo"),
path("result/",views.result,name="result"),
path("comment/",views.comment,name="comment"),
path("comment/add_comment/",views.add_comment,name="add_comment"),
#path("result/food/",views.fooddetailview,name="fooddetailview"),
#path("result/food/food/",views.fooddetailview,name="fooddetailview"),
#path("result/food/food/food/",views.fooddetailview,name="fooddetailview"),
#path("result/paleo/",views.paleodetailview,name="paleodetailview"),
#path("result/paleo/paleo/",views.paleodetailview,name="paleodetailview"),
#path("result/paleo/paleo/paleo/",views.paleodetailview,name="paleodetailview"),
#path("result/vegetarian/",views.vegetariandetailview,name="vegetariandetailview"),
#path("result/vegetarian/vegetarian/",views.vegetariandetailview,name="vegetariandetailview"),
#path("result/vegetarian/vegetarian/vegetarian/",views.vegetariandetailview,name="vegetariandetailview"),
#path("result/vegan/",views.vegandetailview,name="vegandetailview"),
#path("result/vegan/vegan/",views.vegandetailview,name="veganndetailview"),
#path("result/vegan/vegan/vegan/",views.vegandetailview,name="vegandetailview"),
path("scheme",views.schemeselection,name="schemeselection"),
path("result/scheme/",views.schemeselection,name="schemeselection"),
path("result/scheme/scheme/",views.schemeselection,name="schemeselection"),
path("result/scheme/scheme/scheme/",views.schemeselection,name="schemeselection"),
path("register/",views.register,name="register"),
path("login/",views.login,name="login"),
path('pybot/',views.pybot,name='pybot'),
path('callcalcal/',views.callcalcal,name="calcal"),
path('callcalcal/calcalculated/',views.calcal,name="calculatedcalcal"),

path("testdropdown/",views.test,name="dropdown"),
path("testdropdown/ama",views.okay,name="ama"),

]