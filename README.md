# Safe-navigator
####  

We daily come across women safety incidents, Safe Navigator is designed with sincere efforts to mitigate such incidents by showing the safest route between source and destination. 
Google maps provides the shortest route taking live traffic in consideration, but what about safety features? 
Safe Navigator considers travel time, traffic density to avoid secluded routes, number of nearby police stations, hospitals, fire station, toll gate , shops open during travel time falling on the route, past incidents etc falling on the route to ensure women safety. Also past accidents reported and route quality has been considered to avoid accident prone routes as well.
Say for instance, to reach KIA airport there are two routes one from toll gate and other is the one bypassing toll gate through deserted roads. Safe Navigator will give preference to the one with toll gate.
All features are extracted using Azure Route, Traffic and search API. Also map rendering is done using Azure maps
https://docs.microsoft.com/en-us/rest/api/maps/route
https://docs.microsoft.com/en-us/azure/azure-maps/map-route

Folder structure 

|   Controller.py
|   output.doc
|   README.md
|   ui.html
|   
+---.idea
|       .name
|       misc.xml
|       modules.xml
|       SafeNavigator.iml
|       workspace.xml
|      

Sample rest call to run:
http://192.168.4.76:8090/postjson?sourceLat=47.608013&sourceLong=-122.335167&destLat=47.673988&destLong=-122.121513
