---
title: 'Liquid objects: settings'
description: >-
  Allows you to access all of the theme's settings from the
  [`settings_schema.json`
  file](/themes/architecture/config/settings-schema-json).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/settings'
  md: 'https://shopify.dev/docs/api/liquid/objects/settings.md'
api_name: liquid
---

# settings

Allows you to access all of the theme's settings from the [`settings_schema.json` file](https://shopify.dev/themes/architecture/config/settings-schema-json).

***

**Tip:** To learn about the available setting types, refer to \<a href="/themes/architecture/settings/input-settings">Input settings\</a>.

***

### Directly accessible in

* Global

### Reference a setting value

##### Code

```liquid
{% if settings.favicon != blank %}
  <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
{% endif %}
```

##### Data

```json
{
  "settings": {
    "favicon": null
  }
}
```
