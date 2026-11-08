<p align="center">
  <img src="../../assets/hokucat.png" width="100" height="100" alt="El gato negro de Hokucat y una estrella de color ámbar">
</p>

<h1 align="center">Hokucat</h1>

<p align="center"><strong>Fondos de pantalla animados para macOS</strong></p>

<p align="center">
  <a href="../../README.md">English</a> · <a href="../../README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · Español · <a href="README.fr.md">Français</a> · <a href="README.ar.md">العربية</a>
</p>

<p align="center"><strong><a href="https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.80/Hokucat-1.4.80.dmg">Descargar la versión preliminar v1.4.80</a></strong> · <a href="https://github.com/ar-gen-tin/hokucat/releases/download/v1.4.80/SHA256SUMS.txt">SHA-256</a> · <a href="../install-with-ai.md">Instalar con IA</a></p>

Explora tu biblioteca de fondos de pantalla, previsualiza un fondo y ajusta sus opciones disponibles en una sola ventana. Usa IA para crear tus propios fondos de pantalla.

<a href="../../assets/hokucat-demo.mp4"><img src="../../assets/hokucat-demo.gif" width="960" alt="Breve vista previa del gato Hokucat; haz clic para ver el vídeo de presentación editado"></a>

[Sitio oficial](https://hokucat.com/) · [Ver el vídeo](../../assets/hokucat-demo.mp4) · [Crear un fondo de pantalla](../ai-wallpapers.md) · [Preguntas frecuentes](../faq.md)

*El vídeo es una presentación editada de los fondos de pantalla. Las obras de terceros para PC que aparecen en los materiales de vista previa se utilizan únicamente para pruebas. Consulta los [autores y las páginas originales](../credits.md).*

<img src="../../assets/hokucat-dashboard.jpg" width="960" alt="Panel de fondos de pantalla de Hokucat con biblioteca, vista previa y ajustes juntos">

*Captura real del Panel de fondos de pantalla en la versión 1.4.73 para evaluación.*

## Prueba Hokucat

**La 1.4.80 es una versión preliminar firmada con Developer ID**, compatible con **macOS 13 o posterior** en Mac con **Apple Silicon o Intel**. Esta versión preliminar no está notarizada por Apple; macOS puede bloquear la primera apertura. Consulta las novedades en el [registro de cambios](../../CHANGELOG.md).

Descarga y abre el DMG, arrastra Hokucat a la carpeta Applications (Aplicaciones) y sigue estos pasos:

1. Abre Hokucat desde la carpeta Applications (Aplicaciones) y selecciona **Panel de fondos de pantalla…** en la barra de menús.
2. Elige un fondo. Previsualízalo y ajusta los controles disponibles para esa obra en la misma página.
3. Haz clic en **Aplicar fondo de pantalla**. Si utilizas más de una pantalla, elige primero la pantalla de destino.

## Personaliza tu escritorio

- **Una biblioteca para explorar.** Busca un fondo, organiza la colección manualmente u ordénala por nombre.
- **Vista previa y ajustes juntos.** Ve la obra seleccionada junto a sus controles. En los vídeos compatibles, ajusta el encuadre, la velocidad y la inversión horizontal antes de aplicar el fondo.
- **Gestión sencilla de la biblioteca.** Arrastra las entradas para reordenarlas, usa el menú del botón derecho para las acciones habituales y elimina fondos importados tras confirmar. Los archivos originales permanecen donde estaban.
- **Interacciones familiares en el Mac.** Accede a Hokucat desde la barra de menús, sigue usando los controles habituales del escritorio y juega con la mirada del gato y la estrella que puedes arrastrar. Las interacciones disponibles dependen de cada fondo.
- **Una elección para cada pantalla.** Usa un fondo distinto en cada pantalla conectada. Hokucat recuerda tus elecciones.

La interfaz de la aplicación está disponible en **inglés, chino simplificado, chino tradicional, japonés, coreano, portugués de Brasil, español, francés y árabe**. Elige el idioma en Ajustes.

## Crea un fondo de pantalla con IA

Usa Codex, Claude Code o Grok Bot para crear un vídeo original en bucle y sin sonido, o utiliza un vídeo para el que tengas permiso de uso. La [guía de creación](../ai-wallpapers.md) incluye un prompt y un ejemplo ejecutable que genera un paquete listo para **Panel de fondos de pantalla → Importar…**.

Package v1 admite **imágenes PNG/JPEG y vídeos MP4/MOV/M4V sin sonido**. La IA ayuda a crear el contenido; Hokucat reproduce los archivos importados de forma local. Los proyectos interactivos genéricos de Web o Windows Scene, la entrada de puntero o audio en tiempo real y las conexiones en tiempo real con API o agentes quedan fuera de este formato de paquete. Algunos fondos integrados o adaptados pueden tener sus propias funciones interactivas.

La animación generada por código en [`examples/make-wallpaper.py`](../../examples/make-wallpaper.py) es un ejemplo independiente creado para este repositorio. Es distinto de los fondos de terceros para PC que se muestran para pruebas.

## Preguntas, comentarios y créditos

Lee las [preguntas frecuentes](../faq.md) para conocer los detalles de compatibilidad e importación, o [comunica un problema](https://github.com/ar-gen-tin/hokucat/issues) indicando las versiones de macOS y Hokucat y los pasos para reproducirlo. Las mejoras en la documentación, las traducciones y los ejemplos son bienvenidas. Consulta la [guía de contribución](../../CONTRIBUTING.md).

Este repositorio contiene la documentación pública, los materiales de presentación y el ejemplo de creación. **No contiene el código fuente completo de la aplicación para Mac.** Consulta los cambios documentados de la versión preliminar en el [historial de cambios](../../CHANGELOG.md).

Hokucat surgió a partir de [Grok Bot Wallpaper](https://github.com/Bodila51/grokbot-wallpaper), de **0xCodila (Bodila51)**. Las obras de terceros mantienen el crédito a sus creadores; mostrarlas en una versión de prueba no concede permiso para redistribuirlas. [Origen del proyecto y créditos de los materiales](../credits.md)
