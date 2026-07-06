---
title: 'Liquid objects: color_scheme_group'
description: >-
  A color_scheme_group from a [`color_scheme_group`
  setting](/themes/architecture/settings/input-settings#color_scheme_group).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/color_scheme_group'
  md: 'https://shopify.dev/docs/api/liquid/objects/color_scheme_group.md'
api_name: liquid
---

# color\_​scheme\_​group

A color\_scheme\_group from a [`color_scheme_group` setting](https://shopify.dev/themes/architecture/settings/input-settings#color_scheme_group).

***

**Tip:** To learn about color schemes in themes, refer to \<a href="/themes/architecture/settings/input-settings#color\_scheme">\<code>\<span class="PreventFireFoxApplyingGapToWBR">color\<wbr/>\_scheme\</span>\</code> setting\</a>.

***

##### Example

```json
{}
```

### Referencing color\_scheme\_group settings directly

##### Code

```liquid
{% for scheme in settings.color_schemes %}
  .color-{{ scheme.id }} {
    --color-background: {{ scheme.settings.background }};
    --color-text: {{ scheme.settings.text }};
  }
{% endfor %}
```

##### Data

```json
{
  "settings": {
    "color_schemes": {}
  }
}
```

##### Output

```html
.color-background-1 {
    --color-background: #FFFFFF;
    --color-text: #121212;
  }

  .color-background-2 {
    --color-background: #F3F3F3;
    --color-text: #121212;
  }

  .color-inverse {
    --color-background: #121212;
    --color-text: #FFFFFF;
  }

  .color-accent-1 {
    --color-background: #121212;
    --color-text: #FFFFFF;
  }

  .color-accent-2 {
    --color-background: #334FB4;
    --color-text: #FFFFFF;
  }
```
