import cv2
import numpy as np
import csv
import os
import face_recognition
import numpy

video_capture = cv2.VideoCapture(0)
 
jobs_image = face_recognition.load_image_file("jobs.jpg")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
 
ratan_tata_image = face_recognition.load_image_file("tata.jpg")
ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]
 
mark_image = face_recognition.load_image_file("mark.jpg")
mark_encoding = face_recognition.face_encodings(mark_image)[0]
 
elon_image = face_recognition.load_image_file("elon.jpg")  
elon_encoding = face_recognition.face_encodings(elon_image)[0]
 
known_face_encoding = [
jobs_encoding,
ratan_tata_encoding,
mark_encoding,
elon_encoding
]
 
known_faces_names = [
"jobs",
"ratan tata",
"Mark Zuckerberg",
"Elon Musk"
]
 
patients = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
 

d={"jobs":"Cold Fever","ratan tata":"HeadAche","Mark Zuckerberg":"TB","Elon Musk":"Heart Attack"}
 
 
f = open('patients_details.csv','w+',newline = '')
lnwriter = csv.writer(f)
 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame =numpy.ascontiguousarray(small_frame[:, :, ::-1])
    if True:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2
 
                cv2.putText(frame,name, 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
 
                if name in patients:
                    patients.remove(name)
                    print("*patient Details*")
                    print("NAME:",name)
                    print("Problem:",d[name])
                    lnwriter.writerow([name,d[name]])
    cv2.imshow("Patient Details",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()
f.close()


