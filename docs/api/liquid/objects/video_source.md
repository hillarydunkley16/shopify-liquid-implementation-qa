---
title: 'Liquid objects: video_source'
description: Information about the source files for a video.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/video_source'
  md: 'https://shopify.dev/docs/api/liquid/objects/video_source.md'
api_name: liquid
---

# video\_​source

Information about the source files for a video.

## Properties

* * **format**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The format of the video source file.

    **Note:** When mp4 videos are uploaded, Shopify generates an m3u8 file as an additional video source. An m3u8 file enables video players to leverage HTTP live streaming (HLS), resulting in an optimized video experience based on the user\&#39;s internet connection.

    | Possible values |
    | - |
    | mov |
    | mp4 |
    | m3u8 |

  * **height**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The height of the video source file.

  * **mime\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the video source file.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) of the video source file.

  * **width**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The width of the video source file.

##### Example

```json
{
  "format": "mp4",
  "height": 1080,
  "mime_type": "video/mp4",
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0",
  "width": 1920
}
```
