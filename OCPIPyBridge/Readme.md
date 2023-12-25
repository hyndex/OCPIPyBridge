### Complete Documentation for Each Model in OCPIPyBridge

OCPIPyBridge, a Python library for the Open Charge Point Interface (OCPI) protocol, includes several models for representing different entities in electric vehicle (EV) charging infrastructure and services. Below is a detailed documentation for each model:

#### 1. `Dimension` Model
- **Purpose**: Represents physical dimensions.
- **Fields**:
  - `type`: String indicating the dimension type.
  - `volume`: Float representing the volume.

#### 2. `ChargingPeriod` Model
- **Purpose**: Represents a period during which charging takes place.
- **Fields**:
  - `startDateTime`: String indicating the start date and time.
  - `dimensions`: List of `Dimension` objects.

#### 3. `Token` Model
- **Purpose**: Represents a token for authentication and identification.
- **Fields**:
  - `uid`: Unique identifier string.
  - `type`, `authId`, `visualNumber`, `issuer`: Various strings for identification.
  - `valid`: Boolean indicating if the token is valid.
  - `whitelist`, `language`, `lastUpdated`: Additional descriptive strings.

#### 4. `Connector` Model
- **Purpose**: Represents a charging connector.
- **Fields**:
  - Includes various strings and floats for connector details like `id`, `standard`, `format`, and technical specifications.
  - `pricing`: Optional dictionary for pricing information.
  - Lists for `authentication_modes`, `identification_restrictions`, `payment_methods`.
  - `supported_energy_mix`: Dictionary for energy mix information.

#### 5. `Logo` Model
- **Purpose**: Represents a logo.
- **Fields**:
  - `url`: `HttpUrl` for the logo image.
  - `category`, `type`: Strings for categorization.
  - `width`, `height`: Integers for dimensions.

#### 6. `BusinessDetails` Model
- **Purpose**: Represents business details.
- **Fields**:
  - `name`: String for business name.
  - `website`: Optional `HttpUrl`.
  - `logo`: Optional `Logo` object.

#### 7. `Credentials` Model
- **Purpose**: Represents credentials.
- **Fields**:
  - `token`, `url`: Strings for token and URL.
  - `business_details`: `BusinessDetails` object.
  - `party_id`, `country_code`, `role`: Additional strings.

#### 8. `PriceComponent` Model
- **Purpose**: Represents a component of pricing.
- **Fields**:
  - `type`: String for the type of pricing component.
  - `price`, `stepSize`: Floats for pricing details.

#### 9. `TariffElement` Model
- **Purpose**: Represents an element of a tariff.
- **Fields**:
  - `priceComponents`: List of `PriceComponent` objects.

#### 10. `Tariff` Model
- **Purpose**: Represents a tariff.
- **Fields**:
  - `id`, `currency`: Strings for identification and currency.
  - `elements`: List of `TariffElement` objects.

#### 11. `Meter` Model
- **Purpose**: Represents a meter.
- **Fields**:
  - `id`: String for the meter ID.
  - `value`: Float for the meter value.
  - `timestamp`: String for the timestamp.

#### 12. `Reservation` Model
- **Purpose**: Represents a reservation.
- **Fields**:
  - `id`, `expiryDate`, `idTag`, `reservationId`: Various strings and floats for reservation details.

#### 13. `Feedback` Model
- **Purpose**: Represents feedback.
- **Fields**:
  - `id`, `rating`, `comment`, `userId`: Strings and float for feedback details.

#### 14. `Coordinates` Model
- **Purpose**: Represents geographical coordinates.
- **Fields**:
  - `latitude`, `longitude`: Floats for coordinates.

#### 15. `OpeningTimes` Model
- **Purpose**: Represents opening times.
- **Fields**:
  - Lists for `regularHours`, `exceptionalOpenings`, `exceptionalClosings`.

#### 16. `RegularHours` Model
- **Purpose**: Represents regular opening hours.
- **Fields**:
  - `weekday`: Integer for the day of the week.
  - `periodBegin`, `periodEnd`: Strings for time periods.

#### 17. `ExceptionalPeriod` Model
- **Purpose**: Represents an exceptional period.
- **Fields**:
  - `periodBegin`, `periodEnd`: Strings for time periods.

#### 18. `Facility` Model
- **Purpose**: Represents a facility.
- **Fields**:
  - `type`: String for the facility type.

#### 19. `EnergyMix` Model
- **Purpose**: Represents an energy mix.
- **Fields**:
  - `isGreenEnergy`: Boolean for green energy.
  - `energySources`, `environImpact`: Lists of dictionaries for energy sources and environmental impact.
  - `supplierName`, `energyProductName`: Strings for supplier and product names.

#### 20. `Image` Model
- **Purpose**: Represents an image.
- **Fields**:
  - `url`, `thumbnail`: `HttpUrl` objects.
  - `category`, `type`: Strings for categorization.
  - `width`, `height`: Integers for dimensions.

#### 21. `Location` Model
- **Purpose**: Represents a location.
- **Fields**:
  - Extensive details including strings, lists, and objects for location, facilities, and related information.

#### 22. `EVSE` Model
- **Purpose**: Represents an Electric Vehicle Supply Equipment (EVSE).
- **Fields**:
  - Extensive fields for EVSE details including lists, strings, and `Coordinates`.

#### 23. `CDR` Model
- **Purpose**: Represents a Charge Detail Record (CDR).
- **Fields**:
  - Detailed fields for charging record information including strings, floats, and optional fields.

#### 24. `Command` and Sub-Commands
- **Purpose**: Represents various commands.
- **Fields**:
  - `Command` includes `type` and `data` fields.
  - Sub-commands like `CancelReservationCommand`, `ReserveNowCommand`, `StartSessionCommand`, `StopSessionCommand`, `UnlockConnectorCommand` with specific fields and validators.

#### 25. `Transaction` Model
- **Purpose**: Represents a transaction.
- **Fields**:
  - `id`, `meterStart`, `timestamp`, `idTag`: Strings and floats for transaction details.

#### 26. `User` Model
- **Purpose**: Represents a user.
- **Fields**:
  - `id`, `name`, `email`: Strings for user details.
  - `verified`: Boolean for verification status.

### Usage Examples and Integration
The documentation includes examples of how to use these models, specifically with Flask and FastAPI frameworks, demonstrating the practical application in EV charging infrastructure services.

### Contributing and Licensing
Guidelines for contributing to the library are provided, along with author details and licensing information, encouraging community involvement and use under the MIT License.