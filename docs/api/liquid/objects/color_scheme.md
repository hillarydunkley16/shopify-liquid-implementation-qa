---
title: 'Liquid objects: color_scheme'
description: >-
  A color_scheme from a [`color_scheme`
  setting](/themes/architecture/settings/input-settings#color_scheme).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/color_scheme'
  md: 'https://shopify.dev/docs/api/liquid/objects/color_scheme.md'
api_name: liquid
---

# color\_​scheme

A color\_scheme from a [`color_scheme` setting](https://shopify.dev/themes/architecture/settings/input-settings#color_scheme).

***

**Tip:** To learn about color scheme groups in themes, refer to \<a href="/themes/architecture/settings/input-settings#color\_scheme\_group">\<code>\<span class="PreventFireFoxApplyingGapToWBR">color\<wbr/>\_scheme\<wbr/>\_group\</span>\</code> setting\</a>.

***

## Properties

* * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the color\_scheme

  * **settings**

  * The [settings](https://shopify.dev/docs/themes/architecture/settings/input-settings#color_scheme_group) of the color\_scheme.

##### Example

```json
{
  "id": "background-2",
  "settings": {}
}
```

### Referencing color\_scheme settings directly

When a color\_scheme setting is referenced directly, the color scheme ID is returned.

##### Code

```liquid
{{ settings.card_color_scheme }}
```

##### Data

```json
{
  "settings": {
    "card_color_scheme": {}
  }
}
```

##### Output

```html
background-2
```
