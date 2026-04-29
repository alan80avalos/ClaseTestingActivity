# Google Search Test con TypeScript y Playwright
Este proyecto contiene pruebas automatizadas usando **TypeScript** y **Playwright**.

La prueba realiza búsquedas en Google con diferentes términos y verifica que la búsqueda se haya realizado correctamente.

## Tecnologías utilizadas
- TypeScript
- Playwright
- Node.js
- npm

Antes de ejecutar el proyecto, es necesario tener instalado:
- Node.js
- npm

correr pruebas:
- npx playwright test
En caso de que salga el "no soy un robot" se podria forzar a que solo ejecute uno a la vez con:
- npx playwright test tests/googleSearch.spec.ts --headed --workers=1

## Nota:
En mi caso google me muestra la verificación de "no soy un robot" por que detecto automatización en el navegador, siendo que tengo la sospecha que podria ser por que al principio intente realizar las pruebas con mas "Workers" y Google detecto como actividad sospechosa.
Siendo que intente bajar los workers, quitar el test de ejemplo, subir el timeout, cambiar el tipo de navegador de chrome que abre de navegador de pruebas a navegador normal mediante el .config y no cambio mucho más que el tiempo de ejecución. 
Pero es probable que si es la primea vez que se ejecuta sea de forma satisfactoria al Google no mostrar el captcha.