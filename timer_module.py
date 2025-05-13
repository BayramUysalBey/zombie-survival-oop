import time
def timer(func):  
    def wrapper(*args, **kwargs):  
        start = time.time()  
        result = func(*args, **kwargs)  
        end = time.time()  
        with open("zombie_performance.txt", "a") as f:  
            f.write(f"{func.__name__} took {end - start} seconds\n")  
        return result  
    return wrapper