#  override



class parentclass ():
    def send_message(self):
        print("bu alan içine mesaj verilecektir")

class baseclass(parentclass):
    def send_message(self):
        print("base class üzerinden gelen mesaj")




parent = parentclass ()
parent.send_message()

base = baseclass()
base.send_message()