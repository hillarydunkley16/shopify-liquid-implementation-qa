---
title: 'Liquid objects: brand'
description: >-
  The [brand
  assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets)
  for the store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/brand'
  md: 'https://shopify.dev/docs/api/liquid/objects/brand.md'
api_name: liquid
---

# brand

The [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets) for the store.

## Properties

* * **colors**

  * The brand's colors.

    To learn about how to access brand colors, refer to [`brand_color`](https://shopify.dev/docs/api/liquid/objects/brand_color).

  * **cover\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The square logo for the brand, resized to 32x32 px.

  * **favicon\_​url**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The square logo for the brand, resized to 32x32 px.

  * **logo**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The default logo for the brand.

  * **metafields**

  * The social links for the brand.

    Social links are stored in [metafields](https://shopify.dev/docs/api/liquid/objects/metafield), and can be accessed using the syntax `shop.brand.metafields.social_links.<platform>.value`.

    | Platforms |
    | - |
    | `facebook` |
    | `pinterest` |
    | `instagram` |
    | `tiktok` |
    | `tumblr` |
    | `snapchat` |
    | `vimeo` |

    ExampleAccess social links

    ##### Code

    ```liquid
    {{ shop.brand.metafields.social_links.twitter.value }}
    {{ shop.brand.metafields.social_links.youtube.value }}
    ```

    ##### Data

    ```json
    {
      "shop": {
        "brand": {
          "metafields": {}
        }
      }
    }
    ```

    ##### Output

    ```html
    https://twitter.com/ShopifyDevs
    https://www.youtube.com/c/shopifydevs
    ```

  * **short\_​description**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A short description of the brand.

  * **slogan**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The slogan for the brand.

  * **square\_​logo**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The square logo for the brand.

##### Example

```json
{
  "colors": {},
  "cover_image": {},
  "favicon_url": {},
  "logo": {},
  "metafields": {},
  "short_description": "Canada's foremost retailer for potions and potion accessories. Try one of our award-winning artisanal potions, or find the supplies to make your own!",
  "slogan": "Save the toil and trouble!",
  "square_logo": {}
}
```
