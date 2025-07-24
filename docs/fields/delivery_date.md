# Delivery Date

## Overview

**Element Name:** `DELIVERY_DATE`<br>
**Type:** string<br>
**Architecture:** Simple<br>
**Required:** Yes<br>

Expected delivery time. Can be number of days (1-999) or specific date in YYYY-MM-DD format.


## General Constraints

- **Required field** - must be present in the XML
- **Pattern:** `\d{1,3}|\d{4}-\d{2}-\d{2}`

## XML Examples

```xml
<DELIVERY_DATE>5</DELIVERY_DATE>
```

```xml
<DELIVERY_DATE>2024-12-25</DELIVERY_DATE>
```




