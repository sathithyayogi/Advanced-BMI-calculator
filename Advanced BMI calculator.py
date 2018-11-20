Name = str(input("Enter your name:"))
Gender = int(input("Enter 1 for Female, 2 for Male and 3 for Others :"))
if Gender==1:
    Weight = float(input("Enter your real weight in Kg:"))
    print("Are you going to enter your height in Meter or Centi meter \n 1.Type 1 for the Cetimeter \n 2.Type 2 for the Meter")
    Unit = int(input("Waiting for your response type 1 or 2 :"))
    if Unit == 2:
        height_m1 =float(input("Enter your height:"))
        Bmi = Weight / height_m1**2
        if Bmi <= 15:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Very severely underweight.')

        elif Bmi  > 15 and Bmi < 16:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',you are Severely underweight.')

        elif Bmi > 16 and Bmi < 18.5:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Underweight.')

        elif Bmi > 18.5 and Bmi < 25:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Normal (healthy weight).')
        elif Bmi > 25 and Bmi < 30:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Overweight.')
        elif Bmi > 30 and Bmi < 35:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class I (Moderately obese).') 
        elif Bmi > 35 and Bmi < 40:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class II (Severely obese).')
        elif Bmi > 40 and Bmi < 45:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class III (Very severely obese).')
        elif Bmi > 45 and Bmi < 50:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class IV (Morbidly Obese).') 
        elif Bmi > 50 and Bmi < 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class V (Super Obese).') 
        elif Bmi > 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class VI (Hyper Obese).') 
        else:
            print('There is an error with your input')
            print('Please check you have entered value')
    elif Unit==1:
        height =float(input("Enter your height:"))
        height_m = height / 100 
        Bmi = Weight / height_m**2
        if Bmi <= 15:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Very severely underweight.')

        elif Bmi  > 15 and Bmi < 16:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Severely underweight.')

        elif Bmi > 16 and Bmi < 18.5:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Underweight.')

        elif Bmi > 18.5 and Bmi < 25:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Normal (healthy weight).')
        elif Bmi > 25 and Bmi < 30:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Overweight.')
        elif Bmi > 30 and Bmi < 35:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class I (Moderately obese).') 
        elif Bmi > 35 and Bmi < 40:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class II (Severely obese).')     
        elif Bmi > 40 and Bmi < 45:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class III (Very severely obese).')
        elif Bmi > 45 and Bmi < 50:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class IV (Morbidly Obese).') 
        elif Bmi > 50 and Bmi < 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class V (Super Obese).') 
        elif Bmi > 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class VI (Hyper Obese).') 
        else:
            print('There is an error with your input')
            print('Please check you have entered value')
    else:
        print("You have entered the " + Unit + "type only 1 or 2")
