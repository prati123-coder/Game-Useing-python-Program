def func (a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(5,6,7,8,9,name="pratiksha", age=21)
# kwargs should be a last parameter   # *arge is a last parameter