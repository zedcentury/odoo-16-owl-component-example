# Odoo 16 owl component example

`counter` komponentining kodi `dev/owl_component/static/src/counter` ichida joylashgan:

* `counter.js` - funksionallik
* `counter.scss` - style
* `counter.xml` - skelet
* `index.js` - bu faylda komponent `id="counter"` bo'lgan elementga mount qilishi yozilgan

`views/components.xml` faylida template yozilgan id qiymati biriktirilgan

`views/templates.xml` faylida komponentdan foydalanilgan va ushbu template controller'da `/owl-component/example-page`
manzilida bog'langan.

`__manifest__.py` faylida quyidagi kodlar qo'shish kerak:

```text
'data': [
    ...
    'views/components.xml',
],

...

'assets': {
    'web.assets_frontend': [
        'owl_component/static/src/**/*'
    ],
}
```