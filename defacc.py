class Account:
    def __init__(self, acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self,old_pass,new_pass):
        if old_pass == self.__acc_pass:
            self.__acc_pass = new_pass
            print("Password has been changed successfully.")
        else:
            print("Old password is incorrect. Password change failed.")
pass1 = Account(123456, "my_password")
pass1.reset_pass("my_password", "new_password")
print("Password reset successful.")
print("Attempting to reset password with incorrect old password:")
pass1.reset_pass("wrong_password", "new_password")
print("Password reset attempt with incorrect old password completed.")
print("Attempting to reset password with correct old password:")
pass1.reset_pass("new_password", "another_new_password")
print("Password reset successful.")