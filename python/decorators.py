def log_me(func):
    ''' Log input parameters and return values of a function '''

    def func_wrapper(self, *args, **kwargs):
        args_list = list(args)
        for k, v in kwargs.iteritems():
            args_list.append('{0}={1}'.format(k, v))
        print 'Calling {0}{1}'.format(func.func_name, tuple(args_list))
        result = func(self, *args, **kwargs)
        print 'Result: {0}'.format(result)
        return result

    return func_wrapper
