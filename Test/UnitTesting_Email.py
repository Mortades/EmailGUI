import unittest
from readEmailCredentials import readCredentials
from Email_GUI import sendemail
from Email_GUI import save_file

class Test_email(unittest.TestCase):
    def testReadCredentials1(self):
        email, password = readCredentials("Credential1.txt")
        self.assertEqual(email, 'humanreal20@gmail.com', "Email address is wrong")

    def testReadCredentials2(self):
        email, password = readCredentials("Credential2.txt")
        self.assertEqual(email, 'humanreal20@"@gmail.com*', "Email address is wrong")
        self.assertEqual(password, 'dfhdfhdfgsdfds!"$%^&*', "Email address is wrong")

    def testSendEmail(self):
        login, password = readCredentials("Credential1.txt")
        Error = sendemail(login, login,
                  'Subject', 'Message',
                  login, password,
                  smtpserver='smtp.gmail.com:587')

        self.assertEqual(Error, 1, "Problem in sendEmail Function")

    # def testY(self):
        # self.assertEqual(x, is equal to y, error msg)
if __name__ == '__main__':
    unittest.main()
