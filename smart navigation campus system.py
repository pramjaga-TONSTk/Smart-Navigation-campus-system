from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI(
    title="Smart Campus Navigation, Faculty Monitoring and Resource Analytics System",
    version="1.0.0"
)

router = APIRouter()

class Location(BaseModel):
    name: str
    category: str


class RouteRequest(BaseModel):
    start: str
    destination: str


class RouteResponse(BaseModel):
    start: str
    destination: str
    estimated_time_minutes: int
    path: list[str]


class FacultyStatus(BaseModel):
    faculty_id: str
    name: str
    department: str
    status: str
    location: str


class ResourceUsageSummary(BaseModel):
    total_rooms: int
    occupied_rooms: int
    utilization_rate: float
    high_demand_resources: list[str]


# Campus locations
campus_locations = [
    Location(name="Library", category="Academic"),
    Location(name="Admin Block", category="Administrative"),
    Location(name="Lab Complex", category="Research"),
    Location(name="Seminar Hall", category="Event"),
    Location(name="Cafeteria", category="Utility")
]


# Campus routes
campus_routes = {
    ("Library", "Central Walkway"): ["Library", "Central Walkway", "Lab Complex"],
    ("Admin Block", "Main Road"): ["Admin Block", "Main Road", "Library"],
    ("Cafeteria", "Seminar Hall"): ["Cafeteria", "Open Ground", "Seminar Hall"]
}


# Faculty data
faculty_data = [
    FacultyStatus(
        faculty_id="FAC101",
        name="Dr. Meena Iyer",
        department="Computer Science",
        status="In Class",
        location="Block A - Room 204"
    ),

    FacultyStatus(
        faculty_id="FAC102",
        name="Dr. Arjun Rao",
        department="Electronics",
        status="Available",
        location="Faculty Cabin E-12"
    ),

    FacultyStatus(
        faculty_id="FAC103",
        name="Dr. Kavya Nair",
        department="Mathematics",
        status="In Meeting",
        location="Conference Room"
    )
]


@router.get("/")
def root():
    return {"message": "Welcome to SCN-FMRA"}


@router.post(
    "/navigation/route",
    response_model=RouteResponse
)
def get_route(data: RouteRequest):

    key = (data.start, data.destination)

    path = campus_routes.get(
        key,
        [data.start, "Central Walkway", data.destination]
    )

    return RouteResponse(
        start=data.start,
        destination=data.destination,
        estimated_time_minutes=8,
        path=path
    )


@router.get(
    "/faculty/status",
    response_model=list[FacultyStatus]
)
def get_all_faculty_status():
    return faculty_data


@router.get(
    "/faculty/status/{faculty_id}",
    response_model=FacultyStatus
)
def get_faculty_by_id(faculty_id: str):

    for faculty in faculty_data:
        if faculty.faculty_id == faculty_id:
            return faculty

    return FacultyStatus(
        faculty_id="NA",
        name="Not Found",
        department="NA",
        status="Unavailable",
        location="Unknown"
    )


@router.get(
    "/analytics/resources",
    response_model=ResourceUsageSummary
)
def get_resource_summary():

    total_rooms = 40
    occupied_rooms = 28

    utilization_rate = round(
        (occupied_rooms / total_rooms) * 100,
        2
    )

    return ResourceUsageSummary(
        total_rooms=total_rooms,
        occupied_rooms=occupied_rooms,
        utilization_rate=utilization_rate,
        high_demand_resources=[
            "Seminar Hall",
            "AI Lab",
            "Library Study Rooms"
        ]
    )


app.include_router(router)