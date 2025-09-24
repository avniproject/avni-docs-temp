title: Key system and data flows concepts
excerpt: ''
    - type: basic
      slug: subject-types
      title: Subject types
---
Now that we understand the [three key components of fieldwork](doc:avnis-domain-model-of-field-based-work) i.e. Organisation, Services and Service Encounter - let's try to understand how Avni works and achieves various functions.

# How implementation-specific mobile application is created?

Avni is a generic platform that allows any organisation doing field-based work to use it for their specific purpose. The diagram below explains the steps involved in creating an organisation-specific application from a generic platform.

<Image title="Screenshot 2019-11-15 at 5.33.27 PM.png" alt={1440} align="center" src="https://files.readme.io/8932d2e-Screenshot_2019-11-15_at_5.33.27_PM.png">
  Data flow of organisation, services and service encounter definition.
</Image>

# How does avni field user gets all the subject data on his/her device?

As we saw earlier, given the organisation work physically consists of catchments and locations. The subjects are living or located at these locations.

<Image title="Screenshot 2019-11-15 at 5.35.21 PM.png" alt={1726} align="center" src="https://files.readme.io/0f59c92-Screenshot_2019-11-15_at_5.35.21_PM.png">
  During organisation setup the implementer or customer IT person sets up catchments with locations and assigns them to the provider (field user)
</Image>

The diagram below shows how the subjects and the subjects's complete data, which is required by the field user (and only those subjects) are made available.

<Image title="Screenshot 2019-11-15 at 6.07.48 PM.png" alt={1580} align="center" src="https://files.readme.io/8e8be68-Screenshot_2019-11-15_at_6.07.48_PM.png">
  Subjects belonging to the catchment of the user downloaded to their device
</Image>

# How Avni works in an offline mode

Avni maintains a database on the mobile device. All the data downloaded from the server is kept on this device. When the user is using the application, all the data is served from this device to the user and all the new data created by the user is stored in the mobile database. When the synchronisation happens this new data is sent to the server.

# How does the generic avni mobile application behave as if it has been developed for a specific organisation?

The diagram below explains how avni app customises itself based on the complete organisational setup (explained earlier).

<Image title="Screenshot 2019-11-15 at 5.52.34 PM.png" alt={1792} align="center" src="https://files.readme.io/8033619-Screenshot_2019-11-15_at_5.52.34_PM.png">
  Avni app customises itself based on the organisation data setup present in the mobile database on the device
</Image>
