import cv2
import json
import sqlite3

with sqlite3.connect("sqlite.db") as db:
    cur = db.cursor()

query = "SELECT product_name FROM raw_inventory"
cur.execute(query)
product_name = cur.fetchall()


# Function to decode a QR code image and parse JSON data
def decode_json_qr_code(decoded_text):
    try:
        # Parse the JSON data
        decoded_data = json.loads(decoded_text)
        return decoded_data
    except json.JSONDecodeError as e:
        print("Failed to parse JSON data from QR code:", str(e))
        return None


# Initialize the camera
cap = cv2.VideoCapture(0)  # Use the default camera (change 0 to a different number if you have multiple cameras)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Create a QR code detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code in the frame
    retval, decoded_info, decoded_points, _ = detector.detectAndDecodeMulti(frame)

    if retval:
        # Ensure we have at least one QR code detected
        if len(decoded_info) > 0:
            # Take the first decoded QR code (assuming only one QR code is present)
            decoded_text = decoded_info[0]

            # Decode the JSON data from the QR code
            decoded_data = decode_json_qr_code(decoded_text)

            if decoded_data is not None:
                # Print the decoded JSON data
                print(decoded_data)
                print(type(decoded_data))


                # Close the OpenCV window
                cv2.destroyAllWindows()
                break

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
