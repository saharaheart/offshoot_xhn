import inherited_2
class shape():
    @classmethod
    def install(cls):
        if inherited_2.config["allow"]["plugins"] is True:
            print('This can be used')
class circle(shape):
    config = {'red':'fucking'}
cir = circle()
cir.install()
