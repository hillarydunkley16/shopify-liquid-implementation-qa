---
title: 'Liquid tags: style'
description: Generates an HTML `<style>` tag with an attribute of `data-shopify`.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/style'
  md: 'https://shopify.dev/docs/api/liquid/tags/style.md'
api_name: liquid
---

# style

Generates an HTML `<style>` tag with an attribute of `data-shopify`.

***

**Note:** If you reference \<a href="/docs/storefronts/themes/architecture/settings/input-settings#color">color settings\</a> inside \<code>style\</code> tags, then the associated CSS rules will update as the setting is changed in the theme editor, without a page refresh. See \<a href="/docs/storefronts/themes/tools/online-editor#color-settings">more information and limitations\</a> of live preview.

***

## Syntax

```oobleckTag
{% style %}
  CSS_rules
{% endstyle %}
```

### CSS\_rules

The desired CSS rules for the `<style>` tag.

##### Code

```liquid
{% style %}
  .h1 {
    color: {{ settings.colors_accent_1 }};
  }
{% endstyle %}
```

##### Data

```json
{
  "settings": {
    "colors_accent_1": "#121212"
  }
}
```

##### Output

```html
<style data-shopify>
  .h1 {
    color: #121212;
  }
</style>
```
