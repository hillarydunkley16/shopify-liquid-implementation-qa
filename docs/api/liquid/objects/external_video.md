---
title: 'Liquid objects: external_video'
description: Information about an external video from YouTube or Vimeo.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/external_video'
  md: 'https://shopify.dev/docs/api/liquid/objects/external_video.md'
api_name: liquid
---

# external\_​video

Information about an external video from YouTube or Vimeo.

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/external\_video\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">external\<wbr/>\_video\<wbr/>\_tag\</span>\</code> filter\</a> to output the video in an HTML \<code>\&lt;iframe\&gt;\</code> tag. Use the \<a href="/docs/api/liquid/filters/external\_video\_url">\<code>\<span class="PreventFireFoxApplyingGapToWBR">external\<wbr/>\_video\<wbr/>\_url\</span>\</code> filter\</a> to specify parameters for the external video player.

***

## Properties

* * **alt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The alt text of the external video.

  * **aspect\_​ratio**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The aspect ratio of the video as a decimal.

  * **external\_​id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the video from its external source.

  * **host**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The service that hosts the video.

    | Possible values |
    | - |
    | youtube |
    | vimeo |

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the external video.

  * **media\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The media type of the external video. Always returns `external_video`.

    ExampleFilter for media of a specific type

    You can use the `media_type` property with the [`where` filter](https://shopify.dev/docs/api/liquid/filters/where) to filter the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) for all media of a desired type.

    ##### Code

    ```liquid
    {% assign external_videos = product.media | where: 'media_type', 'external_video' %}

    {% for external_video in external_videos %}
      {{- external_video | external_video_tag }}
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
    <iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
    ```

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The position of the external video in the [`product.media`](https://shopify.dev/docs/api/liquid/objects/product#product-media) array.

  * **preview\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * A preview image of the media.

    **Note:** Preview images don\&#39;t have an ID attribute.

##### Example

```json
{
  "alt": "Potion beats",
  "aspect_ratio": "1.77",
  "external_id": "vj01PAffOac",
  "host": "youtube",
  "id": 22015756402753,
  "media_type": "external_video",
  "position": 1,
  "preview_image": {}
}
```
