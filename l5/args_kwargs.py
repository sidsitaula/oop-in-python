def args(a, *args):
    print(a)
    print(args)


def kwargs2(**kwargs):
    print(kwargs)


def kwargs(a='', **kwargs):
    print(kwargs)
    kwargs2(**kwargs)


args(1, 2, 3, 4)
kwargs(a=67, b=69, c=68)
