class TextProcessor:
    def __init__(self) -> None:
        self._punctuation = '.,!?%@#$*&^:;'


    def __is_punktuation(self, char):
        return char in self._punctuation


    def get_clean_string(self, sTring):
        clean = ""
        for char in sTring:
            if self.__is_punktuation(char):
                continue
            clean += char
        return clean
    
    
x = TextProcessor()
print(x.get_clean_string('')) # <- Enter your string