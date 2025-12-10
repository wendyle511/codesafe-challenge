"""
Starter Login System

This program simulates a simple login process.  
It keeps track of users, accepts input, and logs activity.

Some parts of this system may not follow recommended security practices.
Your task in the Codesafe challenge will involve improving the security
of the login process based on what you learn.
"""

import datetime


# Very small sample database (not secure, just for demo purposes)
USER_DATABASE = {
    "alice": "password123",
    "bob": "letmein",
    "charlie": "qwerty"
}


class ActivityLog:
    """
    A basic in-memory logging tool.

    Stores text entries and prints them when added.
    Not intended for real-world production use.
    """

    def __init__(self):
        self.entries = []

    def _timestamp(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def write(self, text: str):
        """Record a log entry with a timestamp."""
        entry = f"[{self._timestamp()}] {text}"
        print(entry)
        self.entries.append(entry)

    def show(self):
        """Show all recorded entries."""
        print("\n--- ACTIVITY LOG ---")
        if not self.entries:
            print("(no activity recorded)")
        for entry in self.entries:
            print(entry)
        print("--- END OF LOG ---\n")


class LoginSystem:
    """
    A very simple authentication handler.

    - Checks if a username exists
    - Compares entered passwords
    - Logs all attempts and results
    """

    def __init__(self, db: dict, logger: ActivityLog):
        self.db = db
        self.logger = logger

    def authenticate(self, username: str, password: str) -> bool:
        """
        Attempt to authenticate a user.

        The function logs each attempt. Some information recorded
        in the logs may not follow best security practices.
        """

        # This line may need review from a security perspective.
        # It records full details of the login attempt.
        self.logger.write(f"ATTEMPT user={username} password={password}")

        # Check if user exists
        if username not in self.db:
            self.logger.write("RESULT: failure (unknown user)")
            return False

        # Password validation
        if self.db[username] != password:
            self.logger.write("RESULT: failure (invalid password)")
            return False

        # Success
        self.logger.write("RESULT: success")
        return True


def run_login_simulation():
    """
    Runs a simple 3-attempt login loop.

    Prompts the user to enter a username and password.
    After the attempts, the activity log is displayed.
    """

    logger = ActivityLog()
    system = LoginSystem(USER_DATABASE, logger)

    print("Welcome to the system demo.")
    print("You will have up to 3 attempts to log in.\n")

    max_attempts = 3
    attempts = 0

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
