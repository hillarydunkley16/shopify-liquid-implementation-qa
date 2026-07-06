---
title: 'Liquid filters: default'
description: |-
  Sets a default value for any variable whose value is one of the following:

  - [`empty`](/docs/api/liquid/basics#empty)
  - [`false`](/docs/api/liquid/basics#truthy-and-falsy)
  - [`nil`](/docs/api/liquid/basics#nil)
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/default'
  md: 'https://shopify.dev/docs/api/liquid/filters/default.md'
api_name: liquid
---

# default

```oobleck
variable | default: variable
```

Sets a default value for any variable whose value is one of the following:

* [`empty`](https://shopify.dev/docs/api/liquid/basics#empty)
* [`false`](https://shopify.dev/docs/api/liquid/basics#truthy-and-falsy)
* [`nil`](https://shopify.dev/docs/api/liquid/basics#nil)

##### Code

```liquid
{{ product.selected_variant.url | default: product.url }}
```

##### Data

```json
{
  "product": {
    "selected_variant": null,
    "url": "/products/health-potion"
  }
}
```

##### Output

```html
/products/health-potion
```

### allow\_false

```oobleck
variable | default: variable, allow_false: boolean
```

By default, the `default` filter's value will be used in place of `false` values. You can use the `allow_false` parameter to allow variables to return `false` instead of the default value.

##### Code

```liquid
{%- assign display_price = false -%}

{{ display_price | default: true, allow_false: true }}
```

##### Output

```html
false
```
