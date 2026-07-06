---
title: 'Liquid objects: article'
description: >-
  An article, or [blog
  post](https://help.shopify.com/manual/online-store/blogs/writing-blogs), in a
  blog.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/article'
  md: 'https://shopify.dev/docs/api/liquid/objects/article.md'
api_name: liquid
---

# article

An article, or [blog post](https://help.shopify.com/manual/online-store/blogs/writing-blogs), in a blog.

## Properties

* * **author**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The full name of the author of the article.

  * **comment\_​post\_​url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL where POST requests are sent when creating new comments.

  * **comments**

    array of [comment](https://shopify.dev/docs/api/liquid/objects/comment)

  * The published comments for the article.

    Returns an empty array if comments are disabled.

    **Tip:** Use the \<a href="/docs/api/liquid/tags/paginate">paginate\</a> tag to choose how many comments to show at once, up to a limit of 50.

  * **comments\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of published comments for the article.

  * **comments\_​enabled?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if comments are enabled. Returns `false` if not.

  * **content**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The content of the article.

  * **created\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the article was created.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **excerpt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The excerpt of the article.

  * **excerpt\_​or\_​content**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Returns the article [excerpt](https://shopify.dev/docs/api/liquid/objects/article#article-excerpt) if it exists. Returns the article [content](https://shopify.dev/docs/api/liquid/objects/article#article-content) if no excerpt exists.

  * **handle**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the article.

  * **id**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ID of the article.

  * **image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The featured image for the article.

  * **metafields**

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the article.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **moderated?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the blog that the article belongs to is set to [moderate comments](https://help.shopify.com/manual/online-store/blogs/managing-comments). Returns `false` if not.

  * **published\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the article was published.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **tags**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The tags applied to the article.

    ExampleShow the total tag count

    When looping through `article.tags`, you can print how many times a tag is used with `tag.total_count`. This number shows visitors how many blog posts have been tagged with a particular tag.

    ##### Code

    ```liquid
    {% for tag in article.tags -%}
      {{ tag }} ({{ tag.total_count }})
    {%- endfor %}
    ```

    ##### Data

    ```json
    {
      "article": {
        "tags": [
          "clear potions",
          "potion troubleshooting",
          "tips"
        ]
      }
    }
    ```

    ##### Output

    ```html
    clear potions (1)potion troubleshooting (2)tips (2)
    ```

  * **template\_​suffix**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the [custom template](https://shopify.dev/themes/architecture/templates#alternate-templates) assigned to the article.

    The name doesn't include the `article.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the article, then `nil` is returned.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the article.

  * **updated\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the article was updated.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the article.

  * **user**

    [user](https://shopify.dev/docs/api/liquid/objects/user)

  * The user associated with the author of the article.

##### Example

```json
{
  "author": "Polina Waters",
  "comment_post_url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion/comments",
  "comments": [],
  "comments_count": 1,
  "comments_enabled?": true,
  "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>",
  "created_at": "2022-04-14 16:56:02 -0400",
  "excerpt": "And where to buy <strong>more</strong>!",
  "excerpt_or_content": "And where to buy <strong>more</strong>!",
  "handle": "potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion",
  "id": 556510085185,
  "image": {},
  "metafields": {},
  "moderated?": true,
  "published_at": "2022-04-14 16:56:02 -0400",
  "tags": [],
  "template_suffix": "",
  "title": "How to tell if you're out of invisibility potion",
  "updated_at": "2022-06-04 19:27:33 -0400",
  "url": {},
  "user": {}
}
```

## Templates using article

[Theme architecture](https://shopify.dev/themes/architecture/templates/article)

[article template](https://shopify.dev/themes/architecture/templates/article)
