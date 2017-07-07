#!/opt/anaconda/bin/python


# In[1]:

import sys
import os, re
import csv
import datetime as dt
import numpy as np
import urllib2


# In[16]:

import bokeh.plotting as bk
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models import DatetimeTickFormatter, OpenURL, TapTool
from bokeh.models import HoverTool, BoxAnnotation, Span, Label, WheelZoomTool
from bokeh.palettes import Set1_8, Set2_8
from bokeh.models import Range1d
from bokeh.layouts import column

# In[3]:

import randomcolor
rand_color = randomcolor.RandomColor()
print(rand_color.generate())


# In[26]:

simuList = sys.argv[1]

tools1 = ["pan,resize,wheel_zoom,crosshair,hover,tap,reset,save"]

plot1 = figure(plot_width=1000, plot_height=600, x_axis_type="datetime", y_axis_type="datetime",
                min_border=10, tools=tools1, active_scroll="wheel_zoom", active_inspect="hover")

plot1.axis[0].formatter = DatetimeTickFormatter(years="%Y", months="%b-%y", days="%d-%b-%y", hours="%H:%M")
plot1.axis[1].formatter = DatetimeTickFormatter(years="%Y", months="%b-%y", days="%d-%b-%y", hours="%H:%M")

finput = file(simuList)

lineref = '# CumulPeriod | PeriodDateBegin |   PeriodDateEnd |        RunDateBegin |          RunDateEnd |     RealCpuTime |     UserCpuTime |      SysCpuTime | ExeDate'

nbfiles=0
for line in finput :
    
    color = rand_color.generate()[0]
    
    print '#==========================================='
    line = line.split(',')
    
    for i in range(1,len(line)):                           # config file allows definition like ....    , color="#FF0000"
        #print i, line[i].strip() 
        exec line[i].strip()

    fileruncard=line[0].strip()
    fileruncard=fileruncard.replace('/catalog', '/fileServer')
    arr=fileruncard.split('/')
    simuName = "/".join(arr[-5:])

    print 'color= ', color
    print 'simuName= ', simuName
    print 'file= ', fileruncard

    try:
            f=urllib2.urlopen(fileruncard + '/MONITORING/run.card')
            csv_reader = csv.reader(f)
            headerline = csv_reader.next()
            while headerline != [lineref] :           # read until find lineref
                headerline = csv_reader.next()
            # read an extra line
            headerline = csv_reader.next()

            nblines=0
            x,y = [],[]
            for line in csv_reader:
                a=line[0][1:]           # to remove first character=#
                part=a.split('|')
                PeriodDateBegin=dt.datetime.strptime(part[1].strip(),'%Y%m%d')
                CumulPeriod=int(part[0].strip())
                RunDateBegin=dt.datetime.strptime(part[3].strip(),'%Y-%m-%dT%H:%M:%S')
                RunDateEnd=dt.datetime.strptime(part[4].strip(),'%Y-%m-%dT%H:%M:%S')
                x.append(RunDateBegin)
                y.append(PeriodDateBegin)
                #y.append(CumulPeriod)
                nblines=nblines+1
                
            print '--> Read %d lines'%nblines
            if nblines < 10 :
                print '----> File skipped (not enough lines < 10)'
                continue
            
            source = ColumnDataSource(data=dict(x = x,
                                                y = y,
                                                simuName = [simuName for n in range(len(x))]
                                                ))
            
            plot1.line('x', 'y', source=source, line_alpha=1.0, line_join="round", line_color=color, line_width=3)
            
            nbfiles=nbfiles+1
                
    except:
        print "======> Error when reading run.card"
        continue

        
hover = plot1.select(dict(type=HoverTool))
hover.tooltips = [("Simulation", "@simuName")]
hover.mode = 'mouse'

url = "https://vesg.ipsl.upmc.fr/thredds/fileServer/work_thredds/@simuName/MONITORING/index.html"
taptool = plot1.select(type=TapTool)
taptool.callback = OpenURL(url=url)

plot1.title.text = "run.card analysis"
plot1.title.align = 'center'

plot1.xaxis.axis_label = 'Execution dates'
plot1.yaxis.axis_label = 'Simulation dates'
        

# In[5]:

output_file(sys.argv[2], title='run.card analysis')

save(plot1)


