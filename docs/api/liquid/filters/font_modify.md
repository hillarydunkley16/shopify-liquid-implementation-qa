---
title: 'Liquid filters: font_modify'
description: Modifies a specific property of a given font.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/font_modify'
  md: 'https://shopify.dev/docs/api/liquid/filters/font_modify.md'
api_name: liquid
---

# font\_​modify

```oobleck
font | font_modify: string, string
```

returns [font](https://shopify.dev/docs/api/liquid/objects/font)

Modifies a specific property of a given font.

The `font_modify` filter requires two parameters. The first indicates which property should be modified and the second is either the new value, or modification amount, for that property.

***

**Tip:** You can access every variant of the chosen font\&#39;s family by using \<a href="/docs/api/liquid/objects/font#font-variants">\<code>font.variants\</code>\</a>. However, you can more easily access specific styles and weights by using the \<code>\<span class="PreventFireFoxApplyingGapToWBR">font\<wbr/>\_modify\</span>\</code> filter.

***

The following table outlines the valid font properties and modification values:

| Property | Modification value | Output |
| - | - | - |
| `style` | `normal` | Returns the normal variant of the same weight, if it exists. |
| `italic` | Returns the italic variant of the same weight, if it exists. | |
| `oblique` | Returns the oblique variant of the same weight, if it exists.Oblique variants are similar to italic variants in appearance. All Shopify fonts have only oblique or italic variants, not both. | |
| `weight` | `100` → `900` | Returns a variant of the same style with the given weight, if it exists. |
| `normal` | Returns a variant of the same style with a weight of `400`, if it exists. | |
| `bold` | Returns a variant of the same style with a weight of `700`, if it exists. | |
| `+100` → `+900` | Returns a variant of the same style with a weight incremented by the given value, if it exists.For example, if a font has a weight of `400`, then using `+100` would return the font with a weight of `500`. | |
| `-100` → `-900` | Returns a variant of the same style with a weight decremented by the given value, if it exists.For example, if a font has a weight of `400`, then using `-100` would return the font with a weight of `300`. | |
| `lighter` | Returns a lighter variant of the same style by applying the rules used by the [CSS `font-weight` property](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#Meaning_of_relative_weights) and browser [fallback weights](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#Fallback_weights), if it exists. | |
| `bolder` | Returns a bolder variant of the same style by applying the rules used by the [CSS `font-weight` property](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#Meaning_of_relative_weights) and browser [fallback weights](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight#Fallback_weights), if it exists. | |

##### Code

```liquid
{%- assign bold_font = settings.type_body_font | font_modify: 'weight', 'bold' -%}

h2 {
  font-weight: {{ bold_font.weight }};
}
```

##### Data

```json
{
  "settings": {
    "type_body_font": {}
  }
}
```

##### Output

```html
h2 {
  font-weight: 700;
}
```

### Non-existent font variants

If the `font_modify` filter tries to create a font variant that doesn't exist, then it returns `nil`. To handle this, you can either assign a fallback value with the [`default` filter](https://shopify.dev/docs/api/liquid/filters/default), or check for `nil` before using the variant.

##### Code

```liquid
{%- assign bold_font = settings.type_body_font | font_modify: 'weight', 'bold' -%}
{%- assign italic_font = settings.type_body_font | font_modify: 'style', 'italic' -%}
{%- assign heavy_font = settings.type_body_font | font_modify: 'weight', '900' | default: bold_font -%}
{%- assign oblique_font = settings.type_body_font | font_modify: 'style', 'oblique' | default: italic_font -%}

h2 {
  font-style: {{ heavy_font.weight }};
}

.italic {
  {% if oblique_font -%}
    font-style: {{ oblique_font.style }};
  {%- else -%}
    font-style: {{ italic_font.style }};
  {%- endif %}
}
```

##### Data

```json
{
  "settings": {
    "type_body_font": {}
  }
}
```

##### Output

```html
h2 {
  font-style: 700;
}

.italic {
  font-style: ;
}
```
