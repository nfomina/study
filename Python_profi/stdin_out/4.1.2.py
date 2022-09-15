import sys
from datetime import datetime

data = [datetime.strptime(x.strip(), '%Y-%m-%d') for x in sys.stdin]

print((max(data)-min(data)).days)