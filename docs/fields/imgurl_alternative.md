# Imgurl Alternative

## Overview

**Element Name:** `IMGURL_ALTERNATIVE`<br>
**Type:** string<br>
**Architecture:** Simple<br>
**Required:** No<br>
**Multiple:** Yes (max 10)<br>

Additional product images. Maximum 10 alternative images. Each URL maximum 255 characters.


## General Constraints

- **Optional field** - can be omitted
- **Multiple occurrences** allowed (maximum 10)
- **Maximum length:** 255 characters
- **Pattern:** `https?://[^\s]{1,245}`

## XML Examples

```xml
<IMGURL_ALTERNATIVE>https://example.com/images/product2.jpg</IMGURL_ALTERNATIVE>
```




