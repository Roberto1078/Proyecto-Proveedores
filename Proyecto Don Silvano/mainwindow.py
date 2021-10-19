from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog,QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Administrador.administrador_proveedores import Proveedores
from Administrador.proveedor import Proveedor


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow,self).__init__()
        self.proveedores = Proveedores()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.contador = 0
        self.lista = []
        #Ventana Agregar
        self.ui.agregar_guardar_pushbutton.clicked.connect(self.click_agregar_proveedor)
        self.ui.agregar_mostrar_todos_los_proveedores_pushbutton.clicked.connect(self.click_mostrar_todo)
        #Click Archivo
        self.ui.actionGuardar_Archivo.triggered.connect(self.guardar_archivo)
        self.ui.actionAbrir_Archivo.triggered.connect(self.abrir_archivo)
        #Ventana Buscar
        self.ui.buscar_pushbutton.clicked.connect(self.buscar)
        

    @Slot()
    def click_agregar_proveedor(self) :
        
        nombre = self.ui.nombre_lineedit.text().title()
        empresa = self.ui.empresa_lineedit.text().title()
        direccion = self.ui.direccion_lineedit.text().title()
        colonia = self.ui.colonia_lineedit.text().upper()
        telefono_de_oficina = self.ui.telefono_de_oficina_lineedit.text()
        celular = self.ui.celular_lineedit.text()
        ciudad = self.ui.ciudad_lineedit.text().upper()
        estado = self.ui.estado_lineedit.text().upper()
        recomienda = self.ui.recomienda_lineedit.text().upper()
        correo_electronico = self.ui.correo_electronico_lineedit.text()
        link = self.ui.link_lineedit.text()
        producto1 = self.ui.producto1_lineedit.text().upper()
        producto2 = self.ui.producto2_lineedit.text().upper()
        producto3 = self.ui.producto3_lineedit.text().upper()
        producto4 = self.ui.producto4_lineedit.text().upper()
        producto5 = self.ui.producto5_lineedit.text().upper()
        producto6 = self.ui.producto6_lineedit.text().upper()
        oficio1 = self.ui.actividad1_lineedit.text().upper()
        oficio2 = self.ui.actividad2_lineedit.text().upper()
        oficio3 = self.ui.actividad3_lineedit.text().upper()
        oficio4 = self.ui.actividad4_lineedit.text().upper()
        oficio5 = self.ui.actividad5_lineedit.text().upper()
        oficio6 = self.ui.actividad6_lineedit.text().upper()


        proveedor = Proveedor(nombre,empresa,direccion,colonia,telefono_de_oficina,celular,ciudad,estado,recomienda,
        correo_electronico,link,producto1,producto2,producto3,producto4,producto5,producto6,
        oficio1,oficio2,oficio3,oficio4,oficio5,oficio6)
        self.proveedores.agregar(proveedor)

        QMessageBox.information(
            self,
            'Éxito',
            'Se ha agregado correctamente al proveedor'
        )
    
    @Slot()
    def click_mostrar_todo(self) :

        self.ui.mostrar_todo_plaintextedit.clear()
        self.ui.mostrar_todo_plaintextedit.insertPlainText(str(self.proveedores)) 

    @Slot()
    def guardar_archivo(self):

        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            'proveedores',
            'JSON (*.json)'
        )[0]

        if self.proveedores.guardar_archivo(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'El archivo se ha guardado correctamente en ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo guardar el archivo'
            )

    @Slot()
    def abrir_archivo(self):

        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            'proveedores',
            'JSON (*.json)'
        )[0]

        if self.proveedores.abrir_archivo(ubicacion) :
            QMessageBox.information(
                self,
                'Éxito',
                'Se abrio el archivo correctamente ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo abrir el archivo'
            )

    @Slot()
    def buscar(self):

        busqueda = self.ui.busqueda_lineedit.text().upper()

        if self.contador==0 :

            a=0 #Oficio
            b=0 #Producto
            c=0 #Colonia
            d=0 #Ciudad
            e=0 #Estado
            f=0 #Persona que recomienda
            for proveedor in self.proveedores :

                if busqueda==proveedor.oficio1 or busqueda==proveedor.oficio2 or busqueda==proveedor.oficio3 or busqueda==proveedor.oficio4 or busqueda==proveedor.oficio5 or busqueda==proveedor.oficio6 :
                    a+=1
                elif busqueda==proveedor.producto1 or busqueda==proveedor.producto2 or busqueda==proveedor.producto3 or busqueda==proveedor.producto4 or busqueda==proveedor.producto5 or busqueda==proveedor.producto6 :
                    b+=1
                elif busqueda==proveedor.colonia :
                    c+=1
                elif busqueda==proveedor.ciudad :
                    d+=1
                elif busqueda==proveedor.estado :
                    e+=1
                elif busqueda==proveedor.recomienda :
                    f+=1

            temporal_list = []
            temporal_list.append(a)
            temporal_list.append(b)
            temporal_list.append(c)
            temporal_list.append(d)
            temporal_list.append(e)
            temporal_list.append(f)
            temporal_list.sort(reverse=True)

            if a==0 and b==0 and c==0 and d==0 and e==0 and f==0 :
                QMessageBox.warning(
                    self,
                    'Atención',
                    f'El criterio de busqueda "{busqueda}" no coincide con el registro '
                )
            elif a==temporal_list[0] : #Oficio

                contactos_encontrados_oficio(self,busqueda)

                tabla_de_oficios(self,busqueda)

                self.contador=1

            elif b==temporal_list[0] : #Producto

                contactos_encontrados_producto(self,busqueda)

                tabla_de_productos(self,busqueda)

                self.contador=1

            elif c==temporal_list[0] : #Colonia

                contactos_encontrados_colonia(self,busqueda) #self.lista se le meten los contactos encontrados

                tabla_de_colonia(self)

                self.contador=1

            elif d==temporal_list[0] : #Ciudad

                contactos_encontrados_ciudad(self,busqueda)

                tabla_de_ciudad(self)

                self.contador=1

            elif e==temporal_list[0] : #Estado

                contactos_encontrados_estado(self,busqueda)

                tabla_de_estado(self)

                self.contador=1

            elif f==temporal_list[0] :
                self.contador=1
        else:

            busqueda = self.ui.busqueda_lineedit.text().upper()

            a=0 #Oficio
            b=0 #Producto
            c=0 #Colonia
            d=0 #Ciudad
            e=0 #Estado
            f=0 #Persona que recomienda
            for proveedores in self.lista :

                if busqueda==proveedores[17] or busqueda==proveedores[18] or busqueda==proveedores[19] or busqueda==proveedores[20] or busqueda==proveedores[21] or busqueda==proveedores[22] :
                    a+=1
                elif busqueda==proveedores[11] or busqueda==proveedores[12] or busqueda==proveedores[13] or busqueda==proveedores[14] or busqueda==proveedores[15] or busqueda==proveedores[16] :
                    b+=1
                elif busqueda==proveedores[3] :
                    c+=1
                elif busqueda==proveedores[6] :
                    d+=1
                elif busqueda==proveedores[7] :
                    e+=1
                elif busqueda==proveedores[8] :
                    f+=1

            temporal_list = []
            temporal_list.append(a)
            temporal_list.append(b)
            temporal_list.append(c)
            temporal_list.append(d)
            temporal_list.append(e)
            temporal_list.append(f)
            temporal_list.sort(reverse=True)

            if a==0 and b==0 and c==0 and d==0 and e==0 and f==0 :
                QMessageBox.warning(
                    self,
                    'Atención',
                    f'El criterio de busqueda "{busqueda}" no coincide con el registro '
                )
            elif a==temporal_list[0] : #Oficio

                contactos_encontrados_oficio_segundaiteracion(self,busqueda)

                tabla_de_oficios(self,busqueda)

            elif b==temporal_list[0] : #Producto

                contactos_encontrados_producto_segundaiteracion(self,busqueda)

                tabla_de_productos(self,busqueda)

            elif c==temporal_list[0] : #Colonia

                contactos_encontrados_colonia_segundaiteracion(self,busqueda)

                tabla_de_colonia(self)

            elif d==temporal_list[0] : #Ciudad

                contactos_encontrados_ciudad_segundaiteracion(self,busqueda)

                tabla_de_ciudad(self)

            elif e==temporal_list[0] : #Estado

                contactos_encontrados_estado_segundaiteracion(self,busqueda)

                tabla_de_estado(self)
            
            elif f==temporal_list[0] : #Persona que recomienda
                pass


