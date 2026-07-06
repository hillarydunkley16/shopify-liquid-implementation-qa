---
title: 'Liquid filters: standard_event_data'
description: Generates a JSON payload for standard events.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/standard_event_data'
  md: 'https://shopify.dev/docs/api/liquid/filters/standard_event_data.md'
api_name: liquid
---

# standard\_​event\_​data

```oobleck
variable | standard_event_data: event_type, context: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a JSON payload for standard events.

The `standard_event_data` filter generates JSON payloads for standard events. It can be used on [`product`](https://shopify.dev/docs/api/liquid/objects/product), [`collection`](https://shopify.dev/docs/api/liquid/objects/collection), and [`cart`](https://shopify.dev/docs/api/liquid/objects/cart) objects.

The only supported event type is `"view"`.

For products, you can optionally pass a context parameter. Valid values are: `page`, `search`, `collection`, `dialog`, and `recommendation`. If omitted, `context` is `null`. For carts, you can optionally pass a context parameter. Valid values are: `page` and `dialog`. If omitted, `context` is `null`. If the cart hasn't been created yet, then the payload returns `null` for the `cart` field. The context parameter is ignored for collections.

##### Code

```liquid
{{ product | standard_event_data: "view", context: "page" }}
```

##### Output

```html
{"product":{"id":6786188247105,"title":"Health potion","handle":"health-potion","selectedVariant":null},"context":"page","selectedOptions":[]}
```

### Collection view event data

##### Code

```liquid
{{ collection | standard_event_data: "view" }}
```

##### Output

```html
{"collection":{"id":null,"handle":"all","productsCount":19}}
```

### Cart view event data

##### Code

```liquid
{{ cart | standard_event_data: "view", context: "dialog" }}
```

##### Output

```html
{"context":"dialog","cart":null}
```
