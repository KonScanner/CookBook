import sys
from typing import List


class CrowsNest:
    def __init__(self) -> None:
        self.vowels = "aeiouAEIOU"
        self.a = "a"
        self.an = "an"
        self.ac = "Ahow, Captain,"
        self.otlb = "off the landboard bow!"

    def _cap(self, str_: str):
        return str_.capitalize()

    def _vowelCheck(self, str_: str):
        return self.an if str_[0] in self.vowels else self.a

    def run(self, list_: List[str]):
        """
        Arguments:
            list_:  List[str]
        Returns:
            "Ahow, Captain, (a|an) *list_, off the landboard bow!"
        """
        if len(list_) == 2:
            return f"{self.ac} {self._vowelCheck(list_[1])} {self._cap(list_[1])} {self.otlb}"

        elif len(list_) > 2:
            result_str = ""
            for c, i in enumerate(list_):
                if c == 0:
                    result_str += f" {self._vowelCheck(i)} {self._cap(i)}"
                elif c != len(list_) - 2:
                    result_str += f", {self._vowelCheck(i)} {self._cap(i)}"
                else:
                    result_str += f" and {self._vowelCheck(i)} {self._cap(i)}"
        else:
            print(help(self.run))
            return "Please use at lease one parameter on execution!"


if __name__ == "__main__":
    print(CrowsNest().run(sys.argv))
