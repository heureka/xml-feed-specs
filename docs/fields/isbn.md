# Isbn

## Overview

**Element Name:** `ISBN`<br>
**Type:** string<br>
**Architecture:** Simple<br>
**Required:** No<br>

International Standard Book Number. Accepts ISBN-10 (10 digits with possible X) or
ISBN-13 (13 digits) format.


## General Constraints

- **Optional field** - can be omitted
- **Pattern:** `\d{9}[\dX]|\d{13}`

## XML Examples

```xml
<ISBN>9781234567890</ISBN>
```

```xml
<ISBN>123456789X</ISBN>
```




