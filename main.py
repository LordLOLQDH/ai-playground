# Import necessary libraries
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't send data, just uses the address of the host
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
    except Exception as e:
        print(f"Error: {e}")
        ip_address = "Unknown"
    finally:
        s.close()
    return ip_address

def save_user_data(email, password, ip):
    with open("userdaten.txt", "a") as file:
        file.write(f"{email},{password},{ip}\n")

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    ip = get_ip_address()
    
    save_user_data(email, password, ip)
    print("User data saved successfully.")
