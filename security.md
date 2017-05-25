# Aspectos que te han tenido en cuenta en cuanto a seguridad en la aplicación.

## Autenticación

Para acceder a nuestra apliacion estamos usando la API de autenticacion para acceder con una cuenta de Google, dado que Google posee una estructura de autenticacion muy segura, incluso tiene acceso mediante validadción en dos pasos.

En cuanto al acceso a pestañas o funcionalidades de la aplicación, estamos usando nuestros propios mixins y usamos loginrequired()

## Formularios

Para la seguridad de formularios estamos usando el csrf token el cual evita ataques por cross site scripting.

## En cuanto al repositorio

No estamos entregando las llaves de seguridad de la aplicacion ni las llaves de seguirdad de la app de google que usamos para autenticación.

Si deseas mas información o conocer las llaves de la aplicación para aportar al proyecto puedes dejarme un mensaje, un comentario o escribirme al correo: jbeltranleon@gmail.com