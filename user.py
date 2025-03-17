class User:
    def __init__(self, name='', age=0, email=''):
        self._name = name  # Using underscore to indicate a private variable

    # Getter for name
    def get_name(self):
        return self._name
    
    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            raise ValueError("Invalid name")

    '''
    #accepting user info
    def accept_user_input(self):
        try:
            self.set_name(input("Enter your name: "))
        except ValueError as e:
            print(f"Error: {e}")'''

    # greeting user
    def greet(self):
        print(f"Good Luck! {self.get_name()}")  
    