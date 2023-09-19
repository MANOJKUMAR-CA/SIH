import time

class RehabilitationRobot:
    def __init__(self):
        self.motor = None  # Placeholder for a robotic arm or motor (not implemented in this simplified example)

    def perform_exercise(self, exercise_name):
        if self.motor is None:
            print("Rehabilitation robot hardware not initialized.")
            return
        
        if exercise_name == "Shoulder Flexion":
            print("Performing Shoulder Flexion exercise.")
            # Simulate the robotic arm moving to assist with the exercise
            self.motor.move_to_position(45)  # Move to 45 degrees angle
            time.sleep(2)  # Simulate exercise duration
            self.motor.move_to_position(0)  # Return to the initial position
        elif exercise_name == "Knee Extension":
            print("Performing Knee Extension exercise.")
            # Simulate the robotic arm moving to assist with the exercise
            self.motor.move_to_position(90)  # Move to 90 degrees angle
            time.sleep(2)  # Simulate exercise duration
            self.motor.move_to_position(0)  # Return to the initial position
        elif exercise_name == "Elbow Flexion":
            print("Performing Elbow Flexion exercise.")
            # Simulate the robotic arm moving to assist with the exercise
            self.motor.move_to_position(30)  # Move to 90 degrees angle
            time.sleep(2)  # Simulate exercise duration
            self.motor.move_to_position(0)  # Return to the initial position
        else:
            print("Unknown exercise name. Please specify a valid exercise.")

# Instantiate the Rehabilitation Robot
robot = RehabilitationRobot()

# Example usage:
# Perform the "Shoulder Flexion" exercise
robot.perform_exercise("Shoulder Flexion")

# Perform the "Knee Extension" exercise
robot.perform_exercise("Knee Extension")

# Perform the "Elbow Flexion" exercise
robot.perform_exercise("Elbow Flexion")