def contactos_encontrados_colonia(self,busqueda):
        
    for proveedor in self.proveedores :

        if proveedor.colonia==busqueda:

            not_main_list = []    
            not_main_list.append(proveedor.nombre) #Posicion 0
            not_main_list.append(proveedor.empresa) #Posicion 1
            not_main_list.append(proveedor.direccion) #Posicion 2
            not_main_list.append(proveedor.colonia) #Posicion 3
            not_main_list.append(proveedor.telefono_de_oficina) #Posicion 4
            not_main_list.append(proveedor.celular) #Posicion 5
            not_main_list.append(proveedor.ciudad) #Posicion 6
            not_main_list.append(proveedor.estado) #Posicion 7
            not_main_list.append(proveedor.recomienda) #Posicion 8
            not_main_list.append(proveedor.correo_electronico) #Posicion 9
            not_main_list.append(proveedor.link) #Posicion 10
            not_main_list.append(proveedor.producto1) #Posicion 11
            not_main_list.append(proveedor.producto2) #Posicion 12
            not_main_list.append(proveedor.producto3) #Posicion 13
            not_main_list.append(proveedor.producto4) #Posicion 14
            not_main_list.append(proveedor.producto5) #Posicion 15
            not_main_list.append(proveedor.producto6) #Posicion 16
            not_main_list.append(proveedor.oficio1) #Posicion 17
            not_main_list.append(proveedor.oficio2) #Posicion 18
            not_main_list.append(proveedor.oficio3) #Posicion 19
            not_main_list.append(proveedor.oficio4) #Posicion 20
            not_main_list.append(proveedor.oficio5) #Posicion 21
            not_main_list.append(proveedor.oficio6) #Posicion 22

            self.lista.append(not_main_list) #Lista donde se almacena lo encontrado

def contactos_encontrados_ciudad(self,busqueda):

    for proveedor in self.proveedores :

        if proveedor.ciudad==busqueda:
            
            not_main_list = []
            not_main_list.append(proveedor.nombre) #Posicion 0
            not_main_list.append(proveedor.empresa) #Posicion 1
            not_main_list.append(proveedor.direccion) #Posicion 2
            not_main_list.append(proveedor.colonia) #Posicion 3
            not_main_list.append(proveedor.telefono_de_oficina) #Posicion 4
            not_main_list.append(proveedor.celular) #Posicion 5
            not_main_list.append(proveedor.ciudad) #Posicion 6
            not_main_list.append(proveedor.estado) #Posicion 7
            not_main_list.append(proveedor.recomienda) #Posicion 8
            not_main_list.append(proveedor.correo_electronico) #Posicion 9
            not_main_list.append(proveedor.link) #Posicion 10
            not_main_list.append(proveedor.producto1) #Posicion 11
            not_main_list.append(proveedor.producto2) #Posicion 12
            not_main_list.append(proveedor.producto3) #Posicion 13
            not_main_list.append(proveedor.producto4) #Posicion 14
            not_main_list.append(proveedor.producto5) #Posicion 15
            not_main_list.append(proveedor.producto6) #Posicion 16
            not_main_list.append(proveedor.oficio1) #Posicion 17
            not_main_list.append(proveedor.oficio2) #Posicion 18
            not_main_list.append(proveedor.oficio3) #Posicion 19
            not_main_list.append(proveedor.oficio4) #Posicion 20
            not_main_list.append(proveedor.oficio5) #Posicion 21
            not_main_list.append(proveedor.oficio6) #Posicion 22

            self.lista.append(not_main_list) #Lista donde se almacena lo encontrado

def contactos_encontrados_estado(self,busqueda):

    for proveedor in self.proveedores :

        if proveedor.estado==busqueda:

            not_main_list = []    
            not_main_list.append(proveedor.nombre) #Posicion 0
            not_main_list.append(proveedor.empresa) #Posicion 1
            not_main_list.append(proveedor.direccion) #Posicion 2
            not_main_list.append(proveedor.colonia) #Posicion 3
            not_main_list.append(proveedor.telefono_de_oficina) #Posicion 4
            not_main_list.append(proveedor.celular) #Posicion 5
            not_main_list.append(proveedor.ciudad) #Posicion 6
            not_main_list.append(proveedor.estado) #Posicion 7
            not_main_list.append(proveedor.recomienda) #Posicion 8
            not_main_list.append(proveedor.correo_electronico) #Posicion 9
            not_main_list.append(proveedor.link) #Posicion 10
            not_main_list.append(proveedor.producto1) #Posicion 11
            not_main_list.append(proveedor.producto2) #Posicion 12
            not_main_list.append(proveedor.producto3) #Posicion 13
            not_main_list.append(proveedor.producto4) #Posicion 14
            not_main_list.append(proveedor.producto5) #Posicion 15
            not_main_list.append(proveedor.producto6) #Posicion 16
            not_main_list.append(proveedor.oficio1) #Posicion 17
            not_main_list.append(proveedor.oficio2) #Posicion 18
            not_main_list.append(proveedor.oficio3) #Posicion 19
            not_main_list.append(proveedor.oficio4) #Posicion 20
            not_main_list.append(proveedor.oficio5) #Posicion 21
            not_main_list.append(proveedor.oficio6) #Posicion 22

            self.lista.append(not_main_list) #Lista donde se almacena lo encontrado

