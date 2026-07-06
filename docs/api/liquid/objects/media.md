---
title: 'Liquid objects: media'
description: |-
  An abstract media object that can represent the following object types:

  - [`image`](/docs/api/liquid/objects/image)
  - [`model`](/docs/api/liquid/objects/model)
  - [`video`](/docs/api/liquid/objects/video)
  - [`external_video`](/docs/api/liquid/objects/external_video)
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/media'
  md: 'https://shopify.dev/docs/api/liquid/objects/media.md'
api_name: liquid
---

# media

An abstract media object that can represent the following object types:

* [`image`](https://shopify.dev/docs/api/liquid/objects/image)
* [`model`](https://shopify.dev/docs/api/liquid/objects/model)
* [`video`](https://shopify.dev/docs/api/liquid/objects/video)
* [`external_video`](https://shopify.dev/docs/api/liquid/objects/external_video)

The `media` object can be returned by the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) or a [`file_reference` metafield](https://shopify.dev/apps/metafields/types).

You can use [media filters](https://shopify.dev/docs/api/liquid/filters/media-filters) to generate URLs and media displays. To learn about how to use media in your theme, refer to [Support product media](https://shopify.dev/themes/product-merchandising/media/support-media).

***

**Note:** Each media type has unique properties in addition to the general \<code>media\</code> properties. To learn about these additional properties, refer to the reference for each type.

***

## Properties

* * **alt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The alt text of the media.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the media.

  * **media\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The media type.

    | Possible values |
    | - |
    | image |
    | model |
    | video |
    | external\_video |

    ExampleFilter for media of a specific type

    You can use the `media_type` property with the [`where` filter](https://shopify.dev/docs/api/liquid/filters/where) to filter the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) for all media of a desired type.

    ##### Code

    ```liquid
    {% assign images = product.media | where: 'media_type', 'image' %}

    {% for image in images %}
      {{- image | image_url: width: 300 | image_tag }}
    {% endfor %}
    ```

    ##### Data

    ```json
    {
      "product": {
        "media": [
          "products/oil-dripping-into-jar.jpg"
        ]
      }
    }
    ```

    ##### Output

    ```html
    <img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300" alt="Viper venom" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/products/oil-dripping-into-jar.jpg?v=1650399519&amp;width=300 300w" width="300" height="200">
    ```

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The position of the media in the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media).

    If the source is a [`file_reference` metafield](https://shopify.dev/apps/metafields/types), then `nil` is returned.

  * **preview\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * A preview image of the media.

    **Note:** Preview images don\&#39;t have an ID attribute.

##### Example

```json
{
  "alt": "Dandelion milk",
  "id": 21772527435841,
  "media_type": "image",
  "position": 1,
  "preview_image": {}
}
```
