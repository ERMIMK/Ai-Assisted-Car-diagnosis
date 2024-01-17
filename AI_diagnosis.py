import openai
from Car_Information.Car_info import CarInfo
from DecisionTree.DecisionTree import DecisionNode



"""
THIS CLASS PREDICTS POTENTIAL PROBLEM OF THE CAR
"""
class CarPredictor:

    def __init__(self, api_key,):
        self.api_key = api_key

    def format_decision_list(self, decision_list, car_detail):
        # The function foramt_decision_list format the data to understandable OPENAI model txt
        car_detail_text = (f"Car Manufacturer: {car_detail[0]}\n"
                           f"Car Model: {car_detail[1]}\n"
                           f"Car Year: {car_detail[2]}\n")
        formatted_text = f"Diagnosing car issues:\n{car_detail_text}"
        for decision in decision_list:
            for question, answer in decision.items():
                formatted_text += f"Q: {question}\nA: {answer}\n"
        return formatted_text       #Return string value

    def predict_car_problem(self, decision_list, car_info):
        # function to predict car_problem by feeding the OPEN AI - text-davinci-003 model
        formatted_text = self.format_decision_list(decision_list, car_info)

        openai.api_key = self.api_key

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=formatted_text + "What could be the problem with the car based on the above responses? give me atleast 3 potential problem and short solutions of each potential problem using this format what the potential problem : Solutions and have nice spaing between since it's dirctly displayed on terminal",
            max_tokens=100
        )

        return response['choices'][0]['text'].strip()  #Return string value
    
    def get_valid_obd_code(self):
        while True:
            code = input("Enter the OBD code (e.g., P1234): ").upper()
            if len(code) == 5 and code[0] in ['P', 'C', 'B', 'U'] and code[1:].isdigit():
                return code
            else:
                print("Invalid code format. Please try again.")

    def format_obd_code(self, car_detail):
        read_code = self.get_valid_obd_code()
        car_detail_text = (f"Car Manufacturer: {car_detail[0]}\n"
                           f"Car Model: {car_detail[1]}\n"
                           f"Car Year: {car_detail[2]}\n")
        formatted_code  = (f"The car : {car_detail_text} is showing the following OBD Code {read_code} what could be the potential problem shortly with potential solution? response less than 100 words")
        return formatted_code
    
    def predict_code_problem(self, car_detail):
        # function to predict car_problem by feeding the OPEN AI - text-davinci-003 model
        formatted_text = self.format_obd_code(car_detail)

        openai.api_key = self.api_key

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=formatted_text, 
            max_tokens=100
        ) 

        return response['choices'][0]['text']


