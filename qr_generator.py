import qrcode

# Sample list
my_list = [{'njofvjenfbv': 'rwniwvn', 'hjswdbhv': 'kjnwndcjkwv'}]

# Convert the list to a string
list_str = ', '.join(map(str, my_list))

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the list string as data to the QR code
qr.add_data(list_str)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_img.save("list_qr_code.png")

# Display the QR code
qr_img.show()
