---
title: 'Liquid objects: recommendations'
description: >-
  Product recommendations for a specific product based on sales data, product
  descriptions, and collection relationships.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/recommendations'
  md: 'https://shopify.dev/docs/api/liquid/objects/recommendations.md'
api_name: liquid
---

# recommendations

Product recommendations for a specific product based on sales data, product descriptions, and collection relationships.

Product recommendations become more accurate over time as new orders and product data become available. To learn more about how product recommendations are generated, refer to [Product recommendations](https://shopify.dev/themes/product-merchandising/recommendations).

***

**Note:** The \<code>recommendations\</code> object returns products only when rendered in a section using the \<a href="/api/ajax/reference/product-recommendations">Product Recommendations API\</a> and the \<a href="/api/section-rendering">Section Rendering API\</a>. To learn about how to include product recommendations in your theme, refer to \<a href="/themes/product-merchandising/recommendations/show-product-recommendations">Show product recommendations\</a>.

***

## Properties

* * **intent**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The recommendation intent.

    If `performed?` is `false`, then `nil` is returned.

  * **performed?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` when being referenced inside a section that's been rendered using the Product Recommendations API and the Section Rendering API. Returns `false` if not.

  * **products**

    array of [product](https://shopify.dev/docs/api/liquid/objects/product)

  * The recommended products.

    If `performed?` is `false`, then an [EmptyDrop](https://shopify.dev/docs/api/liquid/basics#emptydrop) is returned.

  * **products\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of recommended products.

    If `performed?` is `false`, then 0 is returned.

##### Example

```json
{
  "products": [],
  "products_count": 4,
  "performed?": true
}
```
