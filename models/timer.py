import time

class Timer():
    def __init__(self,nb_min = 40):
        self._nb_min = nb_min
        self._nb_min_remaining = nb_min
        self.time = "Not started"

    def start(self):

        while(self._nb_min_remaining):
            mins, secs = divmod(self._nb_min_remaining, 60)
            self.time = '{:02d}:{:02d}'.format(mins, secs)
            print(self.time, end="\r")
            time.sleep(1)
            self._nb_min_remaining -= 1


        self._nb_min_remaining = self._nb_min
        self.time = "Not started"
