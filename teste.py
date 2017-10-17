import django

from pitcaria.models import cliente

django.setup()

import pitcaria.models.cliente


def populate():

    add_cliente(username="bruno", passw="bruno", first="Bruno", last="Weber", cpf="09741044933",
                telefone=4734324161, data="26/03/1997", email="brunowber@gmail.com")


def add_cliente(username, passw, first, last, cpf, telefone, data, email):
    try:
        m = cliente.models.Pitcaria.objects.get_or_create(username=username, password=passw, first_name=first,
                                                          last_name=last, cpf=cpf, telefone=telefone, data_nasc=data, email=email)[0]
        m.save()
    except:
        print "Falha ao criar usuario"
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting entornos population script...")
    populate()