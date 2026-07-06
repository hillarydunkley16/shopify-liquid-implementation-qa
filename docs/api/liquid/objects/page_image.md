---
title: 'Liquid objects: page_image'
description: >-
  An image to be shown in search engine listings and social media previews for
  the current page.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/page_image'
  md: 'https://shopify.dev/docs/api/liquid/objects/page_image.md'
api_name: liquid
---

# page\_​image

An image to be shown in search engine listings and social media previews for the current page.

The resource's featured image for product and collection pages, and blog posts, is used. For all other pages, or pages where there's no featured image, the [social sharing image](https://help.shopify.com/manual/online-store/images/showing-social-media-thumbnail-images?#setting-the-social-sharing-image-in-your-admin) is used.

### Open Graph fallback tags

The `page_image` object can be used for creating [Open Graph](https://ogp.me/) `og:image` meta tags.

If a theme doesn't include `og:image` tags for a page, then Shopify automatically generates the following tags using the `page_image` object:

* `og:image`
* `og:image:secure_url`
* `og:image:width`
* `og:image:height`

### Directly accessible in

* Global
