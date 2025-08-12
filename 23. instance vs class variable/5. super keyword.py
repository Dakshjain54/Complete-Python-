class parentclass:
    def parent_method(self):
        print("This is the parent method 1")

class childclass(parentclass):
    def parent_method(self):
        print("daksh2")
        super().parent_method()    

    def child_method(self):
        print("This is the child method 2")
        super().parent_method()    

child_obj = childclass()
child_obj.child_method()
child_obj.parent_method()