# Imgurl

## Overview

**Element Name:** `IMGURL`<br>
**Type:** string<br>
**Architecture:** Simple<br>
**Required:** Yes<br>

Primary product image URL. Maximum 255 characters. Must start with http:// or https://.


## General Constraints

- **Required field** - must be present in the XML
- **Maximum length:** 255 characters
- **Pattern:** `https?://[^\s]{1,245}`

## XML Examples

```xml
<IMGURL>https://example.com/images/product.jpg</IMGURL>
```




