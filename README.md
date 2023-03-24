# HandGesture

In This Repositary I am Writing My Self Satisfaction Project #3
This Respository contains complete the hand gesture recognition system. that can be easily trained for certain task.

Hand gesture recognition is a complex task that involves multiple steps such as capturing images or videos, detecting hands, extracting features, and classifying the gestures.

sample.py captures video from the webcam, detects the hand using a skin color mask, finds the contours of the hand, and displays the processed frame with the bounding box around the hand. You can add the gesture classification code to this script to complete the hand gesture recognition system. and its not trained and easily available to train with the gesture based on the hand region of interest. This step depends on the approach you're using for gesture classification. One common approach is to extract features from the hand region of interest, such as the position of the fingers, and use machine learning algorithms to classify the gestures

main.py captures video from the webcam, detects the hand using a skin color mask, finds the contours of the hand, extracts the hand region of interest, and clusters the hand pixels using KMeans. The gesture is then classified based on the KMeans centroids. If the centroid corresponding to the "closed" hand gesture is larger than the centroid corresponding to the "open" hand gesture, the gesture is classified as a fist. Otherwise, it is classified as an open hand. Finally, the gesture label is displayed on the frame. 

And if anyone wondering what  KMeans is a clustering algorithm in machine learning. It is used to partition a set of data points into clusters based on their similarity. The goal of clustering is to group data points that are similar to each other into the same cluster, while keeping data points that are dissimilar to each other in different clusters.

In the context of the hand gesture recognition code, the KMeans algorithm is used to cluster the pixels of the hand region of interest (ROI) into two clusters, which represent the foreground and background of the ROI. The algorithm finds the centroids of these two clusters, and based on the distance between the centroids, it classifies the gesture as either a "fist" or an "open hand". This classification is based on the assumption that when a person makes a fist, the foreground pixels of the ROI are clustered together, while when they open their hand, the foreground pixels are more spread out.

Commentedmain.py is the same file but it has comments added to easily understand the code to viewer
