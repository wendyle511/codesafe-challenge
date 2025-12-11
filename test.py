import unittest
import startercode

class TestLoginSystem(unittest.TestCase):
    def setUp(self):
        self.users = codesafe_login.USERS

    def test_successful_login_still_works(self):
        """Valid username + password should still succeed."""
        logger = codesafe_login.SecurityLogger()
        system = codesafe_login.LoginSystem(self.users, logger)
        result = system.authenticate("alice", "password123")
        self.assertTrue(result, "Valid credentials should still log in successfully")

    def test_failed_login_wrong_password(self):
        """Wrong password should still fail."""
        logger = codesafe_login.SecurityLogger()
        system = codesafe_login.LoginSystem(self.users, logger)
        result = system.authenticate("alice", "wrongpassword")
        self.assertFalse(result, "Wrong password should not log in")

    def test_failed_login_unknown_user(self):
        """Unknown username should still fail."""
        logger = codesafe_login.SecurityLogger()
        system = codesafe_login.LoginSystem(self.users, logger)
        result = system.authenticate("unknown_user", "whatever")
        self.assertFalse(result, "Unknown user should not log in")

    def _assert_password_not_logged(self, username, password):
        """Helper to check that raw password is never written to logs."""
        logger = codesafe_login.SecurityLogger()
        system = codesafe_login.LoginSystem(self.users, logger)
        system.authenticate(username, password)
        joined = "\n".join(logger.events)

        # There should still be a log message about the login attempt
        self.assertTrue(
            any("LOGIN TRY" in e for e in logger.events),
            "There should be a log line for login attempts",
        )

        # But the actual password string must not appear anywhere in the logs
        self.assertNotIn(
            password,
            joined,
            "Raw password must not appear in logs",
        )

    def test_password_not_logged_for_successful_login(self):
        self._assert_password_not_logged("alice", "password123")

    def test_password_not_logged_for_failed_login(self):
        self._assert_password_not_logged("alice", "wrongpassword")


if __name__ == "__main__":
    unittest.main()
