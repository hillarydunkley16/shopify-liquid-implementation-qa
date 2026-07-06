---
title: 'Liquid filters: format_address'
description: >-
  Generates an HTML address display, with each address component ordered
  according to the address's locale.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/format_address'
  md: 'https://shopify.dev/docs/api/liquid/filters/format_address.md'
api_name: liquid
---

# format\_​address

```oobleck
address | format_address
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML address display, with each address component ordered according to the address's locale.

##### Code

```liquid
{{ shop.address | format_address }}
```

##### Data

```json
{
  "shop": {
    "address": {}
  }
}
```

##### Output

```html
<p>Polina&#39;s Potions, LLC<br>150 Elgin Street<br>8th floor<br>Ottawa ON K2P 1L4<br>Canada</p>
```

## Rendered output

##### Code

```liquid
{{ customer.default_address | format_address }}
```

##### Data

```json
{
  "customer": {
    "default_address": {}
  }
}
```

##### Output

```html
<p>Cornelius Potionmaker<br>12 Phoenix Feather Alley<br>1<br>Calgary AB T1X 0L4<br>Canada</p>
```

## Rendered output
