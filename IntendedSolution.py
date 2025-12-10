"""
Secure Login System (INTENDED SOLUTION)

This is the corrected version of the starter code.
The login system behavior stays the same, but sensitive
information is no longer written to the activity log.
"""

import datetime


USER_DATABASE = {
    "alice": "password123",
    "bob": "letmein",
    "charlie": "qwerty"
}


class ActivityLog:
    """In-memory log with timestamps."""

    def __init__(self):
        self.entries = []

    def _timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def write(self, text: str):
        entry = f"[{self._timestamp()}] {text}"
        print(entry)
        self.entries.append(entry)

    def show(self):
        print("\n--- ACTIVITY LOG ---")
        if not self.entries:
            print("(no activity recorded)")
        for e in self.entries:
            print(e)
        print("--- END OF LOG ---\n")


class LoginSystem:
    """
    Handles basic username/password authentication.
    """

    def __init__(self, db: dict, logger: ActivityLog):
        self.db = db
        self.logger = logger

    def authenticate(self, username: str, password: str) -> bool:
        """
        Secure version:
        - Still logs login attempts
        - Does NOT log sensitive info (passwords)
        """

        # FIXED: removed password from log entry
        self.logger.write(f"ATTEMPT user={username}")

        if username not in self.db:
            self.logger.write("RESULT: failure (unknown user)")
            return False

        if self.db[username] != password:
            self.logger.write("RESULT: failure (invalid password)")
            return False

        self.logger.write("RESULT: success")
        return True


def run_login_simulation():
    """Three-attempt login loop."""

    logger = ActivityLog()
    system = LoginSystem(USER_DATABASE, logger)

    print("Welcome to the system demo.")
    print("You will have up to 3 attempts to log in.\n")

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print(f"Attempt {attempts + 1} of {max_attempts}")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if system.authenticate(username, password):
            print(f"Login successful. Welcome, {username}!\n")
            break
        else:
            print("Login failed. Try again.\n")
            attempts += 1

    if attempts >= max_attempts:
        print("Too many failed attempts. Exiting...\n")

    print("Activity log:")
    logger.show()


if __name__ == "__main__":
    run_login_simulation()
