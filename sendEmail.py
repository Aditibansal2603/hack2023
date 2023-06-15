import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("rideseeker1@gmail.com", password)
    # TODO: Send email here

sender_email = "rideseeker1@gmail.com"
receiver_email = ["rideofferer1@gmail.com", "rideseeker1@gmail.com"]
message = """\
Subject: Hi there

This message is sent from Python."""

server.connect("smtp.gmail.com", 465)
server.ehlo()
server.login("rideseeker1@gmail.com", password)
server.sendmail(sender_email, receiver_email, message)
