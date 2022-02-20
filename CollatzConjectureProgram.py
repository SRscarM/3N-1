'''
Name: Sourav
Class: 9th A
Date: 17/12/21
'''
#importing modules
import matplotlib.pyplot as plt
from matplotlib import style

#variables
mainLoop = True
secondLoop = True
maxHeight = 0
maxSteps = 1

#the value of y,x axis
numberList = []
stepsList = []

#styling the chart
plt.style.use('seaborn-darkgrid')
plt.figure(facecolor='#ffebf1')

fontdict = {'fontname': 'Adobe Heiti Std' , 'fontsize': 20, 'color': "#D42CB8"}
subfontdict = {'fontname': 'Adobe Heiti Std' , 'fontsize': 10, 'color': "#CA3EEB"}

fig = plt.gcf()
fig.canvas.manager.set_window_title('3N + 1 Chart Window')

plt.title("The Value Chart",  fontdict )
plt.xlabel("Number Of Steps",  subfontdict)
plt.ylabel("Value of Number" ,  subfontdict)
plt.grid(True, color = "grey", linewidth = "0.5", linestyle = "--")

#the main loop
while mainLoop:
    
    #the try function so that there is no errors
    try:
        num = int(input("Please  Any Positive Integer: "))
        testValue = num
        stepsList.append(maxSteps)
        numberList.append(num)
    
        while secondLoop:
            if (num%2) == 0:
                num = num/2
                print("n = ",num)
                maxSteps += 1
                stepsList.append(maxSteps)
                numberList.append(num)
                if num == 1:
                    break

            if (num%2) != 0:
                num = (num*3)+1
                print("n = ",num)
                maxSteps += 1
                stepsList.append(maxSteps)
                numberList.append(num)
                if num == 1:
                    break

        maxHeight = max(numberList)
        print("the Max number of steps = ",maxSteps )
        print("the Max number it reached = ",maxHeight)
        
        #showing the plot
        plt.plot(stepsList, numberList,
                 marker = 'o',
                 markersize = 2.5,
                 markerfacecolor = '#872CD4',
                 linewidth = 1.2, color = '#6834F6')
        
        plt.show()
        
        #resetting the values
        maxSteps = 1
        maxHeight= 0
        numberList.clear()
        stepsList.clear()

    except ValueError:
        print("NOTE: YOU CANT ENTER A NUMBER!!", "\n")
    
