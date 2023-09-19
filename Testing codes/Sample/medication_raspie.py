import RPi.GPIO as GPIO
import time

# Initialize GPIO pins for controlling the robotic arm or dispenser
# Set up sensors and other hardware components

class MedicationDispensingSystem:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.motor_pin = 17  # Replace with the actual GPIO pin number
        self.sensor_pin = 18  # Replace with the actual GPIO pin number
        GPIO.setup(self.motor_pin, GPIO.OUT)
        GPIO.setup(self.sensor_pin, GPIO.IN)

    def dispense_medication(self, medication_name, dosage):
        # Simulate checking medication database for dosage information
        medication_database = {
            "Medicine X": 10,
            "Medicine Y": 5,
        }
        
        if medication_name in medication_database:
            if dosage <= medication_database[medication_name]:
                # Dispense medication using the robotic arm or dispenser (simulated)
                GPIO.output(self.motor_pin, GPIO.HIGH)
                time.sleep(2)  # Simulate dispensing duration
                GPIO.output(self.motor_pin, GPIO.LOW)

                # Log the dispensing event and dosage for monitoring
                print(f"Dispensed {dosage}mg of {medication_name}")
            else:
                print("Dosage exceeds available stock.")
        else:
            print("Medication not found in the database.")

    def monitor_medication_usage(self):
        # Simulate monitoring sensor for medication removal
        while True:
            if GPIO.input(self.sensor_pin) == GPIO.HIGH:
                # Medication has been removed, log the event (simulated)
                print("Medication removed.")

            # Implement a delay to prevent continuous checking
            time.sleep(2)

    def cleanup(self):
        GPIO.cleanup()

# Instantiate the Medication Dispensing System
medication_system = MedicationDispensingSystem()

# Example usage:
# Dispense 10mg of "Medicine X"
medication_system.dispense_medication("Medicine X", 10)

# Start monitoring medication usage
medication_system.monitor_medication_usage()
