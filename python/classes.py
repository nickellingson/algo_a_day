class MyClass:
    class_var = "Hello from class!"

    def __init__(self, value):
        self.value = value  # instance variable

    def instance_method(self):
        # Uses self (instance)
        print(f"Instance method called. Value = {self.value}")

    @staticmethod
    def static_method(msg):
        # No access to self or cls
        print(f"Static method called. Message = {msg}")

    @classmethod
    def class_method(cls):
        # Accesses cls (the class)
        print(f"Class method called. class_var = {cls.class_var}")

# --- Usage examples ---
obj = MyClass(42)

# 1. Instance method: called on an object
obj.instance_method()  
# Output: "Instance method called. Value = 42"

# 2. Static method: can be called via the class or instance
MyClass.static_method("Hello")
obj.static_method("Hello again")
# Output:
# "Static method called. Message = Hello"
# "Static method called. Message = Hello again"

# 3. Class method: can be called via class or instance
MyClass.class_method()
obj.class_method()
# Output:
# "Class method called. class_var = Hello from class!"
# "Class method called. class_var = Hello from class!"