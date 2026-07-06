---
title: 'Liquid objects: measurement'
description: |-
  A measurement from one of the following metafield types:

  - `dimension`
  - `volume`
  - `weight`
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/measurement'
  md: 'https://shopify.dev/docs/api/liquid/objects/measurement.md'
api_name: liquid
---

# measurement

A measurement from one of the following metafield types:

* `dimension`
* `volume`
* `weight`

***

**Tip:** To learn about metafield types, refer to \<a href="/apps/metafields/types">Metafield types\</a>.

***

## Properties

* * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The measurement type.

    | Possible values |
    | - |
    | dimension |
    | volume |
    | weight |

  * **unit**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The measurement unit.

  * **value**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The measurement value.

##### Example

```json
{
  "type": "volume",
  "unit": "mL",
  "value": "500.0"
}
```
