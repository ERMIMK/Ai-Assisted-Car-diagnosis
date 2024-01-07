from Car_Information.Car_info import CarInfo
from DecisionTree.DecisionTree import DecisionNode
from AI_diagnosis import CarPredictor

# OpenAi private API
my_api_key = "Your Open AI API key"
prediction = CarPredictor(my_api_key)

print("\n===========  WELCOME TO AI CAR DIAGNOIS BY ERMI M ============== \n")

while True:
    print("\n                PLEASE CHOOSE A SERVICE               ")
    print("                 1, AI Car Diagnosis                  ")
    print("                 2, Code Reader with Soultion         ")
    print("                 3, About the code                    ")
    print("                 4, Quit program                      ")

    user_main_choice = input("\n PLEASE ENTER YOUR INPUT : ")
    car_info = CarInfo('Car_Information/CarModelList.csv')

    # first service AI car Diagnosis
    if int(user_main_choice) == 1:
        print("\nLet's fix your car ... ")
        print("\n Tell us about your car \n")

        #collect user car information
        
        user_car_details = car_info.prompt()

        print(f"\nGreat! now let's inspect your {user_car_details[0].upper()} {user_car_details[1].upper()} {user_car_details[2]} car \n")

        # diagnosis user car
        diagnosis = DecisionNode()
        decision_list = diagnosis.run_diagnosis()

        #predict postential issues
        print("\nRunning diagnosis .... \n")
        predict = prediction.predict_car_problem(decision_list, user_car_details)

        print("="* 50)
        print(predict)
        print("="* 50 )
        
        continuity_prompt = input("\n Do you want to diagnose your car again? yes/no  :  ")
        if continuity_prompt.lower() != "yes": break
    
    elif int(user_main_choice) == 2:
        print("\n ===================================\n")
        user_car_details = car_info.prompt()
        print("\n ===================================\n")
        problem_prediction = prediction.predict_code_problem(user_car_details)
        print("\n Diagnosising code and looking for solution ... ")
        print(problem_prediction)

        continuity_prompt = input("\n Do you want to continue yes/no : ")
        if continuity_prompt.lower() != "yes": break


    elif int(user_main_choice) == 3:
        print("DESIGNED BY ERMI M ")
        continuity_prompt = input("\n Do you want to continue yes/no : ")
        if continuity_prompt.lower() != "yes": break
    
    elif int(user_main_choice) == 4: 
        exit()

    else:
        print("Please Enter valid input !! ")




