__author__ = 'asagli'

from django.conf.urls import patterns, url
from formexample.views import *

# Blog patterns.
urlpatterns = patterns("example.views",
    url("^pycicu-freecrop/$" , freeCropView, name="pycicuExample"),
    url("^pycicu-fixedratio/$" , fixedRatioView, name="pycicuExample"),
    url("^pycicu-warningsize/$" , warningSizeView, name="pycicuExample"),
)
