class DecisionNode:
    # Customizable decision node

    def __init__(self):

        self.decision_node = {
            "start": {
                "prompt": "Does your car start (yes/no)? ",
                "yes": "check_noise",
                "no": "check_battery"
            },
            "check_noise": {
                "prompt": "Does your car make noise (yes/no)? ",
                "yes": "noise_type",
                "no": "dashboard_light"
            },
            "check_battery": {
                "prompt": "Is the battery plugged (yes/no)? ",
                "yes": "jump_start",
                "no": "complete"
            },
            "noise_type": {
                "prompt": "Is the noise rattling ? ",
                "yes": "",
                "no": "squealing_noise_check",
            },
            "squealing_noise_check": {
                "prompt": "Is the noise squealing ? ",
                "yes": "",
                "no": "knocking_noise_check"
            },
            "knocking_noise_check":  {
                "prompt": "Is is Knocking noise around the engine ?  ",
                "yes": "oil_check",
                "no": "other_noise"
            },
            "oil_check": {
                "prompt": "Is your oil changed or filled within the last 6 month ? ",
                "yes": "check_engine_light",
                "no": "oil_level_check"
            },
            "oil_level_check": {
                "prompt": "Is the oil level low or the oil color changed ? ",
                "yes": "complete",
                "no": ""

            },
            "complete": {
                "prompt": "Completed, wait for diagnosis ... "
            }
        }

    def run_diagnosis(self):
        decision_list = []
        current_status = "start"

        while True:
            prompt = self.decision_node[current_status]["prompt"]
            client_decision = input(prompt).lower()

            if client_decision in self.decision_node[current_status]:
                next_status = self.decision_node[current_status][client_decision]
                decision_list.append({prompt: client_decision})

                if next_status == "complete":
                    print(self.decision_node[next_status]["prompt"])
                    break
                else:
                    current_status = next_status
            else:
                print("Invalid input: please try again")

        return decision_list


