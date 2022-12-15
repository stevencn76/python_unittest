class Calculator:
    def add(self, *args):
        result = 0

        for n in args:
            result += n
            if n == 2:
                result += 5

        return result
