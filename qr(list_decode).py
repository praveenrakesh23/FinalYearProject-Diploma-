import cv2
import json

# Function to decode a QR code image and parse JSON data
def decode_json_qr_code(qr_code_image_path):
    # Load the QR code image
    img = cv2.imread(qr_code_image_path)

    # Create a QR code detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    retval, decoded_info, decoded_points, straight_qrcode = detector.detectAndDecodeMulti(img)

    if retval:
        # Ensure we have at least one QR code detected
        if len(decoded_info) > 0:
            # Take the first decoded QR code (assuming only one QR code is present)
            decoded_text = decoded_info[0]

            try:
                # Parse the JSON data
                decoded_data = json.loads(decoded_text)
                return decoded_data
            except json.JSONDecodeError as e:
                print("Failed to parse JSON data from QR code:", str(e))
                return None
        else:
            print("No QR code detected in the image.")
            return None
    else:
        print("QR code not detected or could not be decoded.")
        return None

# Path to the QR code image containing the JSON data
qr_code_image_path = "list.png"  # Replace with your image path

# Decode the QR code and get the JSON data
decoded_data = decode_json_qr_code(qr_code_image_path)

if decoded_data is not None:
    # Print the decoded JSON data
    print(decoded_data)
