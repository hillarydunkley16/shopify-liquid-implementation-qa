---
title: 'Liquid objects: rating'
description: 'Information for a [`rating` type](/apps/metafields/types) metafield.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/rating'
  md: 'https://shopify.dev/docs/api/liquid/objects/rating.md'
api_name: liquid
---

# rating

Information for a [`rating` type](https://shopify.dev/apps/metafields/types) metafield.

***

**Tip:** To learn about metafield types, refer to \<a href="/apps/metafields/types">Metafield types\</a>.

***

## Properties

* * **rating**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The rating value.

  * **scale\_​max**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The maximum value of the rating scale.

  * **scale\_​min**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The minimum value of the rating scale.

##### Example

```json
{
  "rating": "4.5",
  "scale_max": "5.0",
  "scale_min": "0.0"
}
```
