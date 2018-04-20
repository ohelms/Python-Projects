# This program is a simple simulation of the Lunar Module from the Appollo space program on the moon. The simulation starts when the retrorockets cut off and you take control of the Lunar Module. You will have all of the initial parameters at your control.

# While the Lunar Module is in free-fall towards the moon, your goal is to control the rate of descent using the thrusters. This is done by entering integer values from 0 to 9 which represent the fuel consumption. A value of 5 maintains the current velocity, 0 is free-fall and 9 creates maximum thrust. All other values will control the descent in a similar way that is associated with the scale. 

# To reflect reality, you will also have a limited supply of fuel. If you run out of fuel before landing, the Lunar Module will start freefalling to the ground.

# If you land on the moon with a velocity between 0 and -1 meters per second you will survive the landing and likely return home safely. A landing velocity between -1 and -10 meters per second means that you will survive the landing, but will be unable to leave the Moon due to critical damage to the Lunar Module. Finally, velocities of less than -10 meters per second will result in a crash and instant death.




import math
def main():

    
    
    #Initiallizes 
    showWelcome()
    elapsedTime = 0
    altitude = (getAltitude())
    velocity = 0
    fuelAmount = (getFuel())
    fuelRate = 0
    currentFuel = fuelAmount
    print ("\nLM state at retrorocket cutoff")
    displayLMState(elapsedTime,altitude,velocity,fuelAmount,fuelRate)


    
    #fuelRate               =askfor input
    #currentFuel            =currentfuel-fuelrate
    #acceleration           =gravity(1.62)*((fuelrate/5)-1)
    #velocity               =velocity+acceleration
    #altitude               =altitude+velocity+(acceleration/2)
    #elapsedTime            =elapsedtime+1

    
    
    #Flight parameters
    while 0 < altitude:
        gravity = (float(1.62))
        fuelRate = (getFuelRate(currentFuel))
        currentFuel = (updateFuel(currentFuel,fuelRate))
        acceleration = updateAcceleration(gravity,fuelRate)
        altitude = updateAltitude(altitude,velocity,acceleration)
        velocity = updateVelocity(velocity,acceleration)
        elapsedTime = elapsedTime + 1
        displayLMState(elapsedTime,altitude,velocity,currentFuel,fuelRate)
    else:
        displayLMLandingStatus(velocity)

        

#Displays welcome message
def showWelcome():
    print ("\nWelcome aboard the Lunar Module Flight Simulator\n"
    "\n   To begin you must specify the LM\'s initial altitude\n"
    "   and fuel level. To simulate the actual LM use\n"
    "   values of 1300 meters and 500 liters, respectively.\n"
    "\n   Good luck and may the force be with you!\n")



#Requests user input for integer value between 1 and 9999 inclusive
def getAltitude():
    altitude = int(input("Enter the initial altitude of the LM (in meters): "))
    while (altitude < 1 or 9999 < altitude):
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
        altitude = int(input("Enter the initial altitude of the LM (in meters): "))
    return altitude



#Requests user input for a positive integer value
def getFuel():
    fuelAmount = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while (fuelAmount <= 0):
        print ('ERROR: Amount of fuel must be positive, please try again')
        fuelAmount = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    return fuelAmount



#Displays the status of the Lunar Module at each stage of flight
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    if fuelAmount == 0 and 0 < altitude:
        print ("OUT OF FUEL - Elapsed Time:{0:4}".format(int(elapsedTime)), "Altitude:{0:8.2f}".format(float(altitude)), "Velocity:{0:8.2f}".format(float(velocity)))
    elif altitude == 0:
        print ("\nLM state at landing/impact")
        print ("Elapsed Time:{0:5}".format(int(elapsedTime)),'s')
        print ("        Fuel:{0:5}".format(int(fuelAmount)),'l')
        print ("        Rate:{0:5}".format(int(fuelRate)),'l/s')
        print ("    Altitude:{0:8.2f}".format(float(altitude)),'m')
        print ("    Velocity:{0:8.2f}".format(float(velocity)),'m/s\n')
    else:
        print ("Elapsed Time:{0:5}".format(int(elapsedTime)),'s')
        print ("        Fuel:{0:5}".format(int(fuelAmount)),'l')
        print ("        Rate:{0:5}".format(int(fuelRate)),'l/s')
        print ("    Altitude:{0:8.2f}".format(float(altitude)),'m')
        print ("    Velocity:{0:8.2f}".format(float(velocity)),'m/s\n')
    return " "


#Current amount of fuel in the Lunar Module
def getFuelRate(currentFuel):
    if currentFuel <= 0:
        fuelRate = 0
    else:
        fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
        if (currentFuel <= fuelRate) and ((0 <= fuelRate and fuelRate <= 9)):
            fuelRate=currentFuel
        else:
            while (fuelRate < 0 or 9 < fuelRate):
                print ('ERROR: Fuel rate must be between 0 and 9, inclusive\n')
                fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    return fuelRate


#Calculates acceleration from fuel usage and gravity
def updateAcceleration(gravity, fuelRate):
    acceleration = gravity * ((fuelRate / 5) - 1)
    return acceleration



#Returns new altitude based on altitude, velocity and acceleration
def updateAltitude(altitude, velocity, acceleration):
    altitude = altitude + velocity + (acceleration / 2)
    if altitude < 0:
        altitude = 0
    return altitude


#Returns new velocity based on current acceleration
def updateVelocity(velocity, acceleration):
    velocity = velocity + acceleration
    return float(velocity)


#Calculates the new value for remaining fuel
def updateFuel(fuel, fuelRate):
    currentFuel = fuel - fuelRate
    return currentFuel


#Displays the status of the Lunar Module if it lands
def displayLMLandingStatus(velocity):
    if velocity >= -1 and 0 >= velocity:
        print("Status at landing - The eagle has landed!")
    elif velocity > -10 and -1 > velocity:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif velocity <= -10:
        print("Status at landing - Ouch - that hurt!")
        return ""


if __name__ == "__main__":
    main()