# Índice

- [Introducción](#introducción)
- [Políticas de seguridad generales](#políticas-de-seguridad-generales)
    - [Políticas de contraseñas](#políticas-de-contraseñas)
    - [Política de uso de VPN](#política-de-uso-de-vpn)
    - [Política de configuración de VPN](#política-de-configuración-de-vpn)
    - [Política de Correo Eletrónico](#políticas-de-correo-electrónico)
    - [Política de dispositivos de la empresa](#políticas-de-dispositivos-empresa)
    - [Política de tarjetas de identificación](#políticas-de-tarjetas-de-identficación)
    - [Política de autenticación biométrica de huella dactilar](#política-de-identificación-de-huella-dactilar)

# Introducción

Este documento establece las políticas de seguridad que nuestra empresa ha implementado para proteger sus activos digitales y físicos. Estas políticas son obligatorias para todos los empleados y colaboradores de la empresa.

Las políticas de seguridad descritas en este documento abarcan varios aspectos, incluyendo la gestión de contraseñas, el uso y configuración de VPN, y la identificación de huella dactilar. Cada política tiene como objetivo mitigar los riesgos asociados a cada área y proporcionar directrices claras sobre las mejores prácticas a seguir.

Es responsabilidad de todos los empleados y colaboradores leer, entender y adherirse a estas políticas. El incumplimiento de estas políticas puede resultar en acciones disciplinarias, hasta e incluyendo la terminación del empleo.

Gracias por su cooperación para mantener la seguridad de nuestra empresa.

# Políticas de seguridad generales

A continuación se presentan una serie de políticas de seguridad aplicables a los distintos ámbitos y mecanismos de autenticación de nuestra empresa:

## Políticas de contraseñas

En nuestra empresa no existe una política de contraseña creadas para los empleados, por lo tanto, teniendo en cuenta que la mayoría de servicios que usamos en la empresa vienen precedidos por un sistema de autenticación para obtener una mayor seguridad, se han recogido las buenas prácticas que el empleado debe seguir para crear, modificar y usar las contraseñas.

**Activos relacionados:**

Dispositivos, cuentas de usuario, información de la empresa y del usuario.

**Riesgos asociados**

- Robo de cuentas de usuario al colocar contraseñas a la vista de los demás o
compartirlas.
- Robo de contraseñas a través de gestores de contraseñas de los navegadores.
- Contraseñas fáciles de descifrar.

**Políticas y directrices**

- Las contraseñas deben cumplir un mínimo de requisitos para su uso:
    - Al menos deben tener un mínimo de 10 caracteres.
    - Deberían estar construidas evitando antipatrones como incluir información personal, terminar en números o sustituir vocales por números. Es aconsejable por ejemplo elegir 4 palabras al azar.
- Las contraseñas deben ser cambiadas periódicamente al menos cada 6 meses
dependiendo de su criticidad.
- Obligatorio usar autenticación de doble factor para servicios con información sensible.
- Las contraseñas no deben ser colocadas en post-it, papeles dejados a simple vista o
compartirla con otro compañero. Las contraseñas de usuario nunca serán pedidas por
la empresa a los empleados.
- Se prohíbe el uso del recordatorio de contraseñas de las páginas web cuando nos
autenticamos con un usuario.

## Política de uso de VPN

Los trabajadores de la empresa autorizados al uso de VPN deben saber cómo realizar las
conexiones y en qué situación para garantizar la seguridad de la información.
Activos relacionados:
Dispositivos, cuentas de usuario, información de la empresa y del usuario.

**Riesgos:**

- El mal uso de la VPN por parte de los empleados de la empresa puede conllevar la
filtración de las credenciales de los trabajadores lo que puede permitir accesos no
autorizados a los sistemas.

**Políticas y directrices:**

- Se prohíbe a los trabajadores compartir las credenciales de acceso.
- Los trabajadores serán los responsables de actualizar el software de VPN a la versión
que establezca la empresa en cualquier momento.
- En el caso de pérdida o robo del dispositivo que tenga acceso a la VPN, el trabajador
deberá notificar a la empresa de manera inmediata.
- La VPN solo se utilizará en estos casos:
    - Cuando los empleados trabajen desde su casa.
    - Cuando se quiera conectar desde una de las sedes a la otra de manera segura.
    - Cuando se utilicen redes públicas.
    - Cuando se necesite realizar operaciones que impliquen el traspaso de información confidencial.

## Política de configuración de VPN

Todos los accesos externos hacia la empresa se realizarán mediante una conexión VPN de
manera que solo las personas autorizadas tengan acceso para garantizar la seguridad de los
datos.

**Activos relacionados:**

Dispositivos, cuentas de usuario, información de la empresa y del usuario.

**Riesgos:**

Si el servicio VPN no está configurado correctamente se pueden dar estos riesgos:

- Accesos no autorizados a la red de la empresa.
- Intercepción de datos durante la transmisión de información.
- Vulnerabilidades que pueden ser explotadas por atacantes.

**Políticas y directrices:**

El departamento de TIC deberá configurar el servicio VPN:

- Asignar los permisos adecuados a las cuentas de usuario.
- Especificar el software permitido para realizar las conexiones VPN, en nuestro caso wireguard.
- Monitorizar quien se conecta y quien no a través de la VPN.
- Asegurar la custodia de las claves públicas 

## Políticas de Correo Electrónico

El correo electrónico es crucial en el funcionamiento de una empresa, y ofrece beneficios como
accesibilidad y rapidez, pero su seguridad inicialmente subestimada lo convierte en un blanco
para ciberdelincuentes. Los empleados pueden cometer errores perjudiciales, desde enviar
información confidencial a destinatarios equivocados hasta caer en trampas de phishing.

**Activos relacionados:**

- Cuentas de correo electrónico, clientes y servidores dedicados a dicho fin

**Riesgos**

- Blanco de ataques de ingeniería social
- Abrir archivos adjuntos con carácter malicioso
- Fugas de información

**Políticas y directrices**

- Desactivar elementos no seguros tales como el HTML, la ejecución de macros y la
descarga de imágenes
- Usar una contraseña segura para acceder al correo
- No publicar las direcciones de correo corporativas en páginas web ni en redes sociales
sin utilizar técnicas de ofuscación
- Instalar aplicaciones antimalware y activar los filtros antispam tanto en el servidor
como en el cliente de correo
- Se debe instalar una tecnología de cifrado y firma digital para proteger la información
confidencial. Normalmente esta será Bitlocker, pero consultar al departamento de IT si se tiene posesión de información clasificada.
- Identificar al remitente y sospechar de la autenticidad del correo cuando el mensaje
solicita hacer algo no habitual
- Analizar cuidadosamente los adjuntos de correos de remitentes desconocidos antes de
abrirlos

## Políticas de dispositivos empresa

Los dispositivos extraíbles son medios de transporte de información que pueden llegar a contener
información sensible o ser un vector de ataque para un posible malware.


**Activos relacionados**

- Movil dispuesto por la empresa
- Portátil dispuesto por la empresa

**Riesgos asociados**

- Posibilidad de extravío o robo.
- Infección de equipos debido a la acción de un malware.
- Filtración de información sensible contenida en uno de los dispositivos.
- Pérdida de la información debido al mal funcionamiento del dispositivo.

**Políticas y directrices**

- No utilizar dispositivos que provengan del exterior, personales o no
autorizados ni registrados por la empresa.
- No se debe almacenar información que no sea estrictamente necesaria para el desarrollo normal del trabajo.
- Debe mantenerse un registro de dispositivos autorizados para su uso.
- Debe mantenerse un registro de usuarios asignados al uso o custodia de los
dispositivos extraíbles autorizados.
- Debe evaluarse la información que se va a contener en el dispositivo,
valorando si es necesario el cifrado de los datos o no en base a su relevancia.
- Deberán considerarse múltiples alternativas antes de optar por el uso de dispositivos
extraíbles, como carpetas compartidas, repositorios privados de la empresa o el
servicio privado de nube del que la empresa dispone.
- En caso de necesidad de transportar el dispositivo, deberá hacerse usando una funda
protectora adecuada.

## Políticas de tarjetas de identficación

Las tarjetas de identificación son personales e intransferibles, propias de cada empleado. En ellas se incluye el nombre, apellidos, chip inteligente con el id de tarjeta y los certificados necesarios para autenticarse en los sistemas.

**Activos relacionados**

- Material contenido en la oficina, ya que con ella se accede a la misma.
- Servidores y equipos contenido en la sala de servidores.

**Riesgos asociados**

- Posibilidad de extravío o robo.
- Posibilidad de *skimming* (Robo de los datos de la tarjeta para su posterior clonado o duplicación)
- Falsificación de la estética de la tarjeta (usada con la premeditación de aparentar ser oficial, sin tener intención de usarla en ningún sistema)

**Políticas y directrices**

- Llevar la tarjeta al lugar de trabajo de una manera segura, guardada en un tarjetero o útil de transporte apropiado. Existen carcasas protectoras que no permiten el paso de las ondas electromagnéticas y son útiles para estos elementos de seguridad. No llevarla suelta, ni mezclarla con otras tarjetas.
- Una vez en el lugar de trabajo, llevarla visible prefereiblemente en un colgante con funda plastificada.
- No dejarse fotografiar mientras se dispone del colgante
- Debe mantenerse un registro de usuarios y sus respectivas tarjetas asignadas.

## Política de Identificación de Huella Dactilar

En nuestra empresa, utilizamos la identificación de huella dactilar como una forma de autenticación biométrica para garantizar la seguridad de los datos y los dispositivos.

**Activos relacionados:**

Dispositivos con lectores de huellas dactilares, cuentas de usuario, información de la empresa y del usuario.

**Riesgos asociados:**

- Uso no autorizado de dispositivos al obtener huellas dactilares de los empleados.
- Robo de identidad a través de la falsificación de huellas dactilares.

**Políticas y directrices:**

- Las huellas dactilares registradas en los dispositivos deben ser de los propietarios de las cuentas de usuario correspondientes.
- Los empleados deben limpiar regularmente los lectores de huellas dactilares para garantizar su correcto funcionamiento.
- En caso de daño o mal funcionamiento del lector de huellas dactilares, el empleado debe notificarlo inmediatamente al departamento de TI.
- En caso de terminación del empleo, las huellas dactilares del empleado deben ser eliminadas de todos los dispositivos y sistemas.
