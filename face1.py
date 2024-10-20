import cv2 

# Load the cascade classifier
cascade_path = "haarcascade_frontalface_default.xml"
a = cv2.CascadeClassifier(cascade_path)

# Initialize video capture
b = cv2.VideoCapture(0)

while True:
    c_rec, d_image = b.read()
    
    # Check if frame is read properly
    if not c_rec:
        print("Failed to capture image")
        break
    
    # Convert to grayscale
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR
    f = a.detectMultiScale(e, 1.3, 6)
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)

    # Display the image
    cv2.imshow('img', d_image)
    
    # Break the loop when 'Esc' key is pressed
    h = cv2.waitKey(40) & 0xff
    if h == 27:  # 27 is the ASCII code for 'Esc'
        break

# Release the video capture object and close all OpenCV windows
b.release()
cv2.destroyAllWindows()