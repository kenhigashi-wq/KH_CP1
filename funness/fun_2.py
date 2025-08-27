import random
import string
import json
import os
from cryptography.fernet import Fernet
from getpass import getpass

class PasswordManager:
    def __init__(self):
        self.key_file = "key.key"
        self.password_file = "passwords.enc"
        self.master_password_hash = "master_password.key"
        self.cipher_suite = self._load_or_create_key()
        self.passwords = self._load_passwords()

    def _load_or_create_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
        else:
            with open(self.key_file, "rb") as key_file:
                key = key_file.read()
        return Fernet(key)

    def _load_passwords(self):
        if os.path.exists(self.password_file):
            with open(self.password_file, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = self.cipher_suite.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        return {}

    def _save_passwords(self):
        encrypted_data = self.cipher_suite.encrypt(json.dumps(self.passwords).encode())
        with open(self.password_file, "wb") as file:
            file.write(encrypted_data)

    def generate_password(self, length=16):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def add_password(self, service, username, password=None):
        if password is None:
            password = self.generate_password()
        
        self.passwords[service] = {
            'username': username,
            'password': password
        }
        self._save_passwords()
        return password

    def get_password(self, service):
        return self.passwords.get(service)

    def list_services(self):
        return list(self.passwords.keys())

    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self._save_passwords()
            return True
        return False

def main():
    pm = PasswordManager()
    
    while True:
        print("\n🔐 Password Manager")
        print("=" * 40)
        print("1. Add new password")
        print("2. Generate random password")
        print("3. View password")
        print("4. List all services")
        print("5. Delete password")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            use_generated = input("Generate random password? (y/n): ").lower() == 'y'
            
            if use_generated:
                password = pm.add_password(service, username)
                print(f"\n✅ Generated password: {password}")
            else:
                password = getpass("Enter password: ")
                pm.add_password(service, username, password)
            print("✅ Password saved successfully!")

        elif choice == "2":
            length = int(input("Enter password length (default 16): ") or 16)
            password = pm.generate_password(length)
            print(f"\n✅ Generated password: {password}")

        elif choice == "3":
            service = input("Enter service name: ")
            credentials = pm.get_password(service)
            if credentials:
                print(f"\nService: {service}")
                print(f"Username: {credentials['username']}")
                print(f"Password: {credentials['password']}")
            else:
                print("❌ Service not found!")

        elif choice == "4":
            services = pm.list_services()
            if services:
                print("\nStored services:")
                for i, service in enumerate(services, 1):
                    print(f"{i}. {service}")
            else:
                print("No passwords stored yet!")

        elif choice == "5":
            service = input("Enter service name to delete: ")
            if pm.delete_password(service):
                print("✅ Password deleted successfully!")
            else:
                print("❌ Service not found!")

        elif choice == "6":
            print("\n👋 Thanks for using Password Manager!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()