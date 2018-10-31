#imports
from System.IO import StreamWriter, FileMode
from Spotfire.Dxp.Application.Visuals import CrossTablePlot
from  Spotfire.Dxp.Data.Export import DataWriterTypeIdentifiers
import tempfile
import os

#create a temporary 

tmp = os.path.join(tempfile.gettempdir(), "forecast_input.csv")
stream = StreamWriter(tmp)


#export the cross table
crossTable.As[CrossTablePlot]().ExportText(stream)
stream.Close()

f = open(tmp,'r')

csv = ""

month_map = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

lines = f.readlines()

header = lines[0].split("\t")

if len(header) == 4:
	for line in lines:
	    print(line)
	    row = line.split("\t")
	    if "Month" in (row):
	        continue
	    date = "-".join([row[0], month_map[row[2]], "01"])
	    value = row[3]
	    csv += ",".join([date,value]) + "\n"
if len(header) == 5:
    for line in f.readlines():
	    row = line.split("\t")
	
	    if "Month" in (row):
	        continue
	    date = "-".join([row[0], month_map[row[2]], row[3]])
	    value = row[4]
	    csv += ",".join([date,value]) + "\n"
	 


Document.Properties["forecastInput"] = csv
print(csv)