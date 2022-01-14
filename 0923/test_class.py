import cv2 

class Robot:
    def __init__(self, name, target):
        self.name = name
        self.target = target

    def is_marker_detected(self, image):
        flag = False
        (corners, ids, rejects) = cv2.aruco.detectMarkers(image, d, p)
        if self.target in ids:
            flag = True
        return flag

    def switch_target(self, new_target):
        self.target = new_target

class NewRobot(Robot):

    def switch_target(self, new_target):
        assert new_target < 1000
        self.target = new_target

    def make_noise(self):
        print("Robot {} shouted: 'Huray!'".format(self.name))
