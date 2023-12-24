from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Union

class Dimension(BaseModel):
    type: str
    volume: float

class ChargingPeriod(BaseModel):
    startDateTime: str
    dimensions: List[Dimension]

class Token(BaseModel):
    uid: str
    type: str
    authId: str
    visualNumber: str
    issuer: str
    valid: bool
    whitelist: str
    language: str
    lastUpdated: str

class Connector(BaseModel):
    id: str
    standard: str
    format: str
    powerType: str
    maxVoltage: float
    maxAmperage: float
    maxElectricPower: float
    voltage: float
    amperage: float
    lastUpdated: str
    terms_and_conditions: str
    phase_to_phase_voltage: float
    phase: int
    pricing: Optional[Dict] = {}
    parking_spot: str
    accessibility: str
    authentication_modes: List[str] = []
    identification_restrictions: List[str] = []
    payment_methods: List[str] = []
    supported_energy_mix: Dict = {}

class Logo(BaseModel):
    url: HttpUrl
    category: str
    type: str
    width: int
    height: int

class BusinessDetails(BaseModel):
    name: str
    website: Optional[HttpUrl]
    logo: Optional[Logo]

class Credentials(BaseModel):
    token: str
    url: HttpUrl
    business_details: BusinessDetails
    party_id: str
    country_code: str
    role: str

class PriceComponent(BaseModel):
    type: str
    price: float
    stepSize: float

class TariffElement(BaseModel):
    priceComponents: List[PriceComponent]

class Tariff(BaseModel):
    id: str
    currency: str
    elements: List[TariffElement]

class Meter(BaseModel):
    id: str
    value: float
    timestamp: str

class Reservation(BaseModel):
    id: str
    expiryDate: str
    idTag: str
    reservationId: float

class Feedback(BaseModel):
    id: str
    rating: float
    comment: str
    userId: str

class Coordinates(BaseModel):
    latitude: float
    longitude: float

class OpeningTimes(BaseModel):
    regularHours: List[Dict]
    exceptionalOpenings: List[Dict]
    exceptionalClosings: List[Dict]

class RegularHours(BaseModel):
    weekday: int
    periodBegin: str
    periodEnd: str

class ExceptionalPeriod(BaseModel):
    periodBegin: str
    periodEnd: str

class Facility(BaseModel):
    type: str

class EnergyMix(BaseModel):
    isGreenEnergy: bool
    energySources: List[Dict]
    environImpact: List[Dict]
    supplierName: str
    energyProductName: str

class Image(BaseModel):
    url: HttpUrl
    thumbnail: HttpUrl
    category: str
    type: str
    width: int
    height: int

class Location(BaseModel):
    id: str
    type: str
    name: str
    address: str
    city: str
    postalCode: str
    country: str
    coordinates: Coordinates
    relatedLocations: List[Location] = []
    parkingType: str
    evse: List[Connector] = []
    facilities: List[Facility] = []
    time_zone: str
    opening_times: OpeningTimes
    charging_when_closed: bool
    images: List[Image] = []
    energy_mix: EnergyMix
    business_details: BusinessDetails
    operator: Optional[Dict] = {}
    suboperator: Optional[Dict] = {}
    owner: Optional[Dict] = {}
    clearinghouse: Optional[Dict] = {}
    last_updated: str

class EVSE(BaseModel):
    uid: str
    evse_id: str
    status: str
    capabilities: List[str] = []
    connectors: List[Connector] = []
    floor_level: str
    coordinates: Coordinates
    physical_reference: str
    directions: List[Dict] = []
    parking_restrictions: List[str] = []
    images: List[Image] = []
    charging_when_closed: bool
    last_updated: str
    energy_mix: Dict = {}
    accessibility: str
    related_evses: List[str] = []
    group_id: str
    pricing_policy: str
    realtime_data: bool

class CDR(BaseModel):
    id: str
    startDateTime: str
    endDateTime: str
    authId: str
    authMethod: str
    location: Optional[Location] = {}
    evseId: str
    connectorId: str
    meterId: str
    currency: str
    totalCost: float
    totalEnergy: float
    totalTime: float
    lastUpdated: str
    stopReason: Optional[str] = ""
    totalParkingTime: Optional[float] = 0.0
    totalReservationCost: Optional[float] = 0.0
    remark: Optional[str] = ""
    signedData: Optional[str] = ""
    relatedCDRs: List[str] = []
    locationReference: Dict = {}
    productData: Dict = {}
    chargingPreferences: Dict = {}
    environmentalImpact: Dict = {}
    cdrToken: Token
    chargingPeriods: List[ChargingPeriod] = []

class Command(BaseModel):
    id: str
    type: str
    data: dict

class Transaction(BaseModel):
    id: str
    meterStart: float
    timestamp: str
    idTag: str

class User(BaseModel):
    id: str
    name: str
    email: str
    verified: bool
