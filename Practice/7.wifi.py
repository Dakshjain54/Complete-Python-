import subprocess

def get_wifi_passwords():

    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
    
    profiles = []
    for line in result.stdout.split('\n'):
        if "All User Profile" in line:
            profile_name = line.split(":")[1].strip()
            profiles.append(profile_name)
    
    wifi_passwords = {}
    
    for profile in profiles:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                wifi_passwords[profile] = password
    
    return wifi_passwords
def wifi_passwords():
    wifi_passwords = get_wifi_passwords()
    
    for profile, password in wifi_passwords.items():
        print(f"Profile: {profile}, Password: {password}")
def main():
    print("Saved Wi-Fi Passwords:")
    wifi_passwords = get_wifi_passwords()
    
    if not wifi_passwords:
        print("No saved Wi-Fi passwords found.")
    else:
        for profile, password in wifi_passwords.items():
            print(f"Profile: {profile}, Password: {password}")
if __name__ == "__main__":
    main()
    

