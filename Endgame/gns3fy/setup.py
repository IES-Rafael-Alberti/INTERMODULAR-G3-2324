import gns3fy

# Objeto del server para establecer la conexión
#gns3_server = gns3fy.Gns3Connector("http://192.168.1.73:80", "p4c?p0uSo", "Ce$F6qo=i@.xQO~xaCf.O@CHt") // Conexión en clase

gns3_server = gns3fy.Gns3Connector("http://localhost:3080")

# Selecciona el proyecto adecuado (lo llamamos laboratorio, lab vamos)
lab = gns3fy.Project(name="multi", connector=gns3_server)

lab.get()

nat = lab.create_node(name="Nat", template="NAT", x=0, y=0)
router = lab.create_node(name="router", template="OpenWrt 23.05.0", x=0, y=200)
router = lab.nodes[-1]  # Asignamos el último objeto creado para tenerlo en esa variable.

#router = lab.create_node(name="router", template="OpenWrt 22.03.0", x=100, y=200)
pc1 = lab.create_node(name="PC1-UbuntuServerMinecraft", template="Ubuntu Desktop Guest 22.04", x=100, y=300)
pc1 = lab.nodes[-1]

pc2 = lab.create_node(name="PC2-UbuntuClient", template="Ubuntu Desktop Guest 22.04", x=50, y=400)
pc2 = lab.nodes[-1]

pc3 = lab.create_node(name="PC3-WindowsServer", template="Windows Server 2022", x=400, y=0)
pc3 = lab.nodes[-1]

# Configura el nodo crítico que es PC1 para tener 3 interfaces
pc1.update(properties={"adapters": 3})

# Configuración de red para PC2
data_pc1 = '''
# La primera interfaz obtiene una dirección IP automáticamente a través de DHCP
auto eth0
iface eth0 inet dhcp

# La segunda interfaz tiene una dirección IP estática en la red 192.168.2.0
auto eth1
iface eth1 inet static
    address 192.168.2.X  # Reemplaza X con un número único para PC1 en la red 192.168.2.0
    netmask 255.255.255.0
'''

# Escribe la nueva configuración en el archivo de PC2
print("Escribiendo archivo de configuración /etc/network/interfaces en PC 1")
pc1.write_file(path='/etc/network/interfaces', data=data_pc1)
print(pc1.get_file("/etc/network/interfaces"))
### Luego, crea los enlaces entre los nodos

# Conecta el router con el NAT
lab.create_link("Nat", "nat0", "router", "Ethernet1")
lab.create_link("router", "Ethernet0", "PC1-UbuntuServerMinecraft", "eth0")
lab.create_link("PC1-UbuntuServerMinecraft", "eth1", "PC2-UbuntuClient", "eth0")
lab.create_link("PC1-UbuntuServerMinecraft", "eth2", "PC3-WindowsServer", "NIC1")

lab.start_nodes()
    
