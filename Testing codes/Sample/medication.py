import time
class MedicationDispensingRobot:
    def __init__(self):
        self.medication_database = {
            "Medicine A": {"stock": 100, "dose": 5},
            "Medicine B": {"stock": 10, "dose": 10},
        }

    def dispense_medication(self, medication_name, dosage):
        if medication_name in self.medication_database:
            if self.medication_database[medication_name]["stock"] >= dosage:
                # Dispense medication
                print(f"Dispensing {dosage}mg of {medication_name}.")
                self.medication_database[medication_name]["stock"] -= dosage
            else:
                print("Not enough medication in stock.")
        else:
            print("Medication not found in the database.")

    def calibrate(self):
        print("Calibrating the robot.")

    def safety_check(self):
        print("Performing safety checks.")

# Instantiate the Medication Dispensing Robot
robot = MedicationDispensingRobot()

# Example usage:
robot.calibrate()
robot.safety_check()

# Dispense 5mg of "Medicine A"
robot.dispense_medication("Medicine A", 5)

# Dispense 15mg of "Medicine B" (not enough in stock)
robot.dispense_medication("Medicine B", 15)

# Dispense 10mg of "Medicine C" (not in the database)
robot.dispense_medication("Medicine C", 10)
