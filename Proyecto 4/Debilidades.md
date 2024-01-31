# vulnerabilidades, tipos de ataques y mitigación de los sistemas de acceso escogidos

## Índice

1. [Código OTP de 2FA](#código-otp-de-2fa)</br>
1.1 [Principales vulnerabilidades de OTP de 2FA](#principales-vulnerabilidades-de-otp-de-2fa)</br>
1.2 [Tipos de ataques de OTP de 2FA](#tipos-de-ataques-de-otp-de-2fa)</br>
1.3 [Mitigación de OTP de 2FA](#mitigación-de-otp-de-2fa)</br>
2. [Tarjeta de identificación](#tarjeta-de-identificación)</br>
2.1 [Principales vulnerabilidades de Tarjeta de identificación](#principales-vulnerabilidades-de-tarjeta-de-identificación)</br>
2.2 [Tipos de ataques de Tarjeta de identificación](#tipos-de-ataques-de-tarjeta-de-identificación)</br>
2.3 [Mitigación de Tarjeta de identificación](#mitigación-de-tarjeta-de-identificación)</br>
2. [Lector de huella dactilar](#lector-de-huella-dactilar)</br>
3.1 [Principales vulnerabilidades de Lector de huella dactilar](#principales-vulnerabilidades-de-lector-de-huella-dactilar)</br>
3.2 [Tipos de ataques de Lector de huella dactilar](#tipos-de-ataques-de-lector-de-huella-dactilar)</br>
3.3 [Mitigación de Lector de huella dactilar](#mitigación-de-lector-de-huella-dactilar)</br>
4. [Contraseña personal](#contraseña-personal)</br>
4.1 [Principales vulnerabilidades de Contraseña personal](#principales-vulnerabilidades-de-contraseña-personal)</br>
4.2 [Tipos de ataques de Contraseña personal](#tipos-de-ataques-de-contraseña-personal)</br>
4.3 [Mitigación de Contraseña personal](#mitigación-de-contraseña-personal)</br>
5. [Clave asimétrica Wireguard](#clave-asimétrica-wireguard)</br>
5.1 [Principales vulnerabilidades de Clave asimétrica Wireguard](#principales-vulnerabilidades-de-clave-asimétrica-wireguard)</br>
5.2 [Tipos de ataques de Clave asimétrica Wireguard](#tipos-de-ataques-de-clave-asimétrica-wireguard)</br>
5.3 [Mitigación de Clave asimétrica Wireguard](#mitigación-de-clave-asimétrica-wireguard)</br>

## Código OTP de 2FA

### Principales vulnerabilidades de OTP de 2FA:

- **Algoritmo predecible:** Si el algoritmo es predecible, se podría generar un OTP valido.
- **Canales de transmisión no seguros:** Los canales por donde se envían los códigos pueden ser interceptados al ser menos seguros, por ejemplo si es a través de sms o de correo electrónico.
- **Fallos humanos:** Si el dispositivo se pierde o es robado, se puede acceder a través de este.

### Tipos de ataques de OTP de 2FA:

- **Phishing:** Alguien podría hacerse pasar por la página web a la cual se accede para el correo electrónico corporativo y pedir la clave que se envia al empleado por sms.
- **Ataques de fuerza bruta:** Un ciberdelincuente podría usar un generador de códigos valido para ir probando y acabar obteniendo acceso.
- **Ataques de Man in the middle:** Un ciberdelincuente puede obtener el código y por lo tanto acceder interceptando la comunicación.
- **Robo:** Alguien podría robar el dispositivo móvil del empleado para obtener el código OTP.

### Mitigación de OTP de 2FA:

- **Algoritmo predecible:** Utilizando el algoritmo TOTP que usa un intervalo de tiempo para utilizar el código OTP.
- **Canales de transmisión no seguros:** En vez de utilizar el correo electrónico, se usará sms a través del dispositivo móvil corporativo que es más complicado de vulnerar si se sigue la política de seguridad referente a los dispositivos corporativos.
- **Fallos humanos:** Plan de concienciación cada 6 meses.

## Tarjeta de identificación

### Principales vulnerabilidades de Tarjeta de identificación:

- **Fallos humanos:** Si la tarjeta se pierde o es robado, se puede acceder a través de este.
- **Facilidad de duplicación:** Las tarjetas pueden ser clonadas copiando la información de la misma.
- **Transmisión insegura:** Los datos que se transmiten desde la tarjeta al lector pueden ser interceptados.
- **Facilidad de falsificar:** Se pueden fabricar tarjetas con una identificación falsa.

### Tipos de ataques de Tarjeta de identificación:

- **Robo:** Alguien puede robar la tarjeta de un empleado con acceso a lugares criticos de la empresa para obtener ese acceso.
- **Clonación de tarjeta:** Un ciberdelincuente puede clonar el chip de la tarjeta inteligente para obtener los certificados que permiten la comprobación para el acceso.
- **Ataque de Man in the middle:** Un ciberelincuente podría interceptar la comunicación del hardware del lector de tarjetas con la base de datos.
- **Malware:** Un malware podría vulnerar el software que comprueba el certificado que contiene la tarjeta con la base de datos que contiene la comprobación de que el certificado es valido.

### Mitigación de Tarjeta de identificación:

- **Fallos humanos:** Plan de concienciación cada 6 meses.
- **Facilidad de duplicación:** Uso de tarjetas inteligentes que aún siendo posible su clonación, contiene mecanismos de seguridad avanzado que dificultan esta clonación.
- **Transmisión insegura:** El dispositivo que comprueba la identificación será el que contenga la base de datos para la comprobación.
- **Facilidad de falsificar:** Tanto la tarjeta inteligente como el dispositivo lector, tienen mecanismos de seguridad complica esta falsificación generando códigos por cada acceso y cifrando la información en el chip de la tarjeta con clave secreta que solo puede descifrar el dispositivo.

## Lector de huella dactilar

### Principales vulnerabilidades de Lector de huella dactilar:

- **Almacenamiento inseguro:** La base de datos donde se guarda la huella dactilar puede ser vulnerable o se guarda en texto sin cifrar facilitando su falsificación.
- **Facilidad de falsificar:** Las huellas dactilares pueden ser recreadas con silicona por ejemplo.
- **Fallos en el software o en el firmware:** Se podría aprovechar estos fallos para permitir acceso.

### Tipos de ataques de Lector de huella dactilar:

- **Ataques de suplantación:** Una persona podría conseguir replicar la huella de un empleado para acceder. 
- **Malware:** Un malware podría vulnerar el software que comprueba el hash de la huella dactilar con la base de datos que almacena el hash.
- **Ataques de inyección de datos a la base de datos:** Un atacante podría vulnerar la base de datos incluyendo el hash de su huella dactilar.

### Mitigación de Lector de huella dactilar:

- **Almacenamiento inseguro:** La base de datos que contiene el hash que se guarda y comprueba por cada huella dactilar será almacenado o en el dispositivo lector o en una máquina sin acceso a internet.
- **Facilidad de falsificar:** Es muy complicado que alguien consiga falsificar la huella utilizando silicona o a través de intentar obtenerla con celo, igualmente el acceso siempre será videovigilado ya que solo se podría hacer desde dentro de la empresa.
- **Fallos en el software o en el firmware:** Actualizar constantemente el software y el firmware del lector de la tarjeta.

## Contraseña personal

### Principales vulnerabilidades de Contraseña personal:

- **Contraseñas débiles:** Contraseñas pueden ser demasiado cortas y estar basadas en información personal.
- **Fallos humanos:** Podemos ser victimas de ataques de phishing entre otros.
- **Reutilización de las contraseñas:** Si usamos siempre la misma contraseña, un atacante que la consiga, puede tener acceso a todas nuestras cuentas.
- **Almacenamiento no seguro:** Las contraseñas pueden ser guardadas en texto plano en las bases de datos que puedan ser vulnerables.
- **Falta de 2FA:** La falta de autenticación de dos factores hacen más vulnerables las contraseñas.

### Tipos de ataques de Contraseña personal:

- **Phishing:** Un ciberdelincuente puede obtener la contraseña de un empleado suplantando a un administrador de sistema.
- **Ataques de fuerza bruta:** Un ciberdelincuente puede ir probando distintas contraseñas para intentar obtener acceso.
- **Ataques por diccionario:** Un ciberdelincuente puede utilizar un diccionario de contraseñas para intentar obtener la contraseña y acceder.
- **Keyloggers:** Un ciberdelincuente puede vulnerar un dispositivo de un empleado e instalar este malware para registrar las teclas del usuario. 
- **Man in the Middle:** Un ciberdelincuente podría interceptar la comunicacióny obtener la contraseña.

### Mitigación de Contraseña personal:

- **Contraseñas débiles:** A través de una política de seguridad robusta y plan de concienciación, se instará a usar constraseñas robustas y complicadas de vulnerar.
- **Fallos humanos:** Plan de concienciación cada 6 meses.
- **Reutilización de las contraseñas:** A través de la política de seguridad, instar a los empleados a no usar la contraseña de uso personal como contraseña corporativa y además a cambiar las contraseñas cada cierto tiempo.
- **Almacenamiento no seguro:** Cifrar las contraseñas que se usen en la empresa para los accesos con un hash.
- **Falta de 2FA:** En la empresa se ha implementado en las políticas de seguridad y en el acceso a varios sistemas de la misma, el uso de 2FA.

## Clave asimétrica Wireguard

### Principales vulnerabilidades de Clave asimétrica Wireguard:

- **Almacenamiento inseguro de claves:** Las claves generadas pueden ser almacenadas en máquinas vulnerables.
- **Mala configuración:** La configuración de Wireguard puede ser equivocada generando claves más cortas.

### Tipos de ataques de Clave asimétrica Wireguard:

- **Robo de claves generadas:** Un ciberdelincuente puede vulnerar la máquina de un empleado y obtener su clave privada para obtener acceso por vpn.

### Mitigación de Clave asimétrica Wireguard:

- **Almacenamiento inseguro de claves:** Se controlará regularmente los dispositivos corporativos para la comprobación de que no han sido vulnerados de alguna manera que haya permitido a un ciberdelincuente obtener acceso a la misma y modificar o usar estas claves.
- **Mala configuración:** En cada dispositivo corporativo con acceso a la vpn de wireguard que al configurarla, se compruebe que la configuración ha sido correcta.