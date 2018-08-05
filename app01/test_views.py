from django.shortcuts import HttpResponse
from .models import T1, T2


def create_t1_t2(request):
    """
    T1.objects.create(name='t1')

    book_list = []
    for i in range(1000):
        book = T2(name="book_%s" % i)
        book_list.append(book)

    T2.objects.bulk_create(book_list)
    """

    print(T1.objects.all().values_list())
    print('==============')
    print(T2.objects.filter(pk=998).values_list())
    import time
    s_time = time.time()
    T1.objects.all()
    print(time.time() - s_time)
    time.sleep(2)
    t_time = time.time()
    T2.objects.all()
    print(time.time() - t_time)

    return HttpResponse("OK")
