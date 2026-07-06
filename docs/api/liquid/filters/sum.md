---
title: 'Liquid filters: sum'
description: Returns the sum of all elements in an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/sum'
  md: 'https://shopify.dev/docs/api/liquid/filters/sum.md'
api_name: liquid
---

# sum

```oobleck
array | sum
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Returns the sum of all elements in an array.

##### Code

```liquid
{% assign fibonacci = '0, 1, 1, 2, 3, 5' | split: ', ' %}

{{ fibonacci | sum }}
```

##### Output

```html
12
```

### Sum object property values

```oobleck
array | sum: string
```

For an array of Liquid objects, you can specify a property to sum.

##### Code

```liquid
Total quantity of all items in cart:
{{ cart.items | sum: 'quantity' }}

Subtotal price for all items in cart:
{{ cart.items | sum: 'final_line_price' | money }}
```

##### Data

```json
{
  "cart": {
    "items": [
      {
        "final_line_price": "22.49",
        "quantity": 1
      },
      {
        "final_line_price": "400.00",
        "quantity": 1
      }
    ]
  }
}
```

##### Output

```html
Total quantity of all items in cart:
2

Subtotal price for all items in cart:
$422.49
```
