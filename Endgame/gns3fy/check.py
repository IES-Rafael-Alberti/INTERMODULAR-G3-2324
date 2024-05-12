import gns3fy

# Objeto del server para establecer la conexión
#gns3_server = gns3fy.Gns3Connector("http://192.168.1.73:80", "p4c?p0uSo", "Ce$F6qo=i@.xQO~xaCf.O@CHt") // Conexión en clase

gns3_server = gns3fy.Gns3Connector("http://localhost:3080")

# Selecciona el proyecto adecuado (lo llamamos laboratorio, lab vamos)
lab = gns3fy.Project(name="multi", connector=gns3_server)

lab.get()

pc1 = lab.get_node('PC1-UbuntuServerMinecraft')

print(pc1.get_file("/etc/network/interfaces"))

    
data_pc1 = '''
# La primera interfaz obtiene una dirección IP automáticamente a través de DHCP
auto eth0
iface eth0 inet dhcp

# La segunda interfaz tiene una dirección IP estática en la red 192.168.2.0
auto eth1
iface eth1 inet static
    address 192.168.2.10  # Reemplaza X con un número único para PC1 en la red 192.168.2.0
    netmask 255.255.255.0
'''

# Escribe la nueva configuración en el archivo de PC2
print("Escribiendo archivo de configuración /etc/network/interfaces en PC 1")
pc1.write_file(path='/etc/network/interfaces', data=data_pc1)

print(pc1.get_file("/etc/network/interfaces"))