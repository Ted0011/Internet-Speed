import csv
import speedtest


st = speedtest.Speedtest()

download_speed = st.download()
upload_speed = st.upload()

down = ' {:5.2f} Mb'.format(download_speed/(1024*1024) )
up = ' {:5.2f} Mb'.format(upload_speed/(1024*1024) )

with open ('D:\\activity3.csv','w+') as file:
    myfile = csv.writer(file)
    myfile.writerow(["S.N.","UPLOAD","DOWNLOAD"])
    number = int(input( "\n" + "Please enter the value you want to insert: " ))
    for i in range(number):

        
        anyt = str(i+1)
        myfile.writerow([anyt,up, down])
        print( "\n" + anyt + " th " + " Upload Speed is: " + up)
        print( anyt + " th " + " Download Speed is: " + down)
        if anyt != number:

            download_speed = st.download()
            upload_speed = st.upload()
            down = ' {:5.2f} Mb'.format(download_speed/(1024*1024) )
	    
            up = ' {:5.2f} Mb'.format(upload_speed/(1024*1024) )
        else:
            break          
            
            