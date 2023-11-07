import functools

def log_arguments(func):
    """Log arguments: 
    Logs decorated function arguments, stored in .__logged_info__ member list
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(arg) for arg in args])
        log_entry = f"Called function {func.__name__} with arguments: {args_str}"
        log_arguments.__logged_info__.append(log_entry)
        return func(*args, **kwargs)
    return wrapper

log_arguments.__logged_info__ = []

def show_log():
    for entry in log_arguments.__logged_info__:
        print(entry)
    log_arguments.__logged_info__ = []