def contactos_encontrados_oficio(self,busqueda):
        
    for proveedor in self.proveedores :

        if proveedor.oficio1==busqueda or proveedor.oficio2==busqueda or proveedor.oficio3==busqueda or proveedor.oficio4==busqueda or proveedor.oficio5==busqueda or proveedor.oficio6==busqueda :

            not_main_list = []    
            not_main_list.append(proveedor.nombre) #Posicion 0
            not_main_list.append(proveedor.empresa) #Posicion 1
            not_main_list.append(proveedor.direccion) #Posicion 2
            not_main_list.append(proveedor.colonia) #Posicion 3
            not_main_list.append(proveedor.telefono_de_oficina) #Posicion 4
            not_main_list.append(proveedor.celular) #Posicion 5
            not_main_list.append(proveedor.ciudad) #Posicion 6
            not_main_list.append(proveedor.estado) #Posicion 7
            not_main_list.append(proveedor.recomienda) #Posicion 8
            not_main_list.append(proveedor.correo_electronico) #Posicion 9
            not_main_list.append(proveedor.link) #Posicion 10
            not_main_list.append(proveedor.producto1) #Posicion 11
            not_main_list.append(proveedor.producto2) #Posicion 12
            not_main_list.append(proveedor.producto3) #Posicion 13
            not_main_list.append(proveedor.producto4) #Posicion 14
            not_main_list.append(proveedor.producto5) #Posicion 15
            not_main_list.append(proveedor.producto6) #Posicion 16
            not_main_list.append(proveedor.oficio1) #Posicion 17
            not_main_list.append(proveedor.oficio2) #Posicion 18
            not_main_list.append(proveedor.oficio3) #Posicion 19
            not_main_list.append(proveedor.oficio4) #Posicion 20
            not_main_list.append(proveedor.oficio5) #Posicion 21
            not_main_list.append(proveedor.oficio6) #Posicion 22

            self.lista.append(not_main_list) #Lista donde se almacena lo encontrado

def contactos_encontrados_producto(self,busqueda):

    for proveedor in self.proveedores :

        if proveedor.producto1==busqueda or proveedor.producto2==busqueda or proveedor.producto3==busqueda or proveedor.producto4==busqueda or proveedor.producto5==busqueda or proveedor.producto6==busqueda :

            not_main_list = []    
            not_main_list.append(proveedor.nombre) #Posicion 0
            not_main_list.append(proveedor.empresa) #Posicion 1
            not_main_list.append(proveedor.direccion) #Posicion 2
            not_main_list.append(proveedor.colonia) #Posicion 3
            not_main_list.append(proveedor.telefono_de_oficina) #Posicion 4
            not_main_list.append(proveedor.celular) #Posicion 5
            not_main_list.append(proveedor.ciudad) #Posicion 6
            not_main_list.append(proveedor.estado) #Posicion 7
            not_main_list.append(proveedor.recomienda) #Posicion 8
            not_main_list.append(proveedor.correo_electronico) #Posicion 9
            not_main_list.append(proveedor.link) #Posicion 10
            not_main_list.append(proveedor.producto1) #Posicion 11
            not_main_list.append(proveedor.producto2) #Posicion 12
            not_main_list.append(proveedor.producto3) #Posicion 13
            not_main_list.append(proveedor.producto4) #Posicion 14
            not_main_list.append(proveedor.producto5) #Posicion 15
            not_main_list.append(proveedor.producto6) #Posicion 16
            not_main_list.append(proveedor.oficio1) #Posicion 17
            not_main_list.append(proveedor.oficio2) #Posicion 18
            not_main_list.append(proveedor.oficio3) #Posicion 19
            not_main_list.append(proveedor.oficio4) #Posicion 20
            not_main_list.append(proveedor.oficio5) #Posicion 21
            not_main_list.append(proveedor.oficio6) #Posicion 22

            self.lista.append(not_main_list) #Lista donde se almacena lo encontrado

def contactos_encontrados_producto_segundaiteracion(self,busqueda):

    temporal_list=[]    
    for proveedor in self.lista :

        if proveedor[11]==busqueda or proveedor[12]==busqueda or proveedor[13]==busqueda or proveedor[14]==busqueda or proveedor[15]==busqueda or proveedor[16]==busqueda :

            not_main_list = []    
            not_main_list.append(proveedor[0]) #Posicion 0
            not_main_list.append(proveedor[1]) #Posicion 1
            not_main_list.append(proveedor[2]) #Posicion 2
            not_main_list.append(proveedor[3]) #Posicion 3
            not_main_list.append(proveedor[4]) #Posicion 4
            not_main_list.append(proveedor[5]) #Posicion 5
            not_main_list.append(proveedor[6]) #Posicion 6
            not_main_list.append(proveedor[7]) #Posicion 7
            not_main_list.append(proveedor[8]) #Posicion 8
            not_main_list.append(proveedor[9]) #Posicion 9
            not_main_list.append(proveedor[10]) #Posicion 10
            not_main_list.append(proveedor[11]) #Posicion 11
            not_main_list.append(proveedor[12]) #Posicion 12
            not_main_list.append(proveedor[13]) #Posicion 13
            not_main_list.append(proveedor[14]) #Posicion 14
            not_main_list.append(proveedor[15]) #Posicion 15
            not_main_list.append(proveedor[16]) #Posicion 16
            not_main_list.append(proveedor[17]) #Posicion 17
            not_main_list.append(proveedor[18]) #Posicion 18
            not_main_list.append(proveedor[19]) #Posicion 19
            not_main_list.append(proveedor[20]) #Posicion 20
            not_main_list.append(proveedor[21]) #Posicion 21
            not_main_list.append(proveedor[22]) #Posicion 22

            temporal_list.append(not_main_list) #Lista donde se almacena lo encontrado
    self.lista=temporal_list

