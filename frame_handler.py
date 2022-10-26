import cv2
import numpy as np

input_source_list = ['picture', 'video', 'camera_feed', 'camera_capture']

def draw_boxes(frame):
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    ret, thresh1 = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY)
    contours2, hierarchy2 = cv2.findContours(thresh1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    image_copy2 = frame.copy()
    cv2.drawContours(image_copy2, contours2, -1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('SIMPLE Approximation contours', image_copy2)
    cv2.waitKey(0)
    image_copy3 = frame.copy()
    for i, contour in enumerate(contours2): # loop over one contour area
        for j, contour_point in enumerate(contour): # loop over the points
            # draw a circle on the current contour coordinate
            cv2.circle(image_copy3, ((contour_point[0][0], contour_point[0][1])), 2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('CHAIN_APPROX_SIMPLE Point only', image_copy3)
    cv2.waitKey(0)
    cv2.imwrite('contour_point_simple.jpg', image_copy3)
    cv2.destroyAllWindows()

def movement_detector(img):  
  frame_count = 0
  previous_frame = None  
  while True:
    frame_count += 1
    if ((frame_count % 2) == 0):
        # 2. Prepare image; grayscale and blur
        prepared_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5,5), sigmaX=0)
        # 3. Set previous frame and continue if there is None
        if (previous_frame is None):
        # First frame; there is no previous one yet
            previous_frame = prepared_frame
            continue          
        # calculate difference and update previous frame
        diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
        previous_frame = prepared_frame
        # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
        kernel = np.ones((5, 5))
        diff_frame = cv2.dilate(diff_frame, kernel, 1)
        # 5. Only take different areas that are different enough (>20 / 255)
        thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        contoured_frame = img.copy()
        cv2.drawContours(image=contoured_frame, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        return contoured_frame

def load_frame(source_num):

    input = input_source_list[source_num]

    #image
    if input == input_source_list[0]:
        img = cv2.imread(filename="assets/street_parking_1.png")
        draw_boxes(img)
        cv2.imshow('PSD frame', img)
        cv2.waitKey(0)

    #feed from video frame
    elif input == input_source_list[1]:
        cap = cv2.VideoCapture('assets/street_parking_1.mp4') 
        # Check if camera opened successfully
        if (cap.isOpened()== False): 
            print("Error opening video stream or file") 
        # Read until video is completed
        frame_count = 0
        previous_frame = None
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            

            if ret == True: 
                grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                prepared_frame = cv2.GaussianBlur(src=grey_frame, ksize=(5,5), sigmaX=0)
                frame_count+=1

                if (previous_frame is None):
                    previous_frame = prepared_frame
                    continue  
                diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
                previous_frame = prepared_frame
                kernel = np.ones((5, 5))
                diff_frame = cv2.dilate(diff_frame, kernel, 1)
                thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
                contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
                contoured_frame = frame.copy()
                cv2.drawContours(image=contoured_frame, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)       
                cv2.imshow('Original Frame',frame) 
                # cv2.imshow('Grey Frame', grey_frame)
                # cv2.imshow('Gaussian Frame', prepared_frame)
                # cv2.imshow('Difference Frame', diff_frame)
                cv2.imshow('Movement Extraction Frame', thresh_frame)
                cv2.imshow('Coutoured Frame', contoured_frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break        
            # Break the loop when video ends
            else: 
                break       
        # When everything done, release the video capture object
        cap.release()      
        # Closes all the frames
        cv2.destroyAllWindows()
    
    #feed from webcam
    elif input == input_source_list[2]:
        cap = cv2.VideoCapture(0)
        previous_frame = None
        while True:
            ret, frame = cap.read()
            if ret == True:
                grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                prepared_frame = cv2.GaussianBlur(src=grey_frame, ksize=(5,5), sigmaX=0)
                if (previous_frame is None):
                    previous_frame = prepared_frame
                    continue  
                diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
                previous_frame = prepared_frame
                kernel = np.ones((5, 5))
                diff_frame = cv2.dilate(diff_frame, kernel, 1)
                thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
                contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
                contoured_frame = frame.copy()
                cv2.drawContours(image=contoured_frame, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

                cv2.imshow('PSD frame from camera', frame)
                cv2.imshow('PSD Movement between frames tracking', thresh_frame)
                cv2.imshow('PSD frame from camera after contouring', contoured_frame)
            # press escape to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
    else:
        print("No data source is selected. Please select a data source to continue.")
#0- image
#1- video
#2- webcam

load_frame(2)   





