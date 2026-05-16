from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query, status
from app.data import applications
from app.schemas import ApplicationCreate, ApplicationResponse, ApplicationUpdate, ApplicationStatus

app = FastAPI(
    title="Internship Applications API",
    description="A mock backend API system for managing internship applications without a real database.",
    version="1.0.0",
)


def get_next_id() -> int:
    if not applications:
        return 1
    return max(application["id"] for application in applications) + 1


def find_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application
    return None


@app.get("/")
def home():
    return {
        "message": "Welcome to the Zaptek Internship Applications API",
        "docs": "/docs",
        "availableRoutes": [
            "GET /applications",
            "GET /applications/{id}",
            "POST /applications",
            "PUT /applications/{id}",
            "DELETE /applications/{id}",
        ],
    }


@app.get("/applications", response_model=list[ApplicationResponse])
def get_applications(
    status_filter: ApplicationStatus | None = Query(default=None, alias="status"),
    track: str | None = None,
    university: str | None = None,
):
    result = applications

    if status_filter:
        result = [app for app in result if app["status"] == status_filter]

    if track:
        result = [app for app in result if track.lower() in app["track"].lower()]

    if university:
        result = [app for app in result if university.lower() in app["university"].lower()]

    return result


@app.get("/applications/{application_id}", response_model=ApplicationResponse)
def get_single_application(application_id: int):
    application = find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application with id {application_id} was not found.",
        )

    return application


@app.post("/applications", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_application(new_application: ApplicationCreate):
    application = new_application.model_dump(mode="json")
    application["id"] = get_next_id()
    application["submittedAt"] = datetime.now(timezone.utc).isoformat()
    applications.append(application)
    return application


@app.put("/applications/{application_id}", response_model=ApplicationResponse)
def update_application(application_id: int, updated_data: ApplicationUpdate):
    application = find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application with id {application_id} was not found.",
        )

    updates = updated_data.model_dump(exclude_unset=True, mode="json")
    application.update(updates)
    return application


@app.delete("/applications/{application_id}")
def delete_application(application_id: int):
    application = find_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application with id {application_id} was not found.",
        )

    applications.remove(application)
    return {"message": f"Application with id {application_id} has been deleted successfully."}
