---
title: 'Liquid objects: color'
description: >-
  A color from a [`color`
  setting](/themes/architecture/settings/input-settings#color).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/color'
  md: 'https://shopify.dev/docs/api/liquid/objects/color.md'
api_name: liquid
---

# color

A color from a [`color` setting](https://shopify.dev/themes/architecture/settings/input-settings#color).

***

**Tip:** Use \<a href="/docs/api/liquid/filters/color-filters">color filters\</a> to modify or extract properties of a \<code>color\</code> object.

***

## Properties

* * **alpha**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The alpha component of the color, which is a decimal number between 0.0 and 1.0.

  * **blue**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The blue component of the color, which is a number between 0 and 255.

  * **chroma**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The chroma component of the color, which is a decimal number between 0.0 and 0.5.

  * **color\_​space**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The color space of the color. Returns 'srgb' or 'oklch'

  * **green**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The green component of the color, which is a number between 0 and 255.

  * **hue**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The hue component of the color, which is a number between 0 and 360.

  * **lightness**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The lightness component of the color, which is a number between 0 and 100.

  * **oklch**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The lightness, chroma, and hue values of the color, represented as a space-separated string.

  * **oklcha**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The lightness, chroma, hue and alpha values of the color, represented as a space-separated string, with a slash before the alpha channel.

  * **red**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The red component of the color, which is a number between 0 and 255.

  * **rgb**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The red, green, and blue values of the color, represented as a space-separated string.

  * **rgba**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The red, green, blue, and alpha values of the color, represented as a space-separated string, with a slash before the alpha channel.

  * **saturation**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The saturation component of the color, which is a number between 0 and 100.

##### Example

```json
{
  "alpha": 1,
  "blue": 180,
  "chroma": 0.16,
  "color_space": "srgb",
  "green": 79,
  "hue": 227,
  "lightness": 45,
  "oklch": "47% 0.16 268",
  "oklcha": "47% 0.16 268 / 1.0",
  "red": 51,
  "rgb": "51 79 180",
  "rgba": "51 79 180 / 1.0",
  "saturation": 56
}
```

### Referencing color settings directly

When a color setting is referenced directly, the hexidecimal color code is returned.

##### Code

```liquid
{{ settings.colors_accent_2 }}
```

##### Data

```json
{
  "settings": {
    "colors_accent_2": "#334fb4"
  }
}
```

##### Output

```html
#334fb4
```
