---
title: 'Liquid objects: image'
description: 'An image, such as a product or collection image.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/image'
  md: 'https://shopify.dev/docs/api/liquid/objects/image.md'
api_name: liquid
---

# image

An image, such as a product or collection image.

To learn about the image formats that Shopify supports, visit the [Shopify Help Center](https://help.shopify.com/manual/online-store/images/theme-images#image-formats).

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/image\_url">\<code>\<span class="PreventFireFoxApplyingGapToWBR">image\<wbr/>\_url\</span>\</code>\</a> and \<a href="/docs/api/liquid/filters/image\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">image\<wbr/>\_tag\</span>\</code>\</a> filters to display images on the storefront.

***

## Properties

* * **alt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The alt text of the image.

  * **aspect\_​ratio**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The aspect ratio of the image as a decimal.

  * **attached\_​to\_​variant?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the image is associated with a variant. Returns `false` if not.

    The `attached_to_variant?` property is only available for images accessed through the following sources:

    * [`product.featured_image`](https://shopify.dev/docs/api/liquid/objects/product#product-featured_image)
    * [`product.images`](https://shopify.dev/docs/api/liquid/objects/product#product-images)

    If you reference this property on an image from another source, then `nil` is returned.

  * **height**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The height of the image in pixels.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the image.

    If you reference the `id` property for preview images of [`generic_file`](https://shopify.dev/docs/api/liquid/objects/generic_file) or [`media`](https://shopify.dev/docs/api/liquid/objects/media) objects, then `nil` is returned.

  * **media\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The media type of the image. Always returns `image`.

    The `media_type` property is only available for images accessed through the following sources:

    * [`product.media`](https://shopify.dev/docs/api/liquid/objects/product#product-media)
    * [`file_reference` type metafields](https://shopify.dev/apps/metafields/types#supported-types)

    If you reference this property on an image from another source, then `nil` is returned.

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

  * The position of the image in the [`product.images`](https://shopify.dev/docs/api/liquid/objects/product#product-images) or [`product.media`](https://shopify.dev/docs/api/liquid/objects/product#product-media) array.

    The `position` property is only available for images that are associated with a product. If you reference this property on an image from another source, then `nil` is returned.

  * **presentation**

    [image\_presentation](https://shopify.dev/docs/api/liquid/objects/image_presentation)

  * The presentation settings for the image.

  * **preview\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * A preview image for the image.

    The `preview_image` property is only available for images accessed through the following sources:

    * [`product.featured_media`](https://shopify.dev/docs/api/liquid/objects/product#product-featured_media)
    * [`product.media`](https://shopify.dev/docs/api/liquid/objects/product#product-media)
    * [`file_reference` type metafields](https://shopify.dev/apps/metafields/types#supported-types)

    If you reference this property on an image from another source, then `nil` is returned.

  * **product\_​id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the product that the image is associated with.

    The `product_id` property is only available for images associated with a product. If you reference this property on an image from another source, then `nil` is returned.

  * **src**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the image.

  * **variants**

    array of [variant](https://shopify.dev/docs/api/liquid/objects/variant)

  * The product variants that the image is associated with.

    The `variants` property is only available for images accessed through the following sources:

    * [`product.featured_image`](https://shopify.dev/docs/api/liquid/objects#product-featured_image)
    * [`product.images`](https://shopify.dev/docs/api/liquid/objects/product#product-images)

    If you reference this property on an image from another source, then `nil` is returned.

  * **width**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The width of the image in pixels.

##### Example

```json
{
  "alt": "Charcoal",
  "aspect_ratio": 1.5001681802892701,
  "attached_to_variant?": false,
  "height": 2973,
  "id": 29355706875969,
  "position": 1,
  "product_id": 6790277595201,
  "src": {},
  "variants": [],
  "width": 4460
}
```

### Referencing the `image` object directly

When an `image` object is referenced directly, the image's relative URL path is returned.

##### Code

```liquid
{{ product.featured_image }}
```

##### Data

```json
{
  "product": {
    "featured_image": "products/mushrooms-on-a-table.jpg"
  }
}
```

##### Output

```html
products/mushrooms-on-a-table.jpg
```
