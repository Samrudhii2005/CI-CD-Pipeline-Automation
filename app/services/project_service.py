from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


def get_all_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def create_project(db: Session, project: ProjectCreate):
    new_project = Project(
        name=project.name,
        description=project.description,
        status=project.status
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def update_project(db: Session, project_id: int, updated_project: ProjectCreate):

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    project.name = updated_project.name
    project.description = updated_project.description
    project.status = updated_project.status

    db.commit()
    db.refresh(project)

    return project


def delete_project(db: Session, project_id: int):

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    db.delete(project)
    db.commit()

    return project