import qrcode

def generate_upi_qr(upi_id, amount, recipient_name="Recipient Name"):
    # Generate the UPI payment URL
    url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}'
    
    # Generate the QR code
    qr = qrcode.make(url)
    
    # Show the QR code
    qr.show()
    
    return qr

def save_qr_code(qr, filename="upi_qr.png"):
    # Save the QR code as an image file
    qr.save(filename)
    print(f"QR code saved as {filename}")

# Input UPI details
upi_id = input("Enter your UPI ID: ")
amount = float(input("Enter the amount to pay: "))

# Generate and display the QR code
qr = generate_upi_qr(upi_id, amount)

# Uncomment this to save the QR code to a file
# save_qr_code(qr, "upi_payment_qr.png")
