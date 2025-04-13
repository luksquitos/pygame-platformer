from datetime import datetime, timedelta

class Delay:
    def __init__(self, **kwargs):
        self.start_at = datetime.now()
        self.end_at = self.start_at + timedelta(**kwargs)
    
    def __bool__(self):
        self.now = datetime.now()
        return self.now < self.end_at
    