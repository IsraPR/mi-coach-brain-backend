# brain/schemas.py
from pydantic import BaseModel, Field


class Summary(BaseModel):
    current_role: str
    target_role: str
    strong_count: int
    growth_count: int
    blocker_count: int
    fastest_route_message: str


class Insight(BaseModel):
    title: str
    status: str
    role_requirement_status: list[str]
    why_blocking: str
    feedback_evidence: list[str]
    next_checkpoint: str


class MapNode(BaseModel):
    id: str
    label: str
    type: str
    category: str
    route_position: int
    connected_to: list[str]
    description: str
    insight: Insight


class CareerMap(BaseModel):
    summary: Summary
    map_nodes: list[MapNode]


class Roadmap(BaseModel):
    now: list[str]
    next: list[str]
    then: list[str]


class NextSteps(BaseModel):
    focus_area: str
    best_next_move: str
    why_now: str
    expected_evidence: list[str] = Field(default_factory=list)
    success_looks_like: list[str] = Field(default_factory=list)
    unlocks: list[str] = Field(default_factory=list)
    can_wait: list[str] = Field(default_factory=list)


class CareerPathResponse(BaseModel):
    """The final structured output expected from the Strands Agent."""

    career_map: CareerMap
    next_steps: NextSteps