def tabla_de_productos(self,busqueda):

    self.ui.tabla.clear()
    self.ui.tabla.setColumnCount(23)
    headers = ['Producto1','Producto2','Producto3','Producto4','Producto5','Producto6','Estado','Ciudad','Colonia','Nombre','Telefono','Celular','Oficio1','Oficio2','Oficio3','Oficio4','Oficio5','Oficio6','Empresa','Link','Dirección','Correo electrónico','Recomienda']
    self.ui.tabla.setHorizontalHeaderLabels(headers)
    self.ui.tabla.setRowCount(len(self.lista))
    self.ui.tabla.setColumnWidth(0,150)
    self.ui.tabla.setColumnWidth(1,150)
    self.ui.tabla.setColumnWidth(2,150)
    self.ui.tabla.setColumnWidth(3,150)
    self.ui.tabla.setColumnWidth(4,150)
    self.ui.tabla.setColumnWidth(5,150)
    self.ui.tabla.setColumnWidth(6,150)
    self.ui.tabla.setColumnWidth(7,150)
    self.ui.tabla.setColumnWidth(8,175)
    self.ui.tabla.setColumnWidth(9,150)
    self.ui.tabla.setColumnWidth(12,150)
    self.ui.tabla.setColumnWidth(13,150)
    self.ui.tabla.setColumnWidth(14,150)
    self.ui.tabla.setColumnWidth(15,150)
    self.ui.tabla.setColumnWidth(16,150)
    self.ui.tabla.setColumnWidth(17,150)
    self.ui.tabla.setColumnWidth(21,300)

    row=0

    for proveedor in self.lista:

        mostrar_lista=[]
        for informacion in self.lista[row]:
            mostrar_lista.append(informacion)

        colonia_widget = QTableWidgetItem(mostrar_lista[3])
        ciudad_widget = QTableWidgetItem(mostrar_lista[6])
        estado_widget = QTableWidgetItem(mostrar_lista[7])
        oficio1_widget = QTableWidgetItem(mostrar_lista[17])
        oficio2_widget = QTableWidgetItem(mostrar_lista[18])
        oficio3_widget = QTableWidgetItem(mostrar_lista[19])
        oficio4_widget = QTableWidgetItem(mostrar_lista[20])
        oficio5_widget = QTableWidgetItem(mostrar_lista[21])
        oficio6_widget = QTableWidgetItem(mostrar_lista[22])
        nombre_widget = QTableWidgetItem(mostrar_lista[0])
        telefono_widget = QTableWidgetItem(mostrar_lista[4])
        celular_widget = QTableWidgetItem(mostrar_lista[5])
        producto1_widget = QTableWidgetItem(mostrar_lista[11])
        producto2_widget = QTableWidgetItem(mostrar_lista[12])
        producto3_widget = QTableWidgetItem(mostrar_lista[13])
        producto4_widget = QTableWidgetItem(mostrar_lista[14])
        producto5_widget = QTableWidgetItem(mostrar_lista[15])
        producto6_widget = QTableWidgetItem(mostrar_lista[16])
        empresa_widget = QTableWidgetItem(mostrar_lista[1])
        link_widget = QTableWidgetItem(mostrar_lista[10])
        direccion_widget = QTableWidgetItem(mostrar_lista[2])
        correo_electronico_widget = QTableWidgetItem(mostrar_lista[9])
        recomienda_widget = QTableWidgetItem(mostrar_lista[8])


        if busqueda==mostrar_lista[11]:
            self.ui.tabla.setItem(row, 0, producto1_widget)
            self.ui.tabla.setItem(row, 1, producto2_widget)
            self.ui.tabla.setItem(row, 2, producto3_widget)
            self.ui.tabla.setItem(row, 3, producto4_widget)
            self.ui.tabla.setItem(row, 4, producto5_widget)
            self.ui.tabla.setItem(row, 5, producto6_widget)
        elif busqueda==mostrar_lista[12]:
            self.ui.tabla.setItem(row, 0, producto2_widget)
            self.ui.tabla.setItem(row, 1, producto1_widget)
            self.ui.tabla.setItem(row, 2, producto3_widget)
            self.ui.tabla.setItem(row, 3, producto4_widget)
            self.ui.tabla.setItem(row, 4, producto5_widget)
            self.ui.tabla.setItem(row, 5, producto6_widget)
        elif busqueda==mostrar_lista[13]:
            self.ui.tabla.setItem(row, 0, producto3_widget)
            self.ui.tabla.setItem(row, 1, producto2_widget)
            self.ui.tabla.setItem(row, 2, producto1_widget)
            self.ui.tabla.setItem(row, 3, producto4_widget)
            self.ui.tabla.setItem(row, 4, producto5_widget)
            self.ui.tabla.setItem(row, 5, producto6_widget)
        elif busqueda==mostrar_lista[14]:
            self.ui.tabla.setItem(row, 0, producto4_widget)
            self.ui.tabla.setItem(row, 1, producto2_widget)
            self.ui.tabla.setItem(row, 2, producto3_widget)
            self.ui.tabla.setItem(row, 3, producto1_widget)
            self.ui.tabla.setItem(row, 4, producto5_widget)
            self.ui.tabla.setItem(row, 5, producto6_widget)
        elif busqueda==mostrar_lista[15]:
            self.ui.tabla.setItem(row, 0, producto5_widget)
            self.ui.tabla.setItem(row, 1, producto2_widget)
            self.ui.tabla.setItem(row, 2, producto3_widget)
            self.ui.tabla.setItem(row, 3, producto4_widget)
            self.ui.tabla.setItem(row, 4, producto1_widget)
            self.ui.tabla.setItem(row, 5, producto6_widget)
        elif busqueda==mostrar_lista[16]:
            self.ui.tabla.setItem(row, 0, producto6_widget)
            self.ui.tabla.setItem(row, 1, producto2_widget)
            self.ui.tabla.setItem(row, 2, producto3_widget)
            self.ui.tabla.setItem(row, 3, producto4_widget)
            self.ui.tabla.setItem(row, 4, producto5_widget)
            self.ui.tabla.setItem(row, 5, producto1_widget)

        self.ui.tabla.setItem(row, 6, estado_widget)
        self.ui.tabla.setItem(row, 7, ciudad_widget)
        self.ui.tabla.setItem(row, 8, colonia_widget)
        self.ui.tabla.setItem(row, 9, nombre_widget)
        self.ui.tabla.setItem(row, 10, telefono_widget)
        self.ui.tabla.setItem(row, 11, celular_widget)
        self.ui.tabla.setItem(row, 12, oficio1_widget)
        self.ui.tabla.setItem(row, 13, oficio2_widget)
        self.ui.tabla.setItem(row, 14, oficio3_widget)
        self.ui.tabla.setItem(row, 15, oficio4_widget)
        self.ui.tabla.setItem(row, 16, oficio5_widget)
        self.ui.tabla.setItem(row, 17, oficio6_widget)
        self.ui.tabla.setItem(row, 18, empresa_widget)
        self.ui.tabla.setItem(row, 19, link_widget)
        self.ui.tabla.setItem(row, 20, direccion_widget)
        self.ui.tabla.setItem(row, 21, correo_electronico_widget)
        self.ui.tabla.setItem(row, 22, recomienda_widget)
                
        row+=1
    proveedores_encontrados = len(self.lista)
    QMessageBox.information(
    self,
    'CONTACTOS ENCONTRADOS',
    f'Se encontraron "{proveedores_encontrados}" contactos')

def contactos_encontrados_oficio_segundaiteracion(self,busqueda) :

    temporal_list=[]    
    for proveedor in self.lista :

        if proveedor[17]==busqueda or proveedor[18]==busqueda or proveedor[19]==busqueda or proveedor[20]==busqueda or proveedor[21]==busqueda or proveedor[22]==busqueda :

            not_main_list = []    
            not_main_list.append(proveedor[0]) #Posicion 0
            not_main_list.append(proveedor[1]) #Posicion 1
            not_main_list.append(proveedor[2]) #Posicion 2
            not_main_list.append(proveedor[3]) #Posicion 3
            not_main_list.append(proveedor[4]) #Posicion 4
            not_main_list.append(proveedor[5]) #Posicion 5
            not_main_list.append(proveedor[6]) #Posicion 6
            not_main_list.append(proveedor[7]) #Posicion 7
            not_main_list.append(proveedor[8]) #Posicion 8
            not_main_list.append(proveedor[9]) #Posicion 9
            not_main_list.append(proveedor[10]) #Posicion 10
            not_main_list.append(proveedor[11]) #Posicion 11
            not_main_list.append(proveedor[12]) #Posicion 12
            not_main_list.append(proveedor[13]) #Posicion 13
            not_main_list.append(proveedor[14]) #Posicion 14
            not_main_list.append(proveedor[15]) #Posicion 15
            not_main_list.append(proveedor[16]) #Posicion 16
            not_main_list.append(proveedor[17]) #Posicion 17
            not_main_list.append(proveedor[18]) #Posicion 18
            not_main_list.append(proveedor[19]) #Posicion 19
            not_main_list.append(proveedor[20]) #Posicion 20
            not_main_list.append(proveedor[21]) #Posicion 21
            not_main_list.append(proveedor[22]) #Posicion 22

            temporal_list.append(not_main_list) #Lista donde se almacena lo encontrado
    self.lista=temporal_list

