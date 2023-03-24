import cv2
import numpy as np
from sklearn.cluster import KMeans

cap = cv2.VideoCapture(0)

# Define the range of skin color for hand detection
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

# Define the KMeans model for clustering hand pixels
kmeans = KMeans(n_clusters=2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the captured frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply a skin color mask to detect the hand
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    # Find the contours of the hand
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(contour) > 10000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extract hand region of interest
            roi = mask[y:y + h, x:x + w]
            roi_pixels = np.float32(roi.reshape(-1, 1))

            # Cluster hand pixels using KMeans
            kmeans.fit(roi_pixels)

            # Classify the gesture based on the KMeans centroids
            if kmeans.cluster_centers_[0] > kmeans.cluster_centers_[1]:
                gesture = "fist"
            else:
                gesture = "open hand"

            # Display the gesture label
            cv2.putText(frame, gesture, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
