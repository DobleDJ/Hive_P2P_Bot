from config import manager,boturl

messages_about = {'es': rf"""
Este es un bot para la publicación y gestión de ofertas de intercambio P2P en HIVE.

Utilice los comandos:	
/start -Reiniciar la configuración de su usuario 🟢
/escrow -Conocer sobre  nuestro sistema de escrow en HIVE 🔄		
/hiveuser -Registrar su usuario de HIVE	👤	
/buy -Poner una orden de COMPRA	🔺	
/sell -Poner una orden de VENTA	🔻	
/cancel -Eliminar una orden	🔴	
/listorder -Mostrar el listado de órdenes activas	📝	
/prices -Conocer los precios de referencia según Coingecko y yadio.io 📈
/price -Conocer el precio de una moneda usando de referencia  Coingecko y yadio.io 💶
/msg -Enviar mensajes al canal de ofertas (Solo Admins) 🔐

Visite el canal de ofertas [Aquí]({boturl})		



Gracias!!
""", 'en': rf"""
This is a bot for publishing and managing P2P exchange offers on HIVE.

Use the commands:	
/start - Restart your user's settings 🟢
/escrow - Learn about our  escrow system in HIVE 🔄		
/hiveuser - Register your HIVE user 👤	
/buy - Place a purchase order 🔺	
/sell - Place a SELL order 🔻	
/cancel - Delete an order 🔴	
/listorder - Show the list of active orders 📝	
/prices -To know about the prices of reference according to Coingecko and yadio.io 📈
/price -To know the price of one currency using the reference Coingecko and yadio.io 💶
/msg - Send messages to the offers channel (Admins only) 🔐

Visit the offers channel [HERE]({boturl})		

Thank you!!
"""}

messages_support = {'es': """
 Puede plantear sus dificultades en el [grupo de Soporte](https://t.me/SoporteHiveCubaP2P)
""", 'en': """
You can raise your difficulties in the [support group](https://t.me/SoporteHiveCubaP2P)
"""}


messages_statU = {'es': """
Para usar este bot, debes activar tu nombre de usuario de Telegram. Para activarlo, abra el menú de hamburguesas en la esquina superior izquierda y seleccione: 

Configuración - > Editar perfil - > Nombre de usuario
""", 'en': """
To use this bot, you need to activate your Telegram username. To activate it, open the hamburger menu in the upper left corner and select: 

Settings - > Edit profile - > Username
"""}

messages_registre = {'es': """ 
No ha registrado su usuario de HIVE, utilice        
/hiveuser nombreUsuarioHive 
""", 'en': """
You have not registered your HIVE user, please use        
/hiveuser nameuserhive
"""}

messages_escrow = {'es': """
Vea el post en  `hivecuba` [HiveCuba P2P: ¿Como funciona?](https://ecency.com/hive-10053/@ertytux/hivecuba-p2p-como-funciona-es)
""", 'en': """
See the post on `hivecuba` [HiveCuba P2P: How does it work?](https://ecency.com/hive-10053/@ertytux/hivecuba-p2p-como-funciona-es)
"""}

messages_notHP = {'es': rf"""
Delegar Hive Power: Delegar  a la cuenta  `{manager}`  permite que el poder de voto de la comunidad sea cada vez mayor. Esto se traduce en una mayor capacidad para recompensar el contenido de calidad y apoyar a los creadores.  Es bueno recordarles que delegar no te da derecho a votos, el voto siempre dependerá del contenido. 

Al delegar a `{manager}` cubrimos los costos de operaciones de este bot. WIN-WIN 

Delegar, es basicamente decirle a la blockchain que los recursos y el poder de voto del Hive Power que vas a delegar se los de a otra cuenta. Nunca pierdes tu Hive Power.
""", 'en': rf"""
Delegating Hive Power: Delegating to the  account `{manager}` allows the voting power of the community to be increased every time. This translates into a greater ability to reward quality content and support creators.  It is good to remind them that delegating does not give you the right to votes, the vote will always depend on the content. 

By delegating to `{manager}` we cover the operating costs of this bot. WIN-WIN 

Delegating, is basically telling the blockchain that the resources and voting power of the Hive Power that you are going to delegate will be given to another account. You never lose your Hive Power.
"""}


messages_notSt={'es':"""
Debe registrar su usuario de HIVE para poder operar en nuestro bot:  
/hiveuser nombreUsuarioHive            
Además, si ha delegado al menos 50 HP a la cuenta  `{manager}` disfrutará cero comisiones.   
""",'en':"""
You must register your HIVE user in order to operate on our bot:  
/hiveuser nameuserhive            
In addition, if you have delegated at least 50 HP to our  account `{manager}` you will enjoy zero commissions.
"""}


