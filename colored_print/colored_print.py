from datetime import datetime

__author__ = 'aGn'
__copyright__ = "Copyright 2021, Planet Earth"


class ColoredPrint:
    def __init__(self):
        self.PINK = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'

    def __call__(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.msg, **kwargs)
        return self

    def disable(self):
        self.PINK = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def store(self, *args, path: str = 'logfile.log'):
        if args:
            self.msg = ' '.join(map(str, args))
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(path, mode='a') as file_:
            file_.write(f"{self.msg} -- {date}")
            file_.write("\n")

    def success(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.OKGREEN + self.msg + self.ENDC, **kwargs)
        return self

    def info(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.OKBLUE + self.msg + self.ENDC, **kwargs)
        return self

    def warn(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.WARNING + self.msg + self.ENDC, **kwargs)
        return self

    def warning(self, *args, **kwargs):
        return self.warn(*args, **kwargs)

    def err(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.FAIL + self.msg + self.ENDC, **kwargs)
        return self

    def error(self, *args, **kwargs):
        return self.err(*args, **kwargs)

    def critical(self, *args, **kwargs):
        return self.err(*args, **kwargs)

    def pink(self, *args, **kwargs):
        self.msg = ' '.join(map(str, args))
        print(self.PINK + self.msg + self.ENDC, **kwargs)
        return self

    def green(self, *args, **kwargs):
        return self.success(*args, **kwargs)

    def red(self, *args, **kwargs):
        return self.err(*args, **kwargs)

    def blue(self, *args, **kwargs):
        return self.info(*args, **kwargs)

    def yellow(self, *args, **kwargs):
        return self.warn(*args, **kwargs)


log = ColoredPrint()