def tabla_de_oficios(self,busqueda):

    self.ui.tabla.clear()
    self.ui.tabla.setColumnCount(23)
    headers = ['Oficio1','Oficio2','Oficio3','Oficio4','Oficio5','Oficio6','Estado','Ciudad','Colonia','Nombre','Telefono','Celular','Producto1','Producto2','Producto3','Producto4','Producto5','Producto6','Empresa','Link','Dirección','Correo electrónico','Recomienda']
    self.ui.tabla.setHorizontalHeaderLabels(headers)
    self.ui.tabla.setRowCount(len(self.lista))
    self.ui.tabla.setColumnWidth(0,150)
    self.ui.tabla.setColumnWidth(1,150)
    self.ui.tabla.setColumnWidth(2,150)
    self.ui.tabla.setColumnWidth(3,150)
    self.ui.tabla.setColumnWidth(4,150)
    self.ui.tabla.setColumnWidth(5,150)
    self.ui.tabla.setColumnWidth(6,150)
    self.ui.tabla.setColumnWidth(7,150)
    self.ui.tabla.setColumnWidth(8,175)
    self.ui.tabla.setColumnWidth(9,150)
    self.ui.tabla.setColumnWidth(12,150)
    self.ui.tabla.setColumnWidth(13,150)
    self.ui.tabla.setColumnWidth(14,150)
    self.ui.tabla.setColumnWidth(15,150)
    self.ui.tabla.setColumnWidth(16,150)
    self.ui.tabla.setColumnWidth(17,150)
    self.ui.tabla.setColumnWidth(21,300)

    row=0

    for proveedor in self.lista:

        mostrar_lista=[]
        for informacion in self.lista[row]:
            mostrar_lista.append(informacion)

        colonia_widget = QTableWidgetItem(mostrar_lista[3])
        ciudad_widget = QTableWidgetItem(mostrar_lista[6])
        estado_widget = QTableWidgetItem(mostrar_lista[7])
        oficio1_widget = QTableWidgetItem(mostrar_lista[17])
        oficio2_widget = QTableWidgetItem(mostrar_lista[18])
        oficio3_widget = QTableWidgetItem(mostrar_lista[19])
        oficio4_widget = QTableWidgetItem(mostrar_lista[20])
        oficio5_widget = QTableWidgetItem(mostrar_lista[21])
        oficio6_widget = QTableWidgetItem(mostrar_lista[22])
        nombre_widget = QTableWidgetItem(mostrar_lista[0])
        telefono_widget = QTableWidgetItem(mostrar_lista[4])
        celular_widget = QTableWidgetItem(mostrar_lista[5])
        producto1_widget = QTableWidgetItem(mostrar_lista[11])
        producto2_widget = QTableWidgetItem(mostrar_lista[12])
        producto3_widget = QTableWidgetItem(mostrar_lista[13])
        producto4_widget = QTableWidgetItem(mostrar_lista[14])
        producto5_widget = QTableWidgetItem(mostrar_lista[15])
        producto6_widget = QTableWidgetItem(mostrar_lista[16])
        empresa_widget = QTableWidgetItem(mostrar_lista[1])
        link_widget = QTableWidgetItem(mostrar_lista[10])
        direccion_widget = QTableWidgetItem(mostrar_lista[2])
        correo_electronico_widget = QTableWidgetItem(mostrar_lista[9])
        recomienda_widget = QTableWidgetItem(mostrar_lista[8])


        if busqueda==mostrar_lista[17]:
            self.ui.tabla.setItem(row, 0, oficio1_widget)
            self.ui.tabla.setItem(row, 1, oficio2_widget)
            self.ui.tabla.setItem(row, 2, oficio3_widget)
            self.ui.tabla.setItem(row, 3, oficio4_widget)
            self.ui.tabla.setItem(row, 4, oficio5_widget)
            self.ui.tabla.setItem(row, 5, oficio6_widget)
        elif busqueda==mostrar_lista[18]:
            self.ui.tabla.setItem(row, 0, oficio2_widget)
            self.ui.tabla.setItem(row, 1, oficio1_widget)
            self.ui.tabla.setItem(row, 2, oficio3_widget)
            self.ui.tabla.setItem(row, 3, oficio4_widget)
            self.ui.tabla.setItem(row, 4, oficio5_widget)
            self.ui.tabla.setItem(row, 5, oficio6_widget)
        elif busqueda==mostrar_lista[19]:
            self.ui.tabla.setItem(row, 0, oficio3_widget)
            self.ui.tabla.setItem(row, 1, oficio1_widget)
            self.ui.tabla.setItem(row, 2, oficio2_widget)
            self.ui.tabla.setItem(row, 3, oficio4_widget)
            self.ui.tabla.setItem(row, 4, oficio5_widget)
            self.ui.tabla.setItem(row, 5, oficio6_widget)
        elif busqueda==mostrar_lista[20]:
            self.ui.tabla.setItem(row, 0, oficio4_widget)
            self.ui.tabla.setItem(row, 1, oficio1_widget)
            self.ui.tabla.setItem(row, 2, oficio3_widget)
            self.ui.tabla.setItem(row, 3, oficio2_widget)
            self.ui.tabla.setItem(row, 4, oficio5_widget)
            self.ui.tabla.setItem(row, 5, oficio6_widget)
        elif busqueda==mostrar_lista[21]:
            self.ui.tabla.setItem(row, 0, oficio5_widget)
            self.ui.tabla.setItem(row, 1, oficio1_widget)
            self.ui.tabla.setItem(row, 2, oficio3_widget)
            self.ui.tabla.setItem(row, 3, oficio4_widget)
            self.ui.tabla.setItem(row, 4, oficio2_widget)
            self.ui.tabla.setItem(row, 5, oficio6_widget)
        elif busqueda==mostrar_lista[22]:
            self.ui.tabla.setItem(row, 0, oficio6_widget)
            self.ui.tabla.setItem(row, 1, oficio1_widget)
            self.ui.tabla.setItem(row, 2, oficio3_widget)
            self.ui.tabla.setItem(row, 3, oficio4_widget)
            self.ui.tabla.setItem(row, 4, oficio5_widget)
            self.ui.tabla.setItem(row, 5, oficio2_widget)

        self.ui.tabla.setItem(row, 6, estado_widget)
        self.ui.tabla.setItem(row, 7, ciudad_widget)
        self.ui.tabla.setItem(row, 8, colonia_widget)
        self.ui.tabla.setItem(row, 9, nombre_widget)
        self.ui.tabla.setItem(row, 10, telefono_widget)
        self.ui.tabla.setItem(row, 11, celular_widget)
        self.ui.tabla.setItem(row, 12, producto1_widget)
        self.ui.tabla.setItem(row, 13, producto2_widget)
        self.ui.tabla.setItem(row, 14, producto3_widget)
        self.ui.tabla.setItem(row, 15, producto4_widget)
        self.ui.tabla.setItem(row, 16, producto5_widget)
        self.ui.tabla.setItem(row, 17, producto6_widget)
        self.ui.tabla.setItem(row, 18, empresa_widget)
        self.ui.tabla.setItem(row, 19, link_widget)
        self.ui.tabla.setItem(row, 20, direccion_widget)
        self.ui.tabla.setItem(row, 21, correo_electronico_widget)
        self.ui.tabla.setItem(row, 22, recomienda_widget)
                
        row+=1
    proveedores_encontrados = len(self.lista)
    QMessageBox.information(
    self,
    'CONTACTOS ENCONTRADOS',
    f'Se encontraron "{proveedores_encontrados}" contactos')