elif Gender ==2:
    Weight = float(input("Enter your real weight in Kg:"))
    print("Are you going to enter your height in Meter or Centi meter \n 1.Type 1 for the Cetimeter \n 2.Type 2 for the Meter")
    Unit = int(input("Waiting for your response type 1 or 2 :"))
    if Unit == 2:
        height_m1 =float(input("Enter your height:"))
        Bmi = Weight / height_m1**2
        if Bmi <= 15:
            print("Mr."+Name +" "+'your Bmi is', Bmi,'Very severely underweight.')

        elif Bmi  > 15 and Bmi < 16:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',you are Severely underweight.')

        elif Bmi > 16 and Bmi < 18.5:
            print("Mr."+Name +" "+'your Bmi is', Bmi,'Underweight.')

        elif Bmi > 18.5 and Bmi < 25:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Normal (healthy weight).')
        elif Bmi > 25 and Bmi < 30:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Overweight.')
        elif Bmi > 30 and Bmi < 35:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class I (Moderately obese).') 
        elif Bmi > 35 and Bmi < 40:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class II (Severely obese).')     
        elif Bmi > 40 and Bmi < 45:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class III (Very severely obese).')
        elif Bmi > 45 and Bmi < 50:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class IV (Morbidly Obese).') 
        elif Bmi > 50 and Bmi < 60:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class V (Super Obese).') 
        elif Bmi > 60:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class VI (Hyper Obese).') 
        else:
            print('There is an error with your input')
            print('Please check you have entered value')
    elif Unit==1:
        height =float(input("Enter your height:"))
        height_m = height / 100 
        Bmi = Weight / height_m**2
        if Bmi <= 15:
            print("Mr."+Name +" "+'your Bmi is', Bmi,'Very severely underweight.')

        elif Bmi  > 15 and Bmi < 16:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Severely underweight.')

        elif Bmi > 16 and Bmi < 18.5:
            print("Mr."+Name +" "+'your Bmi is', Bmi,'Underweight.')

        elif Bmi > 18.5 and Bmi < 25:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Normal (healthy weight).')
        elif Bmi > 25 and Bmi < 30:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Overweight.')
        elif Bmi > 30 and Bmi < 35:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class I (Moderately obese).') 
        elif Bmi > 35 and Bmi < 40:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class II (Severely obese).')     
        elif Bmi > 40 and Bmi < 45:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class III (Very severely obese).')
        elif Bmi > 45 and Bmi < 50:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class IV (Morbidly Obese).') 
        elif Bmi > 50 and Bmi < 60:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class V (Super Obese).') 
        elif Bmi > 60:
            print("Mr."+Name +" "+'your Bmi is', Bmi,',Obese Class VI (Hyper Obese).') 
        else:
            print('There is an error with your input')
            print('Please check you have entered value')
    else:
        print("You have entered the " + Unit + "type only 1 or 2")
elif Gender ==3:
    Weight = float(input("Enter your real weight in Kg:"))
    print("Are you going to enter your height in Meter or Centi meter \n 1.Type 1 for the Cetimeter \n 2.Type 2 for the Meter")
    Unit = int(input("Waiting for your response type 1 or 2 :"))
    if Unit == 2:
        height_m1 =float(input("Enter your height:"))
        Bmi = Weight / height_m1**2
        if Bmi <= 15:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Very severely underweight.')

        elif Bmi  > 15 and Bmi < 16:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',you are Severely underweight.')

        elif Bmi > 16 and Bmi < 18.5:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Underweight.')

        elif Bmi > 18.5 and Bmi < 25:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Normal (healthy weight).')
        elif Bmi > 25 and Bmi < 30:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Overweight.')
        elif Bmi > 30 and Bmi < 35:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class I (Moderately obese).') 
        elif Bmi > 35 and Bmi < 40:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class II (Severely obese).')     
        elif Bmi > 40 and Bmi < 45:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class III (Very severely obese).')
        elif Bmi > 45 and Bmi < 50:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class IV (Morbidly Obese).') 
        elif Bmi > 50 and Bmi < 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class V (Super Obese).') 
        elif Bmi > 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class VI (Hyper Obese).') 
        else:
            print('There is an error with your input')
            print('Please check you have entered value')
    elif Unit==1:
        height =float(input("Enter your height:"))
        height_m = height / 100 
        Bmi = Weight / height_m**2
        if Bmi <= 15:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Very severely underweight.')

        elif Bmi  > 15 and Bmi < 16:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Severely underweight.')

        elif Bmi > 16 and Bmi < 18.5:
            print("Ms."+Name +" "+'your Bmi is', Bmi,'Underweight.')

        elif Bmi > 18.5 and Bmi < 25:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Normal (healthy weight).')
        elif Bmi > 25 and Bmi < 30:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Overweight.')
        elif Bmi > 30 and Bmi < 35:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class I (Moderately obese).') 
        elif Bmi > 35 and Bmi < 40:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class II (Severely obese).')     
        elif Bmi > 40 and Bmi < 45:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class III (Very severely obese).')
        elif Bmi > 45 and Bmi < 50:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class IV (Morbidly Obese).') 
        elif Bmi > 50 and Bmi < 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class V (Super Obese).') 
        elif Bmi > 60:
            print("Ms."+Name +" "+'your Bmi is', Bmi,',Obese Class VI (Hyper Obese).') 
        else:
            print('There is an error with your input')
            print('Please check you have entered value')
    else:
        print("You have entered the " + Unit + "type only 1 or 2")
else:
    print("You have entered the " + Gender + "type only 1 or 2")