def add_created_by(func):
    def wrapper(self, *args, **kwargs):
        request = args[0]
        request.data["created_by"] = request.user.pk
        return func(self, request)
    return wrapper
    
