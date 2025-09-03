---
title: "Move Org to Custom Dashboard from MyDashboard"
slug: "move-org-to-custom-dashboard-from-mydashboard"
excerpt: ""
hidden: false
createdAt: "Mon Aug 12 2024 05:03:59 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 03 2024 09:32:59 GMT+0000 (Coordinated Universal Time)"
---
1. As super admin, call `POST /api/defaultDashboard/create?orgId=[organisationId]` (`organisationId` being the id of the organisation for which you want to create the default dashboard - typically your UAT org)
2. This API will only create the default dashboard for non Prod orgs.
3. Assign the newly created dashboard to the required user groups.
4. Test and verify functionality in UAT org
5. Upload bundle from UAT org to live org.
