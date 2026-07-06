---
title: 'Liquid objects: video'
description: >-
  Information about a video uploaded as [product
  media](/docs/api/liquid/objects/product-media) or a [`file_reference`
  metafield](/apps/metafields/types).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/video'
  md: 'https://shopify.dev/docs/api/liquid/objects/video.md'
api_name: liquid
---

# video

Information about a video uploaded as [product media](https://shopify.dev/docs/api/liquid/objects/product-media) or a [`file_reference` metafield](https://shopify.dev/apps/metafields/types).

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/video\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">video\<wbr/>\_tag\</span>\</code> filter\</a> to output the video in an HTML \<code>\&lt;video\&gt;\</code> tag.

***

## Properties

* * **alt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The alt text of the video.

  * **aspect\_​ratio**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The aspect ratio of the video as a decimal.

  * **duration**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The duration of the video in milliseconds.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the video.

  * **media\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The media type of the model. Always returns `video`.

    ExampleFilter for media of a specific type

    You can use the `media_type` property with the [`where` filter](https://shopify.dev/docs/api/liquid/filters/where) to filter the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) for all media of a desired type.

    ##### Code

    ```liquid
    {% assign videos = product.media | where: 'media_type', 'video' %}

    {% for video in videos %}
      {{- video | video_tag }}
    {% endfor %}
    ```

    ##### Data

    ```json
    {
      "product": {
        "media": [
          {
            "media_type": "external_video"
          },
          {
            "media_type": "video"
          }
        ]
      }
    }
    ```

    ##### Output

    ```html
    <video playsinline="playsinline" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
    ```

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The position of the video in the [`product.media`](https://shopify.dev/docs/api/liquid/objects/product#product-media) array.

  * **preview\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * A preview image for the video.

  * **sources**

    array of [video\_source](https://shopify.dev/docs/api/liquid/objects/video_source)

  * The source files for the video.

##### Example

```json
{
  "alt": "Potion beats",
  "aspect_ratio": 1.779,
  "duration": 34801,
  "id": 22070396551233,
  "media_type": "video",
  "position": 2,
  "preview_image": {},
  "sources": []
}
```