def contactos_encontrados_colonia_segundaiteracion(self,busqueda):

    temporal_list=[]    
    for proveedor in self.lista :

        if proveedor[3]==busqueda:

            not_main_list = []    
            not_main_list.append(proveedor[0]) #Posicion 0
            not_main_list.append(proveedor[1]) #Posicion 1
            not_main_list.append(proveedor[2]) #Posicion 2
            not_main_list.append(proveedor[3]) #Posicion 3
            not_main_list.append(proveedor[4]) #Posicion 4
            not_main_list.append(proveedor[5]) #Posicion 5
            not_main_list.append(proveedor[6]) #Posicion 6
            not_main_list.append(proveedor[7]) #Posicion 7
            not_main_list.append(proveedor[8]) #Posicion 8
            not_main_list.append(proveedor[9]) #Posicion 9
            not_main_list.append(proveedor[10]) #Posicion 10
            not_main_list.append(proveedor[11]) #Posicion 11
            not_main_list.append(proveedor[12]) #Posicion 12
            not_main_list.append(proveedor[13]) #Posicion 13
            not_main_list.append(proveedor[14]) #Posicion 14
            not_main_list.append(proveedor[15]) #Posicion 15
            not_main_list.append(proveedor[16]) #Posicion 16
            not_main_list.append(proveedor[17]) #Posicion 17
            not_main_list.append(proveedor[18]) #Posicion 18
            not_main_list.append(proveedor[19]) #Posicion 19
            not_main_list.append(proveedor[20]) #Posicion 20
            not_main_list.append(proveedor[21]) #Posicion 21
            not_main_list.append(proveedor[22]) #Posicion 22

            temporal_list.append(not_main_list) #Lista donde se almacena lo encontrado
    self.lista=temporal_list

def tabla_de_colonia(self):

    self.ui.tabla.clear()
    self.ui.tabla.setColumnCount(23)
    headers = ['Colonia','Ciudad','Estado','Oficio1','Oficio2','Oficio3','Oficio4','Oficio5','Oficio6','Nombre','Telefono','Celular','Producto1','Producto2','Producto3','Producto4','Producto5','Producto6','Empresa','Link','Dirección','Correo electrónico','Recomienda']
    self.ui.tabla.setHorizontalHeaderLabels(headers)
    self.ui.tabla.setRowCount(len(self.lista))
    self.ui.tabla.setColumnWidth(0,175)
    self.ui.tabla.setColumnWidth(1,150)
    self.ui.tabla.setColumnWidth(2,150)
    self.ui.tabla.setColumnWidth(3,150)
    self.ui.tabla.setColumnWidth(4,150)
    self.ui.tabla.setColumnWidth(5,150)
    self.ui.tabla.setColumnWidth(6,150)
    self.ui.tabla.setColumnWidth(7,150)
    self.ui.tabla.setColumnWidth(8,150)
    self.ui.tabla.setColumnWidth(9,150)
    self.ui.tabla.setColumnWidth(12,150)
    self.ui.tabla.setColumnWidth(13,150)
    self.ui.tabla.setColumnWidth(14,150)
    self.ui.tabla.setColumnWidth(15,150)
    self.ui.tabla.setColumnWidth(16,150)
    self.ui.tabla.setColumnWidth(17,150)
    self.ui.tabla.setColumnWidth(21,300)

    row=0

    for proveedor in self.lista:

        mostrar_lista=[]
        for informacion in self.lista[row]:
            mostrar_lista.append(informacion)

        colonia_widget = QTableWidgetItem(mostrar_lista[3])
        ciudad_widget = QTableWidgetItem(mostrar_lista[6])
        estado_widget = QTableWidgetItem(mostrar_lista[7])
        oficio1_widget = QTableWidgetItem(mostrar_lista[17])
        oficio2_widget = QTableWidgetItem(mostrar_lista[18])
        oficio3_widget = QTableWidgetItem(mostrar_lista[19])
        oficio4_widget = QTableWidgetItem(mostrar_lista[20])
        oficio5_widget = QTableWidgetItem(mostrar_lista[21])
        oficio6_widget = QTableWidgetItem(mostrar_lista[22])
        nombre_widget = QTableWidgetItem(mostrar_lista[0])
        telefono_widget = QTableWidgetItem(mostrar_lista[4])
        celular_widget = QTableWidgetItem(mostrar_lista[5])
        producto1_widget = QTableWidgetItem(mostrar_lista[11])
        producto2_widget = QTableWidgetItem(mostrar_lista[12])
        producto3_widget = QTableWidgetItem(mostrar_lista[13])
        producto4_widget = QTableWidgetItem(mostrar_lista[14])
        producto5_widget = QTableWidgetItem(mostrar_lista[15])
        producto6_widget = QTableWidgetItem(mostrar_lista[16])
        empresa_widget = QTableWidgetItem(mostrar_lista[1])
        link_widget = QTableWidgetItem(mostrar_lista[10])
        direccion_widget = QTableWidgetItem(mostrar_lista[2])
        correo_electronico_widget = QTableWidgetItem(mostrar_lista[9])
        recomienda_widget = QTableWidgetItem(mostrar_lista[8])

        self.ui.tabla.setItem(row, 0, colonia_widget)
        self.ui.tabla.setItem(row, 1, ciudad_widget)
        self.ui.tabla.setItem(row, 2, estado_widget)
        self.ui.tabla.setItem(row, 3, oficio1_widget)
        self.ui.tabla.setItem(row, 4, oficio2_widget)
        self.ui.tabla.setItem(row, 5, oficio3_widget)
        self.ui.tabla.setItem(row, 6, oficio4_widget)
        self.ui.tabla.setItem(row, 7, oficio5_widget)
        self.ui.tabla.setItem(row, 8, oficio6_widget)
        self.ui.tabla.setItem(row, 9, nombre_widget)
        self.ui.tabla.setItem(row, 10, telefono_widget)
        self.ui.tabla.setItem(row, 11, celular_widget)
        self.ui.tabla.setItem(row, 12, producto1_widget)
        self.ui.tabla.setItem(row, 13, producto2_widget)
        self.ui.tabla.setItem(row, 14, producto3_widget)
        self.ui.tabla.setItem(row, 15, producto4_widget)
        self.ui.tabla.setItem(row, 16, producto5_widget)
        self.ui.tabla.setItem(row, 17, producto6_widget)
        self.ui.tabla.setItem(row, 18, empresa_widget)
        self.ui.tabla.setItem(row, 19, link_widget)
        self.ui.tabla.setItem(row, 20, direccion_widget)
        self.ui.tabla.setItem(row, 21, correo_electronico_widget)
        self.ui.tabla.setItem(row, 22, recomienda_widget)
    
        row+=1
    proveedores_encontrados = len(self.lista)
    QMessageBox.information(
    self,
    'CONTACTOS ENCONTRADOS',
    f'Se encontraron "{proveedores_encontrados}" contactos')

