from Function import Function
import pickle


class FunctionsSet:
    def __init__(self):
        self.set_of_functions = []

    def add_function(self, function: Function):
        self.set_of_functions.append(function)

    def delete_function(self, function: Function):
        self.set_of_functions.remove(function)

    def delete_function_by(self, index: int):
        if(self.set_of_functions[index]):
            del self.set_of_functions[index]

    def save_to_file(self, file_name):
        # with open("bin.dat", "wb") as f:
        with open(file_name, "wb") as f:
            pickle.dump(self.set_of_functions, f)

    def read_from_file(self, file_name):
        try:
            # with open("bin.dat", "rb") as f:
            with open(file_name, "rb") as f:
                self.set_of_functions = pickle.load(f)

        except Exception:
            pass

    def __str__(self):
        i = 0
        __str = ""
        for f in self.set_of_functions:
            __str += f"[{i}] {f.type}, {f.info}\n"
            i += 1
        return __str
