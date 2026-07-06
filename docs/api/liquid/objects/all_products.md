---
title: 'Liquid objects: all_products'
description: All of the products on a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/all_products'
  md: 'https://shopify.dev/docs/api/liquid/objects/all_products.md'
api_name: liquid
---

# all\_​products

All of the products on a store.

***

**Note:** The \<code>\<span class="PreventFireFoxApplyingGapToWBR">all\<wbr/>\_products\</span>\</code> object has a limit of 20 unique handles per page. If you want more than 20 products, then consider using a collection instead.

***

### Directly accessible in

* Global

You can use `all_products` to access a product by its [handle](https://shopify.dev/docs/api/liquid/basics#handles). This returns the [`product`](https://shopify.dev/docs/api/liquid/objects/product) object for the specified product. If the product isn't found, then `empty` is returned.

##### Code

```liquid
{{ all_products['love-potion'].title }}
```

##### Data

```json
{
  "all_products": {
    "love-potion": {
      "title": "Love Potion"
    }
  }
}
```

##### Output

```html
Love Potion
```
