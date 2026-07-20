from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.schemas.project import ProjectCreate
from app.services.project_service import (
    get_all_projects,
    get_project,
    create_project,
    update_project,
    delete_project
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/")
def read_projects(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return get_all_projects(db)


@router.get("/{project_id}")
def read_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    project = get_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.post("/")
def add_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_project(db, project)


@router.put("/{project_id}")
def edit_project(
    project_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    updated = update_project(db, project_id, project)

    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")

    return updated


@router.delete("/{project_id}")
def remove_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    deleted = delete_project(db, project_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted successfully"}