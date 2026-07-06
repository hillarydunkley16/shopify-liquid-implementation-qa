---
title: 'Liquid objects: font'
description: >-
  A font from a [`font_picker`
  setting](/themes/architecture/settings/input-settings#font_picker).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/font'
  md: 'https://shopify.dev/docs/api/liquid/objects/font.md'
api_name: liquid
---

# font

A font from a [`font_picker` setting](https://shopify.dev/themes/architecture/settings/input-settings#font_picker).

You can use the `font` object in Liquid [assets](https://shopify.dev/themes/architecture#assets) or inside a [`style` tag](https://shopify.dev/docs/api/liquid/tags/style) to apply font setting values to theme CSS.

***

**Tip:** Use \<a href="/docs/api/liquid/filters/font-filters">font filters\</a> to modify properties of the \<code>font\</code> object, load the font, or obtain font variants.

***

## Properties

* * **baseline\_​ratio**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The baseline ratio of the font as a decimal.

  * **fallback\_​families**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The fallback families of the font.

  * **family**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The family name of the font.

    **Tip:** If the family name contains non-alphanumeric characters (A-Z, a-z, 0-9, or \&#39;-\&#39;), then it will be wrapped in double quotes.

  * **style**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The style of the font.

  * **system?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the font is a system font. Returns `false` if not.

    **Tip:** You can use this property to determine whether you need to include a corresponding \<a href="/docs/api/liquid/filters/font\_face">font-face\</a> declaration for the font.

  * **variants**

    array of [font](https://shopify.dev/docs/api/liquid/objects/font)

  * The variants in the family of the font.

  * **weight**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The weight of the font.

##### Example

```json
{
  "baseline_ratio": 0.133,
  "fallback_families": "sans-serif",
  "family": "Assistant",
  "style": "normal",
  "system?": false,
  "variants": {},
  "weight": "400"
}
```
