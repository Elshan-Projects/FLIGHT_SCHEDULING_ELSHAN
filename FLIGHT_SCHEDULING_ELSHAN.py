import math

cities = [("Berlin",4),("New York",13),("Boston",13),("Istanbul",3),
          ("Moscow",3),("Vienna",5),("Zagreb",6),("Rome",7),("Pekin",10)]
n_a=8
n_c=len(cities)
time_in_days = 7 

print("CITIES:")
for wwww in range(len(cities)):
    print(cities[wwww])
print('\n')

print("NUMBER OF PLANES:")
print(n_a)
print('\n')

def time_converter(tH):
    days = int(tH//24)
    hours = math.floor(tH-days*24)
    minutes = math.floor( ( tH-math.floor(tH) )*60 ) 
    result = str(days)+":"+str(hours)+":"+str(minutes)
    return result



def schedule(n_a,n_c,time_in_days,cities):
    duration = []
    for i in range(len(cities)):
        duration.append(cities[i][1])

    city_str = sorted(cities, key=lambda tup: tup[1])


    cl = []
    for ii in range(len(city_str)):
        cl.append(city_str[ii][0])
    
    ds = sorted(duration)
    th = time_in_days*24
    records=[]
    stage = 0
    x=1
    y=2
    for  j in range(n_c):

        for jj in range(n_a):
            records.append( (j, jj, x, stage+jj*0.25, stage+jj*0.25+ds[j], y, stage+jj*0.25+2*ds[j]) )
            if(records[-1][-1]>=th):
                print("The program was unable to finish in the given time period")
                break
        stage=records[-1][-1]
        x, y = y, x

    table = []
    for m in range(len(records)):
        table.append(( 
            cl[ records[m][0] ], 
            "Plane_"+str( records[m][1] ), 
            " Landed at "+str(records[m][2]), 
            " Leaves at "+time_converter( records[m][3] ), 
            " Arrives at "+time_converter( records[m][4] ) ,
            " Landed at "+str(records[m][5]), 
            " Returns at "+time_converter( records[m][6] ) 
            ))
        
    return table

final_result = schedule(n_a, n_c, time_in_days, cities)

for b in range(len(final_result)):
    print(final_result[b])
    if ( ((b+1)%n_a)==0 ):
        print("\n")
