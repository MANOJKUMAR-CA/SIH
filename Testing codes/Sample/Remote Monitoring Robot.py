import cv2

class RemoteMonitoringRobot:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)  # Initialize the camera (0 for the default camera)

    def capture_and_display(self):
        while True:
            ret, frame = self.camera.read()  # Read a frame from the camera

            if not ret:
                print("Error reading frame from the camera.")
                break

            cv2.imshow("Remote Monitoring", frame)  # Display the frame
            key = cv2.waitKey(1)

            if key == 27:  # Press 'Esc' to exit
                break

        self.camera.release()
        cv2.destroyAllWindows()

# Instantiate the Remote Monitoring Robot
robot = RemoteMonitoringRobot()

# Start capturing and displaying the video feed
robot.capture_and_display()
