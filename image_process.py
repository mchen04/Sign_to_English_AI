import os
import cv2
import mediapipe as mp

def process_image(image_path):
    # Load image
    image = cv2.imread(image_path)

    # Initialize MediaPipe hand detection solution
    mp_hands = mp.solutions.hands.Hands()

    # Process image
    results = mp_hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Extract hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Do something with the hand landmarks
            pass

    # Display processed image
    cv2.imshow('Processed Image', image)

    # Create a new folder to store the processed images
    output_folder_path = "processed_photos"
    os.makedirs(output_folder_path, exist_ok=True)

    # Get the filename of the original image
    filename = os.path.basename(image_path)

    # Save the processed image to the new folder
    output_path = os.path.join(output_folder_path, filename)
    cv2.imwrite(output_path, image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Set the path to your test_photos folder
input_folder_path = os.path.join(os.getcwd(), "test_photos")

# Loop through all the files in the folder
for filename in os.listdir(input_folder_path):
    # Check if the file is an image file (you can modify this to support other image formats)
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Get the full path to the image
        image_path = os.path.join(input_folder_path, filename)

        # Process the image using the process_image function
        process_image(image_path)