def contactos_encontrados_ciudad_segundaiteracion(self,busqueda):
    
    temporal_list=[]    
    for proveedor in self.lista :

        if proveedor[6]==busqueda:

            not_main_list = []    
            not_main_list.append(proveedor[0]) #Posicion 0
            not_main_list.append(proveedor[1]) #Posicion 1
            not_main_list.append(proveedor[2]) #Posicion 2
            not_main_list.append(proveedor[3]) #Posicion 3
            not_main_list.append(proveedor[4]) #Posicion 4
            not_main_list.append(proveedor[5]) #Posicion 5
            not_main_list.append(proveedor[6]) #Posicion 6
            not_main_list.append(proveedor[7]) #Posicion 7
            not_main_list.append(proveedor[8]) #Posicion 8
            not_main_list.append(proveedor[9]) #Posicion 9
            not_main_list.append(proveedor[10]) #Posicion 10
            not_main_list.append(proveedor[11]) #Posicion 11
            not_main_list.append(proveedor[12]) #Posicion 12
            not_main_list.append(proveedor[13]) #Posicion 13
            not_main_list.append(proveedor[14]) #Posicion 14
            not_main_list.append(proveedor[15]) #Posicion 15
            not_main_list.append(proveedor[16]) #Posicion 16
            not_main_list.append(proveedor[17]) #Posicion 17
            not_main_list.append(proveedor[18]) #Posicion 18
            not_main_list.append(proveedor[19]) #Posicion 19
            not_main_list.append(proveedor[20]) #Posicion 20
            not_main_list.append(proveedor[21]) #Posicion 21
            not_main_list.append(proveedor[22]) #Posicion 22

            temporal_list.append(not_main_list) #Lista donde se almacena lo encontrado
    self.lista=temporal_list

def tabla_de_ciudad(self):

    self.ui.tabla.clear()
    self.ui.tabla.setColumnCount(23)
    headers = ['Ciudad','Estado','Colonia','Oficio1','Oficio2','Oficio3','Oficio4','Oficio5','Oficio6','Nombre','Telefono','Celular','Producto1','Producto2','Producto3','Producto4','Producto5','Producto6','Empresa','Link','Dirección','Correo electrónico','Recomienda']
    self.ui.tabla.setHorizontalHeaderLabels(headers)
    self.ui.tabla.setRowCount(len(self.lista))
    self.ui.tabla.setColumnWidth(0,150)
    self.ui.tabla.setColumnWidth(1,150)
    self.ui.tabla.setColumnWidth(2,175)
    self.ui.tabla.setColumnWidth(3,150)
    self.ui.tabla.setColumnWidth(4,150)
    self.ui.tabla.setColumnWidth(5,150)
    self.ui.tabla.setColumnWidth(6,150)
    self.ui.tabla.setColumnWidth(7,150)
    self.ui.tabla.setColumnWidth(8,150)
    self.ui.tabla.setColumnWidth(9,150)
    self.ui.tabla.setColumnWidth(12,150)
    self.ui.tabla.setColumnWidth(13,150)
    self.ui.tabla.setColumnWidth(14,150)
    self.ui.tabla.setColumnWidth(15,150)
    self.ui.tabla.setColumnWidth(16,150)
    self.ui.tabla.setColumnWidth(17,150)
    self.ui.tabla.setColumnWidth(21,300)

    row=0

    for proveedor in self.lista:

        mostrar_lista=[]
        for informacion in self.lista[row]:
            mostrar_lista.append(informacion)

        colonia_widget = QTableWidgetItem(mostrar_lista[3])
        ciudad_widget = QTableWidgetItem(mostrar_lista[6])
        estado_widget = QTableWidgetItem(mostrar_lista[7])
        oficio1_widget = QTableWidgetItem(mostrar_lista[17])
        oficio2_widget = QTableWidgetItem(mostrar_lista[18])
        oficio3_widget = QTableWidgetItem(mostrar_lista[19])
        oficio4_widget = QTableWidgetItem(mostrar_lista[20])
        oficio5_widget = QTableWidgetItem(mostrar_lista[21])
        oficio6_widget = QTableWidgetItem(mostrar_lista[22])
        nombre_widget = QTableWidgetItem(mostrar_lista[0])
        telefono_widget = QTableWidgetItem(mostrar_lista[4])
        celular_widget = QTableWidgetItem(mostrar_lista[5])
        producto1_widget = QTableWidgetItem(mostrar_lista[11])
        producto2_widget = QTableWidgetItem(mostrar_lista[12])
        producto3_widget = QTableWidgetItem(mostrar_lista[13])
        producto4_widget = QTableWidgetItem(mostrar_lista[14])
        producto5_widget = QTableWidgetItem(mostrar_lista[15])
        producto6_widget = QTableWidgetItem(mostrar_lista[16])
        empresa_widget = QTableWidgetItem(mostrar_lista[1])
        link_widget = QTableWidgetItem(mostrar_lista[10])
        direccion_widget = QTableWidgetItem(mostrar_lista[2])
        correo_electronico_widget = QTableWidgetItem(mostrar_lista[9])
        recomienda_widget = QTableWidgetItem(mostrar_lista[8])

        self.ui.tabla.setItem(row, 0, ciudad_widget)
        self.ui.tabla.setItem(row, 1, estado_widget)
        self.ui.tabla.setItem(row, 2, colonia_widget)
        self.ui.tabla.setItem(row, 3, oficio1_widget)
        self.ui.tabla.setItem(row, 4, oficio2_widget)
        self.ui.tabla.setItem(row, 5, oficio3_widget)
        self.ui.tabla.setItem(row, 6, oficio4_widget)
        self.ui.tabla.setItem(row, 7, oficio5_widget)
        self.ui.tabla.setItem(row, 8, oficio6_widget)
        self.ui.tabla.setItem(row, 9, nombre_widget)
        self.ui.tabla.setItem(row, 10, telefono_widget)
        self.ui.tabla.setItem(row, 11, celular_widget)
        self.ui.tabla.setItem(row, 12, producto1_widget)
        self.ui.tabla.setItem(row, 13, producto2_widget)
        self.ui.tabla.setItem(row, 14, producto3_widget)
        self.ui.tabla.setItem(row, 15, producto4_widget)
        self.ui.tabla.setItem(row, 16, producto5_widget)
        self.ui.tabla.setItem(row, 17, producto6_widget)
        self.ui.tabla.setItem(row, 18, empresa_widget)
        self.ui.tabla.setItem(row, 19, link_widget)
        self.ui.tabla.setItem(row, 20, direccion_widget)
        self.ui.tabla.setItem(row, 21, correo_electronico_widget)
        self.ui.tabla.setItem(row, 22, recomienda_widget)
                
        row+=1
    proveedores_encontrados = len(self.lista)
    QMessageBox.information(
    self,
    'CONTACTOS ENCONTRADOS',
    f'Se encontraron "{proveedores_encontrados}" contactos')

