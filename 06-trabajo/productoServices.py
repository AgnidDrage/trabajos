from repositorios import Repositorios


class ProductoService():

    def get_productosList(self):
        return Repositorios().productosList
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

    #def insertion_sort_precio(self, productosList, tipo_orden):
     #   lista = self.get_productosList()
      #  for key in range (1, len(lista)):
       #     insertar = lista[key]
        #    key2 = key-1
         #   while key2 >= 0 and lista[key2]["_precio"] > insertar["_precio"]:
          #      lista[key2+1] = lista[key]
           #     key2 = 1
        #return lista
