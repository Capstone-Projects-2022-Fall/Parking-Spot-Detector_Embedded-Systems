import cv2

input_source_list = ['picture', 'video', 'cameraCapture', 'cameraFeed']

def load_frame(source_num):

    input = input_source_list[source_num]

    if input == input_source_list[0]:
        img = cv2.imread(filename="assets/nature_1.jpeg")
        cv2.imshow('image', img)
        cv2.waitKey(0)
    elif input == input_source_list[1]:
        vid = cv2.VideoCapture(filename="")  
        cv2.imshow('image', img)
        cv2.waitKey(0)
    elif input == input_source_list[3]:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            # frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
            cv2.imshow('webcam', frame)
        # press escape to exit
            if (cv2.waitKey(30) == 27):
                break
        cap.release()
    else:
        print("Not yet configured")


load_frame(0)   