def contactos_encontrados_estado_segundaiteracion(self,busqueda):
    
    temporal_list=[]    
    for proveedor in self.lista :

        if proveedor[7]==busqueda:

            not_main_list = []    
            not_main_list.append(proveedor[0]) #Posicion 0
            not_main_list.append(proveedor[1]) #Posicion 1
            not_main_list.append(proveedor[2]) #Posicion 2
            not_main_list.append(proveedor[3]) #Posicion 3
            not_main_list.append(proveedor[4]) #Posicion 4
            not_main_list.append(proveedor[5]) #Posicion 5
            not_main_list.append(proveedor[6]) #Posicion 6
            not_main_list.append(proveedor[7]) #Posicion 7
            not_main_list.append(proveedor[8]) #Posicion 8
            not_main_list.append(proveedor[9]) #Posicion 9
            not_main_list.append(proveedor[10]) #Posicion 10
            not_main_list.append(proveedor[11]) #Posicion 11
            not_main_list.append(proveedor[12]) #Posicion 12
            not_main_list.append(proveedor[13]) #Posicion 13
            not_main_list.append(proveedor[14]) #Posicion 14
            not_main_list.append(proveedor[15]) #Posicion 15
            not_main_list.append(proveedor[16]) #Posicion 16
            not_main_list.append(proveedor[17]) #Posicion 17
            not_main_list.append(proveedor[18]) #Posicion 18
            not_main_list.append(proveedor[19]) #Posicion 19
            not_main_list.append(proveedor[20]) #Posicion 20
            not_main_list.append(proveedor[21]) #Posicion 21
            not_main_list.append(proveedor[22]) #Posicion 22

            temporal_list.append(not_main_list) #Lista donde se almacena lo encontrado
    self.lista=temporal_list

def tabla_de_estado(self):
    
    self.ui.tabla.clear()
    self.ui.tabla.setColumnCount(23)
    headers = ['Estado','Ciudad','Colonia','Oficio1','Oficio2','Oficio3','Oficio4','Oficio5','Oficio6','Nombre','Telefono','Celular','Producto1','Producto2','Producto3','Producto4','Producto5','Producto6','Empresa','Link','Dirección','Correo electrónico','Recomienda']
    self.ui.tabla.setHorizontalHeaderLabels(headers)
    self.ui.tabla.setRowCount(len(self.lista))
    self.ui.tabla.setColumnWidth(0,150)
    self.ui.tabla.setColumnWidth(1,150)
    self.ui.tabla.setColumnWidth(2,175)
    self.ui.tabla.setColumnWidth(3,150)
    self.ui.tabla.setColumnWidth(4,150)
    self.ui.tabla.setColumnWidth(5,150)
    self.ui.tabla.setColumnWidth(6,150)
    self.ui.tabla.setColumnWidth(7,150)
    self.ui.tabla.setColumnWidth(8,150)
    self.ui.tabla.setColumnWidth(9,150)
    self.ui.tabla.setColumnWidth(12,150)
    self.ui.tabla.setColumnWidth(13,150)
    self.ui.tabla.setColumnWidth(14,150)
    self.ui.tabla.setColumnWidth(15,150)
    self.ui.tabla.setColumnWidth(16,150)
    self.ui.tabla.setColumnWidth(17,150)
    self.ui.tabla.setColumnWidth(21,300)

    row=0

    for proveedor in self.lista:

        mostrar_lista=[]
        for informacion in self.lista[row]:
            mostrar_lista.append(informacion)

        colonia_widget = QTableWidgetItem(mostrar_lista[3])
        ciudad_widget = QTableWidgetItem(mostrar_lista[6])
        estado_widget = QTableWidgetItem(mostrar_lista[7])
        oficio1_widget = QTableWidgetItem(mostrar_lista[17])
        oficio2_widget = QTableWidgetItem(mostrar_lista[18])
        oficio3_widget = QTableWidgetItem(mostrar_lista[19])
        oficio4_widget = QTableWidgetItem(mostrar_lista[20])
        oficio5_widget = QTableWidgetItem(mostrar_lista[21])
        oficio6_widget = QTableWidgetItem(mostrar_lista[22])
        nombre_widget = QTableWidgetItem(mostrar_lista[0])
        telefono_widget = QTableWidgetItem(mostrar_lista[4])
        celular_widget = QTableWidgetItem(mostrar_lista[5])
        producto1_widget = QTableWidgetItem(mostrar_lista[11])
        producto2_widget = QTableWidgetItem(mostrar_lista[12])
        producto3_widget = QTableWidgetItem(mostrar_lista[13])
        producto4_widget = QTableWidgetItem(mostrar_lista[14])
        producto5_widget = QTableWidgetItem(mostrar_lista[15])
        producto6_widget = QTableWidgetItem(mostrar_lista[16])
        empresa_widget = QTableWidgetItem(mostrar_lista[1])
        link_widget = QTableWidgetItem(mostrar_lista[10])
        direccion_widget = QTableWidgetItem(mostrar_lista[2])
        correo_electronico_widget = QTableWidgetItem(mostrar_lista[9])
        recomienda_widget = QTableWidgetItem(mostrar_lista[8])

        self.ui.tabla.setItem(row, 0, estado_widget)
        self.ui.tabla.setItem(row, 1, ciudad_widget)
        self.ui.tabla.setItem(row, 2, colonia_widget)
        self.ui.tabla.setItem(row, 3, oficio1_widget)
        self.ui.tabla.setItem(row, 4, oficio2_widget)
        self.ui.tabla.setItem(row, 5, oficio3_widget)
        self.ui.tabla.setItem(row, 6, oficio4_widget)
        self.ui.tabla.setItem(row, 7, oficio5_widget)
        self.ui.tabla.setItem(row, 8, oficio6_widget)
        self.ui.tabla.setItem(row, 9, nombre_widget)
        self.ui.tabla.setItem(row, 10, telefono_widget)
        self.ui.tabla.setItem(row, 11, celular_widget)
        self.ui.tabla.setItem(row, 12, producto1_widget)
        self.ui.tabla.setItem(row, 13, producto2_widget)
        self.ui.tabla.setItem(row, 14, producto3_widget)
        self.ui.tabla.setItem(row, 15, producto4_widget)
        self.ui.tabla.setItem(row, 16, producto5_widget)
        self.ui.tabla.setItem(row, 17, producto6_widget)
        self.ui.tabla.setItem(row, 18, empresa_widget)
        self.ui.tabla.setItem(row, 19, link_widget)
        self.ui.tabla.setItem(row, 20, direccion_widget)
        self.ui.tabla.setItem(row, 21, correo_electronico_widget)
        self.ui.tabla.setItem(row, 22, recomienda_widget)
                
        row+=1
    proveedores_encontrados = len(self.lista)
    QMessageBox.information(
    self,
    'CONTACTOS ENCONTRADOS',
    f'Se encontraron "{proveedores_encontrados}" contactos')