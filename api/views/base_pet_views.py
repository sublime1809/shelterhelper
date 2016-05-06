from django.views.generic import View


class PetIndexView(View):
    model = None
    model_name = None

    def __init__(self, **kwargs):
        super(PetIndexView, self).__init__(**kwargs)
        if not self.model and not self.model_name:
            raise ValueError('Must define model for IndexView')


class PetListView(View):
    model = None
    model_name = None

    def __init__(self, **kwargs):
        super(PetListView, self).__init__(**kwargs)
        if not self.model and not self.model_name:
            raise ValueError('Must define model for IndexView')


class PetQueryView(View):
    model = None
    model_name = None

    def __init__(self, **kwargs):
        super(PetQueryView, self).__init__(**kwargs)
        if not self.model and not self.model_name:
            raise ValueError('Must define model for IndexView')

    def dispatch(self, request, *args, **kwargs):
        query_string = kwargs.get('filter_params')
        if query_string:
            bits = query_string.split('/')
        else:
            bits = list()
        if len(bits) % 2 != 0:
            raise ValueError('Invalid number of params. Must be formatted '
                             '<key>/<value>')
        filter_params = {bits[i]: bits[i+1] for i in range(0, len(bits), 2)}
        kwargs.update({'filter_params': filter_params})
        return super(PetQueryView, self).dispatch(request, *args, **kwargs)
