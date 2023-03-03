import datetime

def log_error(msg):
    print(f'[*][{datetime.datetime.now().replace(microsecond=0).isoformat()}][ERROR] {msg}')

def log_warning(msg):
    print(f'[*][{datetime.datetime.now().replace(microsecond=0).isoformat()}][WARNING] {msg}')

def log_info(msg):
    print(f'[*][{datetime.datetime.now().replace(microsecond=0).isoformat()}][INFO] {msg}')