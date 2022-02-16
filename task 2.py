def form(chisl, forma):
    return ('{0:%s}'%(forma)).format(chisl)

print(form(40, 'b'))