from repositorios import Repositorios


class ProductoService():

    def get_productosList(self):
        print(Repositorios().productosList)

    def add_producto(self, producto):
        key = len(Repositorios.productosList)
        Repositorios.productosList[key] = producto.__dict__
        return key

    def delete_producto(self, key):
        try:
            lastKey = (len(Repositorios().productosList))
            if key < lastKey and key >= 0:
                del Repositorios.productosList[key]
            else:
                raise KeyError
        except KeyError:
            raise ValueError("ERROR: Key not found")
