---
title: 'Liquid filters: metafield_text'
description: >-
  Generates a text version of the data from a [`metafield`
  object](https://shopify.dev/docs/api/liquid/objects/metafield).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/metafield_text'
  md: 'https://shopify.dev/docs/api/liquid/filters/metafield_text.md'
api_name: liquid
---

# metafield\_​text

```oobleck
metafield | metafield_text
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a text version of the data from a [`metafield` object](https://shopify.dev/docs/api/liquid/objects/metafield).

***

**Note:** The \<code>\<span class="PreventFireFoxApplyingGapToWBR">metafield\<wbr/>\_text\</span>\</code> filter doesn\&#39;t currently support list metafields other than \<code>\<span class="PreventFireFoxApplyingGapToWBR">list.single\<wbr/>\_line\<wbr/>\_text\<wbr/>\_field\</span>\</code> and \<code>\<span class="PreventFireFoxApplyingGapToWBR">list.metaobject\<wbr/>\_reference\</span>\</code>.

***

### Basic types

The following outlines the output for each metafield type:

| Metafield type | Output |
| - | - |
| `single_line_text_field` | The metafield text. |
| `multi_line_text_field` | The metafield text. |
| `page_reference` | The page title. |
| `product_reference` | The product title. |
| `collection_reference` | The collection title. |
| `variant_reference` | The variant title. |
| `file_reference` | The file URL. |
| `number_integer` | The number. |
| `number_decimal` | The number. |
| `date` | The date. |
| `date-time` | The date and time. |
| `url` | The URL. |
| `json` | The JSON. |
| `boolean` | The boolean value. |
| `color` | The color value. |
| `weight` | The weight value and unit. If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `volume` | The volume value and unit. If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `dimension` | The dimension value and unit. If the value is a decimal with more than two places, then it'll be formatted to have a precision of two with trailing zeros removed. |
| `rating` | The rating value. |
| `list.single_line_text_field` | The metafield values in sentence format. For example, if you had the values `Toronto`, `Ottawa`, and `Vancouver`, then the output would be: `Toronto, Ottawa, and Vancouver` |
| `money` | The money value, formatted using the store's [**HTML with currency** setting](https://help.shopify.com/manual/payments/currency-formatting). |
| `rich_text_field` | The rich text value as simple text. |

##### Code

```liquid
{{ product.metafields.information.dosage | metafield_text }}
```

##### Data

```json
{
  "product": {
    "metafields": {}
  }
}
```

##### Output

```html
Potion dosages
```

### Complex types

The following metafield types produce different output depending on the provided `field` parameter:

* [`list.metaobject_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_text#metafield_text-list.metaobject_reference)
* [`metaobject_reference`](https://shopify.dev/docs/api/liquid/filters/metafield_text#metafield_text-metaobject_reference)

### list.metaobject\_reference

```oobleck
metafield | metafield_text: field: string
```

Outputs the list of metaobjects in sentence format. The required `field` parameter specifies which field should be rendered for each metaobject. The `field` parameter can reference only metafields of type `single_line_text_field`.

##### Code

```liquid
{{ product.metafields.information.ingredients | metafield_text: field: 'name' }}
```

##### Data

```json
{
  "product": {
    "metafields": {}
  }
}
```

##### Output

```html
Spinach, Kale, and Mushrooms
```

### metaobject\_reference

```oobleck
metafield | metafield_text: field: string
```

Outputs the metafield text for the metaobject field specified by the required `field` parameter. The `field` parameter can reference only metafields of type `single_line_text_field`.

##### Code

```liquid
{{ product.metafields.information.primary_ingredient | metafield_tag: field: 'name' }}
```

##### Data

```json
{
  "product": {
    "metafields": {}
  }
}
```

##### Output

```html
<span class="metafield-single_line_text_field">Spinach</span>
```
