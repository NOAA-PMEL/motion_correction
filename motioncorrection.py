#!/usr/bin/env python
# coding: utf-8

import math
import pandas as pd

df = pd.DataFrame(oshen_data_raw)


def wind_correction(psm,pcm,wsm,wdm):
    uwnd = (-1)*wsm*math.sin(rad_deg*wdm)*mps_kt
    vwnd = (-1)*wsm*math.cos(rad_deg*wdm)*mps_kt
    wspd = wsm*mps_kt
    cu = psm*math.sin(rad_deg*pcm)*mps_kt
    cv = psm*math.cos(rad_deg*pcm)*mps_kt
    
    uwnd05m = uwnd + cu
    vwnd05m = vwnd + cv
    wsp05m = ((uwnd05m ** 2) + (vwnd05m ** 2)) ** 0.5
    wind_speed = wsp05m
    
    wdir05m = math.atan2((-1)*uwnd05m,(-1)*vwnd05m) / rad_deg
    if wdir05m < 0:
        wind_direction_from = wdir05m + 360
    else:
        wind_direction_from = wdir05m

    return wind_speed, wind_direction_from


pi = 4*math.atan(1)
mps_kt = 1852/(60*60)
rad_deg = pi/180

psm = df['platform_speed_wrt_ground_mean'][0]
pcm = df['platform_course_mean'][0]
wsm = df['wind_speed_mean'][0]
wdm = df['wind_from_direction_mean'][0]

wind_speed,wind_direction_from = wind_correction(psm,pcm,wsm,wdm)
