---
title: "Configurations from backend"
slug: "configurations-from-backend"
excerpt: "Use full queries that can be configured only via backend."
hidden: false
createdAt: "Mon Jun 26 2023 12:25:26 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 12:04:24 GMT+0000 (Coordinated Universal Time)"
---
# How to make the "Total" default report card always appear.

Run the below script

```pgsql
set role <org_name>;

update organisation_config
set settings = settings || '{"hideTotalForProgram": false}' ::jsonb,
    last_modified_date_time = now()
where organisation_id = <org_id>;
```
