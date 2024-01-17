class DecisionNode:
    # Customizable decision node

    def __init__(self):

        self.decision_node = {
            "start": {
                "prompt": "Does your car start (yes/no)?",
                "yes": "check_noise",
                "no": "battery_terminal_check"
            },
            "check_noise": {
                "prompt": "Does your car make noise (yes/no)?",
                "yes": "noise_type",
                "no": "dashboard_light"
            },
            "check_battery": {
                "prompt": "Is the battery properly connected (yes/no)?",
                "yes": "jump_start",
                "no": "battery_replace"
            },
            "noise_type": {
                "prompt": "Is the noise a rattling sound?",
                "yes": "belt_check",
                "no": "squealing_noise_check",
            },
            "squealing_noise_check": {
                "prompt": "Is the noise a squealing sound?",
                "yes": "belt_condition_check",
                "no": "knocking_noise_check"
            },
            "knocking_noise_check": {
                "prompt": "Is it a knocking noise around the engine?",
                "yes": "oil_check",
                "no": "complete"
            },
            "oil_check": {
                "prompt": "Is your oil changed or filled within the last 6 months?",
                "yes": "check_engine_light",
                "no": "oil_level_check"
            },
            "oil_level_check": {
                "prompt": "Is the oil level low or has the oil color changed?",
                "yes": "complete",
                "no": "complete"
            },
            
            "dashboard_light": {
                "prompt": "Are any dashboard lights on?",
                "yes": "which_dashboard_light",
                "no": "complete"
            },
            "battery_terminal_check": {
                "prompt": "Are the battery terminals corroded or loose (yes/no)?",
                "yes": "clean_and_tighten_terminals",
                "no": "battery_voltage_check"
            },
            "clean_and_tighten_terminals": {
                "prompt": "Clean and tighten the battery terminals. Did it start (yes/no)?",
                "yes": "complete",
                "no": "battery_voltage_check"
            },
            "battery_voltage_check": {
                "prompt": "Is the battery voltage below 12.4V (yes/no)?",
                "yes": "charge_or_replace_battery",
                "no": "starter_motor_check"
            },
            "charge_or_replace_battery": {
                "prompt": "Charge or replace the battery. Did it start (yes/no)?",
                "yes": "complete",
                "no": "starter_motor_check"
            },
            "starter_motor_check": {
                "prompt": "Does the starter motor not engage or sound weak (yes/no)?",
                "yes": "replace_starter_motor",
                "no": "fuel_system_check"
            },
            "replace_starter_motor": {
                "prompt": "Replace the starter motor. Did it start (yes/no)?",
                "yes": "complete",
                "no": "fuel_system_check"
            },
            "fuel_system_check": {
                "prompt": "Is there an issue with the fuel system (fuel pump, filter, etc.) (yes/no)?",
                "yes": "repair_fuel_system",
                "no": "ignition_system_check"
            },
            "repair_fuel_system": {
                "prompt": "Repair the fuel system. Did it start (yes/no)?",
                "yes": "complete",
                "no": "ignition_system_check"
            },
            "ignition_system_check": {
                "prompt": "Is there an issue with the ignition system (spark plugs, coil, etc.) (yes/no)?",
                "yes": "repair_ignition_system",
                "no": "check_engine_light"
            },
            "repair_ignition_system": {
                "prompt": "Repair the ignition system. Did it start (yes/no)?",
                "yes": "complete",
                "no": "check_engine_light"
            },
            "complete" : {
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


