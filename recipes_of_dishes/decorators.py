def add_created_by_post(func):
    def wrapper(self, *args, **kwargs):
        print(*args)
        request = args[0]
        request.data["created_by"] = request.user.pk
        return func(self, request)
    return wrapper
    
def add_created_by_get(func):
    def wrapper(self, *args, **kwargs):
        print(*args)
        request = args[0]
        request.data["created_by"] = request.user.pk
        return func(self, *args, **kwargs)
    return wrapper
    
