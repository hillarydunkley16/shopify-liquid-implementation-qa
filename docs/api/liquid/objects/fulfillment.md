---
title: 'Liquid objects: fulfillment'
description: >-
  An order [fulfillment](https://help.shopify.com/manual/orders/fulfillment),
  which includes information like the line items

  being fulfilled and shipment tracking.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/fulfillment'
  md: 'https://shopify.dev/docs/api/liquid/objects/fulfillment.md'
api_name: liquid
---

# fulfillment

An order [fulfillment](https://help.shopify.com/manual/orders/fulfillment), which includes information like the line items being fulfilled and shipment tracking.

## Properties

* * **created\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the fulfillment was created.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **fulfillment\_​line\_​items**

    array of [line\_item](https://shopify.dev/docs/api/liquid/objects/line_item)

  * The line items in the fulfillment.

  * **item\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of items in the fulfillment.

  * **tracking\_​company**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the fulfillment service.

  * **tracking\_​number**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The fulfillment's tracking number.

    If there's no tracking number, then `nil` is returned.

  * **tracking\_​numbers**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * An array of the fulfillment's tracking numbers.

  * **tracking\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL for the fulfillment's tracking number.

    If there's no tracking number, then `nil` is returned.

##### Example

```json
{
  "created_at": "2022-06-15 17:08:30 -0400",
  "fulfillment_line_items": [
    {
      "quantity": 2,
      "line_item": "LineItemDrop"
    },
    {
      "quantity": 1,
      "line_item": "LineItemDrop"
    }
  ],
  "item_count": 3,
  "tracking_company": "Canada Post",
  "tracking_number": "01189998819991197253",
  "tracking_numbers": [
    "01189998819991197253"
  ],
  "tracking_url": "https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=01189998819991197253"
}
```
