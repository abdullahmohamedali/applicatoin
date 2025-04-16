from cryptography.fernet import Fernet
import os

# Path to save the encryption key and diary
KEY_FILE = "diary_key.key"
DIARY_FILE = "encrypted_diary.txt"

def generate_key():
    """Generate and save a new encryption key if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        print("New encryption key generated and saved.")
    else:
        print("Encryption key already exists.")

def load_key():
    """Load the encryption key from the file."""
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key not found. Run the program to generate one first.")
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_data(data, cipher):
    """Encrypt data using the cipher."""
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data, cipher):
    """Decrypt data using the cipher."""
    return cipher.decrypt(encrypted_data).decode()

def write_diary_entry():
    """Write a new diary entry and encrypt it."""
    diary_entry = input("Write your diary entry: ")
    cipher = Fernet(load_key())
    encrypted_entry = encrypt_data(diary_entry, cipher)
    
    # Append the encrypted entry to the diary file
    with open(DIARY_FILE, 'ab') as diary_file:
        diary_file.write(encrypted_entry + b'\n')
    
    print("Diary entry saved securely.")

def read_diary_entries():
    """Decrypt and read all diary entries."""
    if not os.path.exists(DIARY_FILE):
        print("No diary entries found.")
        return
    
    cipher = Fernet(load_key())
    with open(DIARY_FILE, 'rb') as diary_file:
        for line in diary_file:
            decrypted_entry = decrypt_data(line.strip(), cipher)
            print(f"- {decrypted_entry}")

def main():
    """Main menu for the diary manager."""
    print("Welcome to the Daily Diary Encryption Manager!")
    generate_key()  # Ensure the key exists
    while True:
        print("\nChoose an option:")
        print("1. Write a new diary entry")
        print("2. View all diary entries")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            write_diary_entry()
        elif choice == "2":
            read_diary_entries()
        elif choice == "3":
            print("Goodbye! Your secrets are safe with me.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
