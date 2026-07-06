---
title: 'Liquid objects: brand_color'
description: >-
  The colors defined as part of a store's [brand
  assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/brand_color'
  md: 'https://shopify.dev/docs/api/liquid/objects/brand_color.md'
api_name: liquid
---

# brand\_​color

The colors defined as part of a store's [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets).

### Returned by

* [brand.colors](https://shopify.dev/docs/api/liquid/objects/brand#brand-colors)

To access a brand color, specify the following:

* The brand color group: either `primary` or `secondary`
* The color role: Whether the color is a `background` or `foreground` (contrasting) color
* The 0-based index of the color within the group and role

##### Code

```liquid
{{ shop.brand.colors.primary[0].background }}
{{ shop.brand.colors.primary[0].foreground }}
{{ shop.brand.colors.secondary[0].background }}
{{ shop.brand.colors.secondary[1].background }}
{{ shop.brand.colors.secondary[0].foreground }}
```

##### Data

```json
{
  "shop": {
    "brand": {
      "colors": "BrandDrop::BrandColorsDrop"
    }
  }
}
```

##### Output

```html
#0b101f
#DDE2F1
#101B2E
#95A7D5
#A3DFFD
```
