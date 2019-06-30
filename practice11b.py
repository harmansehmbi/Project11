class Login:

    def loginUser(self):
        print(">> Login dear User !!")


class GoogleLogin(Login):

    def loginUser(self, email, password):
        print(">> Google Login Done")


class FacebookLogin(Login):

    def loginUser(self, fbUserName, password):
        print("Fackebook Login Done")


class OTPLogin(Login):

    def loginUser(self, phone):
        print(">> OTP Login Done")


class Cab:

    def bookCab(self, source, destination):
        print("Cab booked from {} to {}".format(source, destination))

class OLAMicro(Cab):

    def bookCab(self, source, destination):
        print("OLA Micro booked from {} to {}".format(source, destination))


class OLASedan(Cab):

    def bookCab(self, source, destination):
        print("OLA Sedan booked from {} to {}".format(source, destination))


class OLAMini(Cab):

    def bookCab(self, source, destination):
        print("OLA Mini booked from {} to {}".format(source, destination))

# In Python everything is dynamic (RUN TIME)
# Polymorphism : RUN TIME POLYMORPHISM

login = Login()
login.loginUser()

print()

login = GoogleLogin()
login.loginUser("John@example.com", "pass123")

print()

login = OTPLogin()
login.loginUser("+91 98721 111045")

print()

print("++++++++++++++++++++++++++")

print()

cab = Cab()
cab.bookCab("Silver Arc", "MBD")

print()

cab = OLAMicro()
cab.bookCab("A", "G")
